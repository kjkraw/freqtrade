from typing import Callable, Optional


def stepped_roi(steps: dict) -> Callable[[int], Optional[float]]:
    """
    Return a callable for the stepped roi, the original roi system for
    freqtrade.
    :param steps: A dictionary of roi values which are used after a certain
    elapsed time.
    :returns: A function which returns the minimum roi for the amount of
    time elapsed.
    """
    def _roi_fn(trade_dur: int) -> Optional[float]:
        keys_list = list(filter(lambda x: x <= trade_dur, steps.keys()))
        if not keys_list:
            return None
        key = max(keys_list)
        return steps[key]

    return _roi_fn


def linear_roi(m: float, b: float) -> Callable[[int], Optional[float]]:
    """
    A simple linear function for calculating roi. Form: y = mx + b
    :param m: The slope of the line
    :param b: The y-intercept of the line
    :returns: function which returns the minimum ROI for the trade duration.
    """
    return lambda x: m * x + b


def exponential_roi(a: float, b: float, p: float, k: float):
    """
    An exponential function for calculating roi. form y = ab^(x/P) + k
    :param a: The coefficient for the function
    :param b: The base of the function
    :param p: The period of the function
    :param k: The y-offset of the function
    """
    return lambda x: a * b ** (x / p) + k
