from enum import Enum, auto

def broadcast_required_shape(left_shape, right_shape):
    return [1] * len(right_shape) + [*left_shape], [*(right_shape)] + [1] * len(left_shape)

def broadcast_large_dims(large_shape, small_shape):
    return [*small_shape] + [1] * (len(large_shape) - 1)

def combine_mask_index(left, mask):
    return left + (mask,)

class ScalarDefault(Enum):
    max = auto()
    min = auto()
    middle = auto()

def scalar_default_value(scalar_default: ScalarDefault, eps=1e-6):
    if scalar_default == ScalarDefault.max:
        return 1 - eps
    elif scalar_default == ScalarDefault.min:
        return eps
    else:
        return 0.5

def empty_function(*args, **kwargs):
    pass