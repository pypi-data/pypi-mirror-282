from abc import ABC, abstractmethod
from typing import Union, List, Any
import ray
from ray import ObjectRef
from ...event import Event


class Observations(ABC):

    def __init__(self, objects: List[Any]):
        self._objects = objects

    @staticmethod
    def new(objects: Union[List[ObjectRef], List[Event]]):
        if len(objects) == 0:
            return Observations.empty()
        elif isinstance(objects[0], ObjectRef):
            return _ObservationsRemote(objects)
        elif isinstance(objects[0], Event):
            return _ObservationsLocal(objects)
        else:
            raise TypeError(f"Invalid observation type {type(objects[0])}.")

    @staticmethod
    def empty():
        return _ObservationsLocal([])

    @abstractmethod
    def __iter__(self):
        pass


class _ObservationsRemote(Observations):

    def __init__(self, objects: List[ObjectRef]):
        assert all([isinstance(obj, ObjectRef) for obj in objects])
        super().__init__(objects)

    def __iter__(self):
        return iter(ray.get(obj_ref) for obj_ref in self._objects)


class _ObservationsLocal(Observations):

    def __init__(self, objects: List[Event]):
        assert all([isinstance(obj, Event) for obj in objects])
        super().__init__(objects)

    def __iter__(self):
        return iter(self._objects)
