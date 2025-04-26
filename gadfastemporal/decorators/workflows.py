import typing

from gadfastemporal import typings
from temporalio import workflow as _workflow


def workflow(cls: typings.Class) -> typings.Class:
    return typing.cast(typings.Class, _workflow.defn(cls))


def run(func: typings.Func) -> typings.Func:
    return typing.cast(typings.Func, _workflow.run(func))
