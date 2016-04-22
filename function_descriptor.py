import numpy as np


class FunctionDescriptor(object):
    """ This class can be used to describe a general C function which receives multiple parameters
    and loops over one of the parameters, executing a given body of statements inside the loop
    """

    """ Pass the name and the body of the function
        Also pass skip_elements, which is an array of the number of elements to skip in each dimension
        while looping
    """
    def __init__(self, name, body):
        self.name = name
        self.body = body
        self.matrix_params = []
        self.value_params = []

    """ Add a parameter to the function
        A function may have any number of parameters but only one may be the looper
        Each parameter has an associated name and shape
    """
    def add_matrix_param(self, name, num_dim, dtype):
        self.matrix_params.append({'name': name, 'num_dim': num_dim, 'dtype': dtype})

    """ Declare a new value (scalar) param for this function
        Param_type: numpy dtype
        name: name of the param
    """
    def add_value_param(self, param_type, name):
        self.value_params.append((np.dtype(param_type), name))

    @property
    def params(self):
        return self.matrix_params + self.value_params