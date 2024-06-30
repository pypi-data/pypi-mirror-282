import torch
from torch import nn
from torch.cuda.amp import GradScaler as GradScaler
from torch.optim.optimizer import Optimizer
from typing import Any, Callable, overload

class GTBaselineOptimizer:
    """
    Recommended optimizer for baseline training and tuning after pruning.
    GTBaselineOptimizer allows to achieve better metrics in most cases.

    During training, the metrics inside the closure may be measured several times,
    so to avoid this, you can use the following example of measurement.

    Examples
    --------
    >>> from enot.optimization import GTBaselineOptimizer

    Create GTBaselineOptimizer and pass it a model and a base optimizer.

    >>> opt = SGD(model.parameters())
    >>> optimizer = GTBaselineOptimizer(model, opt)

    Use GTBaselineOptimizer to do optimizer step and collect training statistics.
    Note that the metrics inside the closure may be measured several times,
    so to avoid this, you can use the following example of measurement.

    >>> epoch_accuracy = 0
    >>> for inputs, labels in dataloader:
    >>>     step_accuracy = []
    >>>
    >>>     def closure():
    >>>         optimizer.zero_grad()
    >>>         outputs = model(inputs)
    >>>         loss = criterion(outputs, labels)
    >>>         loss.backward()
    >>>
    >>>         if len(step_accuracy) == 0:
    >>>             accuracy = calculate_accuracy(outputs, labels)
    >>>             step_accuracy.append(accuracy)
    >>>
    >>>         return loss
    >>>
    >>>     optimizer.step(closure)
    >>>     epoch_accuracy += step_accuracy[0]
    >>> epoch_accuracy /= len(dataloader)

    Notes
    -----
    Use this optimizer simultaneously in train and tune procedure or do not use at all.
    The performance of this optimizer is two times lower than performance of base optimizer,
    and memory consumption is 1.5 times higher than memory consumption of base optimizer.

    """
    def __init__(self, model: nn.Module, optimizer: Optimizer | Any, *, allow_non_optimizer: bool = False, **kwargs) -> None:
        """
        Parameters
        ----------
        model : torch.nn.Module
            PyTorch model to optimize.
        optimizer : torch.optim.Optimizer
            PyTorch optimizer which will be wrapped by our optimizer.

        """
    @property
    def model(self) -> nn.Module:
        """
        Model passed to the constructor.

        Returns
        -------
        torch.nn.Module
            PyTorch model passed to the optimizer constructor.

        """
    @property
    def param_groups(self) -> list[dict[str, Any]]:
        """
        Returns ``param_groups`` variable of the wrapped optimizer.

        Returns
        -------
        list with dict with str keys
            User optimizer parameter groups.

        """
    def state_dict(self) -> dict[str, Any]:
        """
        Call ``state_dict`` of the wrapped optimizer and return the result.

        Returns
        -------
        dict with str keys
            User optimizer state dict.

        """
    def load_state_dict(self, state_dict: dict[str, Any]) -> None:
        """
        Call ``load_state_dict`` of the wrapped optimizer.

        Parameters
        ----------
        state_dict : dict with str keys
            State dict to be loaded to user optimizer instance.

        """
    def zero_grad(self, set_to_none: bool = True) -> None:
        """Call ``zero_grad`` of the wrapped optimizer."""
    def add_param_group(self, param_group: dict[str, Any]) -> None:
        """
        Call ``add_param_group`` of the wrapped optimizer.

        Parameters
        ----------
        param_group : dict with str keys
            Parameter group description to add to user optimizer.

        """
    @overload
    def model_step(self, closure: Callable[[], float]) -> float: ...
    @overload
    def model_step(self, closure: Callable[[], torch.Tensor]) -> torch.Tensor: ...
    @overload
    def step(self, closure: None = ..., scaler: GradScaler | None = None) -> None: ...
    @overload
    def step(self, closure: Callable[[], float], scaler: GradScaler | None = None) -> float: ...
    @overload
    def step(self, closure: Callable[[], torch.Tensor], scaler: GradScaler | None = None) -> torch.Tensor: ...

class _AmpHelperOptimizer(torch.optim.Optimizer):
    """
    A helper optimizer for AMP support.

    This class is intended to be used internally by the GTBaselineOptimizer
    for handling AMP-specific operations. It helps in integrating
    AMP's gradient scaling mechanism by triggering the `step` function.

    Examples
    --------
    Create class instance and pass it a list of parameter groups to be optimized.

    >>> amp_helper_optimizer = _AmpHelperOptimizer(self.param_groups)

    Trigger GradScaler's step function and check if the step function of _AmpHelperOptimizer was called.

    >>> scaler.step(amp_helper_optimizer)
    >>> if amp_helper_optimizer.is_triggered:
    >>>     # do something
    >>> else:
    >>>     # do something

    """
    def __init__(self, params: list[dict[str, Any]]) -> None:
        """
        Parameters
        ----------
        params : list with dict with str keys
            List of parameter groups to be optimized.

        """
    @property
    def is_triggered(self) -> bool:
        """
        Returns whether the optimizer step has been triggered.

        Returns
        -------
        bool
            True if the optimizer step has been triggered, False otherwise.

        """
    @overload
    def step(self, closure: None = ...) -> None: ...
    @overload
    def step(self, closure: Callable[[], float]) -> float: ...
    @overload
    def step(self, closure: Callable[[], torch.Tensor]) -> torch.Tensor: ...
