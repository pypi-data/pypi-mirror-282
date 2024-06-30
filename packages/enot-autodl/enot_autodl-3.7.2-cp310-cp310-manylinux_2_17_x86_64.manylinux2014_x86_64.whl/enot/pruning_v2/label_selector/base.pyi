import abc
from _typeshed import Incomplete
from abc import ABC
from enot.graph.ir.snapshot import Snapshot as Snapshot
from enot.pruning.label_selector.channel_selector_constraint import ChannelsSelectorConstraint as ChannelsSelectorConstraint, DummyChannelsSelectorConstraint as DummyChannelsSelectorConstraint
from enot.pruning_v2.ir import PruningIR as PruningIR
from enot.pruning_v2.label import Label as Label
from torch import nn as nn
from typing import Callable

class LabelSelector(ABC, metaclass=abc.ABCMeta):
    """
    Base class for all pruning label selectors. Label selector implements an algorithm that selects a set of labels
    for pruning with minimum score loss according input parameters.

    This class defines an abstract method :meth:`PruningLabelSelector._select` that should implement selection
    algorithm.

    """
    def __init__(self, constraint: ChannelsSelectorConstraint | None = None) -> None: ...
    def select(self, snapshot: Snapshot) -> list[Label]:
        """
        Method that chooses which labels should be pruned based on current label selector policy.

        .. warning::
            Depending on label selector implementation, this function may have significant execution time.

        Parameters
        ----------
        snapshot : Snapshot
            Target snapshot.

        Returns
        -------
        list of Label
            List of labels which should be pruned.

        """

class LatencyLabelSelector(LabelSelector, metaclass=abc.ABCMeta):
    """Base class for all label selectors that selects a set of labels for pruning with minimum score loss and desired
    pruned model latency."""
    latency_calculation_function: Incomplete
    def __init__(self, target_latency: float, latency_calculation_function: Callable[[nn.Module], float], constraint: ChannelsSelectorConstraint | None = None) -> None:
        '''
        Parameters
        ----------
        target_latency : float
            Target model latency. This argument should have the same units as output of
            ``latency_calculation_function``.
        latency_calculation_function : Callable[[torch.nn.Module], float]
            Function that calculates model latency.
            It should take model (torch.nn.Module) and measure the "speed" (float) of its execution.
            It could be a number of FLOPs, MACs, inference time on CPU/GPU or other "speed" criteria.

        '''
    @property
    def target_latency(self) -> float:
        """Desired latency of the pruned model."""
    @target_latency.setter
    def target_latency(self, value: float) -> None: ...
    def select(self, snapshot: Snapshot) -> list[Label]: ...

class LatencyMeasurementError(Exception):
    """Must be raised by a latency measurement function if the measurement
    cannot be performed for a particular model configuration."""
