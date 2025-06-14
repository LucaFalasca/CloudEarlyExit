from dataclasses import dataclass

import numpy


@dataclass(frozen=True)
class TensorWrapper:
    tensor_name: str
    tensor_type: str
    tensor_shape: list
    numpy_array: numpy.ndarray


@dataclass(frozen=True)
class RequestInfo:
    requester_id: str
    request_idx: int
    callback_port: int
