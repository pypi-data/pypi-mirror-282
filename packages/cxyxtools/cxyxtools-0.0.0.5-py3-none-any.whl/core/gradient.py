import abc
from typing import List, Any


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

    @abc.abstractmethod
    def next_variable(self, func_val, next_step_func_val, learning_rate):
        """
        根据学习率得到的下一个变量
        :param func_val:
        :param next_step_func_val:
        :param learning_rate:
        :return:
        """

    def __str__(self):
        return str(self.get_val())


def _get_variable(func, args, learning_rate, round_number):
    variables: List[Variable] = list(args)
    index = 0
    while index < round_number:
        last_func_val = func(*variables)
        next_variables = []
        for i in range(len(variables)):
            var_list = variables[:]
            var_list[i] = var_list[i].next_step_variable()
            next_variables.append(
                variables[i].next_variable(last_func_val, func(*var_list),
                                           learning_rate))
        variables = next_variables
        index += 1
    result = {}
    for v, k in zip(variables, func.__annotations__):
        result[k] = v
        print(f"{k} -> {v}")
    return result


def gradient_wrapper(func=None, round_number=1000, learning_rate=0.1):
    def inner(*args, **kwargs):
        return _get_variable(func, args, learning_rate, round_number)

    if func is None:
        def outer_wrapper(fun):
            def inner_2(*args, **kwargs):
                return _get_variable(fun, args, learning_rate, round_number)

            return inner_2

        return outer_wrapper
    return inner
