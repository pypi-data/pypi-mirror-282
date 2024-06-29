from .gradient import Variable


class FloatVariable(Variable):
    def __init__(self, init_val, step_width):
        self.val = init_val
        self.step_width = step_width

    def get_val(self):
        return self.val

    def next_step_variable(self):
        return FloatVariable(init_val=self.val + self.step_width,
                             step_width=self.step_width)

    def next_variable(self, func_val, next_step_func_val, learning_rate):
        return FloatVariable(init_val=self.val - (
                next_step_func_val - func_val) / self.step_width * learning_rate,
                             step_width=self.step_width)
