import pulp
from _typeshed import Incomplete
from enot.graph.ir.snapshot import Snapshot as Snapshot
from enot.pruning.label_selector.channel_selector_constraint import ChannelsSelectorConstraint as ChannelsSelectorConstraint, DefaultChannelsSelectorConstraint as DefaultChannelsSelectorConstraint
from enot.pruning_v2.label import Label as Label, score_sum as score_sum
from enot.pruning_v2.label_selector.base import LatencyLabelSelector as LatencyLabelSelector
from enot.utils.common import Number as Number
from torch import nn as nn
from typing import Callable, NamedTuple

class _KnapsackItem(NamedTuple):
    lp_variable: pulp.LpVariable
    labels: tuple[Label, ...]
    score: float
    latency: float

class KnapsackLabelSelector(LatencyLabelSelector):
    """
    Label selector based on knapsack algorithm.

    We assume that the label score is value and latency is weight from the
    classical algorithm, so :class:`~KnapsackLabelSelector` maximizes total score of the model with latency constraint.
    This algorithm cannot be used to find an exact solution because latency of labels have non-linear dependency, but
    the iterative approach gives good results. At each iteration, the label selector recalculates latency estimation
    for each label according to the selection at the previous iteration and solve knapsack problem with target latency
    constraint, until problem converged to this constraint.

    """
    strict_label_order: Incomplete
    verbose: Incomplete
    def __init__(self, target_latency: float, latency_calculation_function: Callable[[nn.Module], float], *, max_relative_latency_step: float = 0.5, strict_label_order: bool = True, constraint: ChannelsSelectorConstraint | None = None, max_iterations: int = 15, solver_execution_time_limit: Number | None = 60, verbose: bool = True) -> None:
        '''
        Parameters
        ----------
        target_latency : float
            Target model latency. This argument should have the same units as output of
            ``latency_calculation_function``.
        latency_calculation_function : Callable[[torch.nn.Module], float]
            Function that calculates model latency. It should take model (torch.nn.Module) and measure the "speed"
            (float) of its execution. It could be a number of FLOPs, MACs, inference time on CPU/GPU or other "speed"
            criteria.
        max_relative_latency_step : float
            Determines the maximum relative difference between the baseline latency and target latency for one knapsack
            iteration. The target latency for each iteration is calculated as
            ``max(latency * (1 - max_relative_latency_step), target_latency)`` that allows to minimize score loss in
            case of aggressive acceleration (more than x2). Value must be in the range (0, 1]. Default value is 0.5.
        strict_label_order : bool
            If True, then the labels within a group are always selected in ascending order of score, otherwise any
            order of selection is acceptable. Default value is True.
        constraint : Optional[ChannelsSelectorConstraint]
            Optional :class:`~enot.pruning.ChannelsSelectorConstraint` instance, that calculates low, high and step for
            the constraint for total number of labels in group. If None, then
            :class:`~enot.pruning.DefaultChannelsSelectorConstraint` will be used. None by default.
        max_iterations : int
            Maximum number of iterations. Default value is 15.
        solver_execution_time_limit : Optional[Number]
            Time limit in seconds for solving a linear problem at each iteration. Default value is 60.
        verbose : bool
            Whether to print selection statistics and show progress bar or not. True by default.

        '''
    @property
    def max_relative_latency_step(self) -> float:
        """Maximum relative difference between baseline latency and target latency for one knapsack iteration."""
    @max_relative_latency_step.setter
    def max_relative_latency_step(self, value: float) -> None: ...
    @property
    def max_iterations(self) -> int:
        """Maximum number of iterations."""
    @max_iterations.setter
    def max_iterations(self, value: int) -> None: ...
