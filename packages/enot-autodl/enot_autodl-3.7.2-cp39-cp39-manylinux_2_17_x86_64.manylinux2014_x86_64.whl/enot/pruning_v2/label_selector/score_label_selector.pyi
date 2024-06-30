from _typeshed import Incomplete
from enot.graph.ir.snapshot import Snapshot as Snapshot
from enot.pruning_v2.label import Label as Label
from enot.pruning_v2.label_selector.base import LabelSelector as LabelSelector, LatencyLabelSelector as LatencyLabelSelector
from enot.utils.common import Number as Number
from torch import nn as nn
from typing import Callable

class UniformLabelSelector(LabelSelector):
    """
    Label selector for uniform (equal) pruning.

    Removes an equal percentage of labels in each prunable layer.

    """
    pruning_ratio: Incomplete
    def __init__(self, pruning_ratio: float) -> None:
        """
        Parameters
        ----------
        pruning_ratio : float
            Ratio of prunable labels to remove in each group.

        """

class GlobalScoreLabelSelector(LabelSelector):
    """
    Label selector for global pruning.

    Selects the least important labels within network.

    """
    n_or_ratio: Incomplete
    def __init__(self, n_or_ratio: Number) -> None:
        """
        Parameters
        ----------
        n_or_ratio : Number
            Number of labels or labels ratio to remove within all network. If the parameter is in the range (0, 1),
            it is interpreted as a fraction of all prunable unique labels. If the parameter greater or equal to 1,
            it is interpreted as a number of labels to remove.

        """

class BinarySearchLatencyLabelSelector(LatencyLabelSelector):
    """
    Based on binary search algorithm label selector.

    It finds the model with latency as close as possible to the target latency parameter,
    and always selects the labels with the lowest scores.

    """
    def __init__(self, target_latency: float, latency_calculation_function: Callable[[nn.Module], float], selector_cb: Callable[[float, float], bool] | None = None) -> None:
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
        selector_cb : Optional[Callable[[float, float], bool]]
            An optional callback that is called at each iteration of the search process. The callback should take the
            current latency as the first parameter and the target latency as the second parameter and return True if
            the search procedure should be stopped, False otherwise. Can be used for logging and early stop.

        '''
