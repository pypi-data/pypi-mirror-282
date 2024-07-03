# # TODO this is a work in progress...


# import inspect
# from typing import List, Type
# from ...utils import _LOGGER
# from ..agent import Agent
# from ..component import (
#     ActiveActuator,
#     ActiveComponent,
#     ActiveSensor,
#     ATTEMPT_METHOD_CLS_VAR,
# )


# import inspect


# def _fully_qualified_name(cls):
#     return cls.__module__ + "." + cls.__qualname__
# )

# def ActionRouter(sensors: List[Type] | None, actuators: List[Type] | None):
#     """
#     This class decorator implements automatic action routing. When an agent decides upon an action in `__cycle__` the typically pattern is to manually call an `attempt` method for an appropriate actuator. This class enables automatic routing of actions based on the `route_events` attribute of the `attempt` decorator (see [ActiveComponent.attempt]).

#     """
#     if sensors is None:
#         sensors = []
#     if actuators is None:
#         actuators = []
#     components = actuators + sensors  #
#     # validate component types
#     for cls in components:
#         if not isinstance(
#             cls, type
#         ):  # TODO check that they are also subclasses of Sensor and Actuator?
#             raise ValueError(
#                 f"Action router requires Sensor/Actuator types but received {cls}"
#             )

#     def _router(cls):
#         _LOGGER.debug(f"ActionRouter on class {cls} Found attempt methods: ")
#         for component_cls in components:
#             attempt_methods = getattr(component_cls, ATTEMPT_METHOD_CLS_VAR)
#             attempt_methods.route_events

#         # this method is used to attempt all actions, they will be automatically routed to the correct actuator.
#         cls.attempt

#     return _router
