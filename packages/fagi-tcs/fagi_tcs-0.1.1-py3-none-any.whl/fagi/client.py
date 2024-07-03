import concurrent.futures as cf
import os
import time
from typing import Dict, Optional, Tuple, Union
import uuid

from requests_futures.sessions import FuturesSession

from fagi.bounded_executor import BoundedExecutor
from fagi.utils import (
    API_KEY_ENVVAR_NAME,
    MAX_FUTURE_YEARS_FROM_CURRENT_TIME,
    MAX_NUMBER_OF_EMBEDDINGS,
    MAX_PAST_YEARS_FROM_CURRENT_TIME,
    SECRET_KEY_ENVVAR_NAME,
)
from fagi.utils import (
    AuthError,
    InvalidAdditionalHeaders,
    InvalidNumberOfEmbeddings,
    InvalidValueType,
)
from fagi.utils import (
    Embedding,
    Environments,
    ModelTypes,
    ObjectDetectionLabel,
    RankingActualLabel,
    RankingPredictionLabel,
)
from fagi.utils import is_timestamp_in_range

from fagi.utils import logger

PredictionLabelTypes = Union[
    str,
    bool,
    int,
    float,
    Tuple[str, float],
    ObjectDetectionLabel,
    RankingPredictionLabel,
]
ActualLabelTypes = Union[
    str,
    bool,
    int,
    float,
    Tuple[str, float],
    ObjectDetectionLabel,
    RankingActualLabel,
]


class Client:
    def __init__(
        self,
        api_key,
        secret_key,
        uri="http://localhost:8000",
        max_workers=8,
        max_queue_bound=5000,
        timeout=200,
        additional_headers=None,
    ) -> None:
        api_key = api_key or os.getenv(API_KEY_ENVVAR_NAME)
        secret_key = secret_key or os.getenv(SECRET_KEY_ENVVAR_NAME)
        if api_key is None or secret_key is None:
            raise AuthError(api_key, secret_key)
        self._uri_event = f"{uri}/log/event/"
        self._uri_model = f"{uri}/log/model/"
        self._timeout = timeout
        self._session = FuturesSession(
            executor=BoundedExecutor(max_queue_bound, max_workers)
        )

        self._headers = {
            "X-Api-Key": api_key,
            "X-Secret-Key": secret_key,
        }

        if additional_headers is not None:
            conflicting_keys = self._headers.keys() & additional_headers.keys()
            if conflicting_keys:
                raise InvalidAdditionalHeaders(conflicting_keys)
            self._headers.update(additional_headers)

    def _now(self):
        return time.time()

    def log(
        self,
        model_id: str,
        model_type: ModelTypes,
        environment: Environments,
        model_version: Optional[str] = None,
        # prediction_id: Optional[Union[str, int, float]] = None,
        prediction_timestamp: Optional[int] = None,
        prediction_label: Optional[PredictionLabelTypes] = None,
        actual_label: Optional[ActualLabelTypes] = None,
        features: Optional[Dict[str, Union[str, bool, float, int]]] = None,
        embedding_features: Optional[Dict[str, Embedding]] = None,
        tags: Optional[Dict[str, Union[str, bool, float, int]]] = None,
        batch_id: Optional[str] = None,
    ) -> cf.Future:
        try:
            if not isinstance(model_id, str):
                raise InvalidValueType("model_id", model_id, "str")
            if not isinstance(model_type, ModelTypes):
                raise InvalidValueType("model_type", model_type, "fagi.utils.types.ModelTypes")
            # Validate environment
            if not isinstance(environment, Environments):
                raise InvalidValueType("environment", environment, "fagi.utils.types.Environments")
            if environment == Environments.VALIDATION:
                if (
                    batch_id is None
                    or not isinstance(batch_id, str)
                    or len(batch_id.strip()) == 0
                ):
                    raise ValueError(
                        "Batch ID must be a nonempty string if logging to validation environment."
                    )

            prediction_id = str(uuid.uuid4())

            # Validate feature types
            if features:
                if not isinstance(features, dict):
                    raise InvalidValueType("features", features, "dict")

            # Validate embedding_features type
            if embedding_features:
                if not isinstance(embedding_features, dict):
                    raise InvalidValueType("embedding_features", embedding_features, "dict")
                if len(embedding_features) > MAX_NUMBER_OF_EMBEDDINGS:
                    raise InvalidNumberOfEmbeddings(len(embedding_features))

            # Check the timestamp present on the event
            if prediction_timestamp is not None:
                if not isinstance(prediction_timestamp, int):
                    raise InvalidValueType(
                        "prediction_timestamp", prediction_timestamp, "int"
                    )
                # Send warning if prediction is sent with future timestamp
                now = int(time.time())
                if prediction_timestamp > now:
                    logger.warning(
                        "Caution when sending a prediction with future timestamp."
                        "fagi only stores 2 years worth of data. For example, if you sent a prediction "
                        "to fagi from 1.5 years ago, and now send a prediction with timestamp of a year in "
                        "the future, the oldest 0.5 years will be dropped to maintain the 2 years worth of data "
                        "requirement."
                    )
                if not is_timestamp_in_range(now, prediction_timestamp):
                    raise ValueError(
                        f"prediction_timestamp: {prediction_timestamp} is out of range."
                        f"Prediction timestamps must be within {MAX_FUTURE_YEARS_FROM_CURRENT_TIME} year in the "
                        f"future and {MAX_PAST_YEARS_FROM_CURRENT_TIME} years in the past from the current time."
                    )

                    # Construct the prediction

            # TODO:
            p = prediction_label
            a = actual_label

            record = {
                "model_id": model_id,
                "model_type": model_type.value,
                "environment": environment.value,
                "model_version": model_version,
                "prediction_id": prediction_id,
                "prediction_timestamp": prediction_timestamp,
                "prediction_label": p,
                "actual_label": a,
                "features": features,
                "embedding_features": embedding_features,
                "tags": tags,
                "batch_id": batch_id,
            }

            return self._post(record=record, uri=self._uri_model, indexes=None)
        except Exception as e:
            logger.error(f"Error while processing the fagi request - {str(e)}")


    def track(
        self,
        event_name,
        environment: Environments,
        prediction_id=None,
        event_timestamp: Optional[int] = None,
        properties=None,
    ) -> cf.Future:
        all_properties = {
            # 'mp_lib': 'python',
            # '$lib_version': __version__,
        }

        if properties:
            all_properties.update(properties)

        record = {
            "prediction_id": prediction_id,
            "event": event_name,
            "properties": all_properties,
            "time": event_timestamp or self._now(),
            "environment": environment.value,
        }

        return self._post(record=record, uri=self._uri_event, indexes=None)

    def _post(self, record, uri, indexes):
        resp = self._session.post(
            uri,
            headers=self._headers,
            timeout=self._timeout,
            # json=MessageToDict(message=record, preserving_proto_field_name=True),
            json=record,
        )
        if indexes is not None and len(indexes) == 2:
            resp.starting_index = indexes[0]
            resp.ending_index = indexes[1]
        return resp

