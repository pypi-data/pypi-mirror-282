from abc import ABC, abstractmethod
from typing import Union, List

from ray.actor import ActorHandle
from ..event import Event
from ..environment import Ambient

from .wrapper_observations import _ObservationsLocal, _ObservationsRemote, _Observations

__all__ = ("_State",)


class _State(ABC):

    @staticmethod
    def new(ambient: Union[Ambient, ActorHandle]):
        if isinstance(ambient, ActorHandle):
            return _StateWrapperRemote(ambient)
        elif isinstance(ambient, Ambient):
            return _StateWrapper(ambient)
        else:
            raise TypeError(f"Invalid ambient type {type(ambient)}.")

    @abstractmethod
    def update(self, actions: List[Event]) -> _Observations:
        pass

    @abstractmethod
    def select(self, actions: List[Event]) -> _Observations:
        pass


class _StateWrapperRemote(_State):
    def __init__(self, ambient: ActorHandle):
        self._inner = ambient

    def update(self, actions: List[Event]) -> _Observations:
        return _ObservationsRemote(
            [self._inner.__update__.remote(query) for query in actions]
        )

    def select(self, actions: List[Event]) -> _Observations:
        return _ObservationsRemote(
            [self._inner.__select__.remote(query) for query in actions]
        )


class _StateWrapper(_State):

    def __init__(self, ambient: Ambient):
        self._inner = ambient

    def update(self, actions: List[Event]) -> _Observations:
        return _ObservationsLocal([self._inner.__update__(query) for query in actions])

    def select(self, actions: List[Event]) -> _Observations:
        return _ObservationsLocal([self._inner.__select__(query) for query in actions])
