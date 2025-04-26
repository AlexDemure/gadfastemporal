import typing

from gadfastemporal import typings
from temporalio import activity as _activity


def activity(func: typings.Func) -> typings.Func:
    method = func.__name__

    instance = None

    if hasattr(func, "__qualname__"):
        qualname_parts = func.__qualname__.split(".")
        if len(qualname_parts) > 1:
            instance = qualname_parts[-2]

    if instance:
        activity_name = f"{instance}.{method}"
    else:
        activity_name = method

    return typing.cast(typings.Func, _activity.defn(name=activity_name)(func))
