from typing import Any, List
import random

from .gradient import Variable


class BorderedIntegerVariable(Variable):
    """
    有边界 Int 变量
    """

    def __init__(self, init_val: int, step_width: int = 1,
                 max_val: int = None,
                 min_val: int = None):
        assert max_val is not None or min_val is not None
        if max_val is not None and init_val >= max_val:
            init_val = max_val
            step_width = -(abs(step_width))
        if min_val is not None and init_val <= min_val:
            init_val = min_val
            step_width = abs(step_width)
        self.val = init_val
        self.step_width = step_width
        self.max = max_val
        self.min = min_val

    def get_val(self) -> Any:
        return self.val

    def next_step_variable(self):
        return BorderedIntegerVariable(self.val + self.step_width,
                                       self.step_width, self.max, self.min)

    def next_variable(self, func_val, next_step_func_val, learning_rate):
        step = (next_step_func_val - func_val) \
               / self.step_width * learning_rate
        if 0 < step < 1:
            step = 1
        elif -1 < step < 0:
            step = -1
        else:
            step = int(step)
        return BorderedIntegerVariable(init_val=self.val - step,
                                       step_width=self.step_width,
                                       max_val=self.max, min_val=self.min)


class BorderedFloatVariable(Variable):
    """
    有边界 Float 变量
    """

    def __init__(self, init_val: float, step_width: float, max_val=None,
                 min_val=None):
        assert max_val is not None or min_val is not None
        if max_val is not None and init_val >= max_val:
            init_val = max_val
            step_width = -(abs(step_width))
        if min_val is not None and init_val <= min_val:
            init_val = min_val
            step_width = abs(step_width)
        self.val = init_val
        self.max = max_val
        self.min = min_val
        self.step_width = step_width

    def get_val(self) -> float:
        return self.val

    def next_step_variable(self):
        return BorderedFloatVariable(
            self.val + self.step_width,
            self.step_width, self.max, self.min)

    def next_variable(self, func_val, next_step_func_val, learning_rate):
        return BorderedFloatVariable(init_val=self.val - (
                next_step_func_val - func_val) / self.step_width * learning_rate,
                                     step_width=self.step_width,
                                     max_val=self.max, min_val=self.min)


class BorderLessIntegerVariable(Variable):
    """
    无边界 int 变量
    """

    def __init__(self, init_val: int = 0, step_width=1):
        self.val = init_val
        self.step_width = step_width

    def get_val(self) -> int:
        return self.val

    def next_step_variable(self) -> Variable:
        return BorderLessIntegerVariable(self.val + self.step_width,
                                         self.step_width)

    def next_variable(self, func_val, next_step_func_val,
                      learning_rate) -> Variable:
        step = (next_step_func_val - func_val) \
               / self.step_width * learning_rate
        if 0 < step < 1:
            step = 1
        elif -1 < step < 0:
            step = -1
        else:
            step = int(step)
        return BorderedFloatVariable(init_val=self.val - step,
                                     step_width=self.step_width)


class BorderLessFloatVariable(Variable):
    """
    无边界 float 变量
    """

    def __init__(self, init_val: float, step_width: float):
        self.val = init_val
        self.step_width = step_width

    def get_val(self) -> float:
        return self.val

    def next_step_variable(self) -> Variable:
        return BorderLessFloatVariable(init_val=self.val + self.step_width,
                                       step_width=self.step_width)

    def next_variable(self, func_val, next_step_func_val,
                      learning_rate) -> Variable:
        return BorderLessFloatVariable(init_val=self.val - (
                next_step_func_val - func_val) / self.step_width * learning_rate,
                                       step_width=self.step_width)


class EnumVariable(Variable):
    """
    可枚举类型变量
    """

    def __init__(self, choices: List[Any], init_index: int = 0):
        assert len(choices) > 1
        self.choices = choices
        self._init_index = init_index
        self.next_index = 0
        self.randint_max = len(self.choices) - 1

    def get_val(self) -> Any:
        return self.choices[self._init_index]

    def next_step_variable(self):
        random_index = random.randint(0, self.randint_max)
        while random == self._init_index:
            random_index = random.randint(0, len(self.choices))
        self.next_index = random_index
        return EnumVariable(self.choices, random_index)

    def next_variable(self, func_val, next_step_func_val, learning_rate):
        if next_step_func_val < func_val:
            return EnumVariable(self.choices, self.next_index)
        return self
