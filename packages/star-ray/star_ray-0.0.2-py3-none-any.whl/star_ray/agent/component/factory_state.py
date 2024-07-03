from abc import ABC, abstractmethod
from typing import Union, List, Any

from ray.actor import ActorHandle
from ...event import Event
from ...environment import Ambient

from .factory_observations import _ObservationsLocal, _ObservationsRemote, Observations

__all__ = ("State",)


class State(ABC):

    @staticmethod
    def new(ambient: Union[Ambient, ActorHandle]):
        if isinstance(ambient, ActorHandle):
            return _AmbientWrapperRemote(ambient)
        elif isinstance(ambient, Ambient):
            return _AmbientWrapper(ambient)
        else:
            raise TypeError(f"Invalid ambient type {type(ambient)}.")

    @abstractmethod
    def update(self, actions: List[Event]) -> Observations:
        pass

    @abstractmethod
    def select(self, actions: List[Event]) -> Observations:
        pass


class _AmbientWrapperRemote(State):
    def __init__(self, ambient: ActorHandle):
        self._inner = ambient

    def update(self, actions: List[Event]) -> Observations:
        return _ObservationsRemote(
            [self._inner.__update__.remote(query) for query in actions]
        )

    def select(self, actions: List[Event]) -> Observations:
        return _ObservationsRemote(
            [self._inner.__select__.remote(query) for query in actions]
        )


class _AmbientWrapper(State):

    def __init__(self, ambient: Ambient):
        self._inner = ambient

    def update(self, actions: List[Event]) -> Observations:
        return _ObservationsLocal([self._inner.__update__(query) for query in actions])

    def select(self, actions: List[Event]) -> Observations:
        return _ObservationsLocal([self._inner.__select__(query) for query in actions])
