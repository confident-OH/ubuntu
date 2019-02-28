import numpy as np
from scipy.special import expit
class neuron:
    def __init__ (self, size):
        self.array_input = np.array([])
        self.array_hide = np.array([])
        self.array_output = np.array([])
        self.input_hide_weight = np.random.nomal(0, 1, (size, size))
        self.hide_output_weight = np.random.nomal(0, 1, (size, size))
        self.output_result_weight = np.random.nomal(0, 1, (size, 1))
    def train (array_input, result):
        self.array_input = np.array([array_input])
        self.array_hide = expit(self.array_input.dot(self.input_hide_weight))
        self.array_output = expit(self.array_hide.dot(self.hide_output_weight))
        item = self.array_output.dot(self.output_result_weight) - result

