import abc
from typing import List, Any, Dict


class Variable(abc.ABC):
    @abc.abstractmethod
    def get_val(self) -> Any:
        """
        返回值
        :return:
        """

    @abc.abstractmethod
    def next_step_variable(self):
        """
        下一个步长的变量对象
        :return:
        """
        return Variable()

    @abc.abstractmethod
    def next_variable(self, func_val, next_step_func_val, learning_rate):
        """
        根据学习率得到的下一个变量
        :param func_val:
        :param next_step_func_val:
        :param learning_rate:
        :return:
        """
        return Variable()

    def __str__(self):
        return str(self.get_val())


class Optimal:
    def __init__(self, optimal_args=None, optimal_kwargs=None,
                 optimal_val=None):
        self.optimal_args = optimal_args
        self.optimal_kwargs = optimal_kwargs
        self.optimal_val = optimal_val

    def _parse_func_return(self, val, args, kwargs):
        if val < self.optimal_val:
            self.optimal_val = val
            self.optimal_args, self.optimal_kwargs = args, kwargs

    def __str__(self):
        kw = {}
        for k, v in self.optimal_kwargs.items():
            if isinstance(v, Variable):
                kw[k] = v.get_val()
            else:
                kw[k] = v
        return f"最终解\n最小值\t: {self.optimal_val} \nargs\t:{[item.get_val() if isinstance(item,Variable) else item for item in self.optimal_args]} \nkwargs\t:{kw}"

    def __call__(self, func):
        def inner(*args, **kwargs):
            val = func(*args, **kwargs)
            self._parse_func_return(val, args, kwargs)
            return val

        return inner


def _get_variable(func, args, kwargs, learning_rate, round_number):
    optimal = Optimal(args, kwargs, func(*args, **kwargs))
    func = optimal(func)

    variables_args: List[Variable] = list(args)
    variables_kwargs: Dict[str, Variable] = kwargs
    index = 0
    var_args_index_list = [i for i in range(len(args)) if
                           isinstance(args[i], Variable)]
    var_kwargs_k_list = [k for k, v in variables_kwargs.items() if
                         isinstance(v, Variable)]
    while index < round_number:
        last_func_val = func(*variables_args, **variables_kwargs)
        next_args = variables_args[:]
        next_kwargs = {k: v for k, v in variables_kwargs.items()}
        for i in var_args_index_list:
            var_list = variables_args[:]
            var_list[i] = var_list[i].next_step_variable()
            next_args[i] = variables_args[i].next_variable(
                last_func_val, func(*var_list, **variables_kwargs),
                learning_rate)
        for k in var_kwargs_k_list:
            kwar_dict = {k: v for k, v in variables_kwargs.items()}
            kwar_dict[k] = kwar_dict[k].next_step_variable()
            next_kwargs[k] = variables_kwargs[k].next_variable(
                last_func_val, func(*variables_args, **kwar_dict),
                learning_rate)
        variables_args = next_args
        variables_kwargs = next_kwargs
        index += 1

    return optimal


def gradient_wrapper(func=None, round_number=1000, learning_rate=0.1):
    def inner(*args, **kwargs):
        return _get_variable(func, args, kwargs, learning_rate, round_number)

    if func is None:
        def outer_wrapper(fun):
            def inner_2(*args, **kwargs):
                return _get_variable(fun, args, kwargs, learning_rate,
                                     round_number)

            return inner_2

        return outer_wrapper
    return inner
