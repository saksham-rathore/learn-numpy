# with default values
# np.zeros(shape) (3) fir 1d, (3,3) 2d

import numpy as np
zeros_array = np.zeros(3)
print(zeros_array)


# ones (shape)
import numpy as np
ones_array = np.ones((2,3))
print(ones_array)

# full(shape, value)
import numpy as np
filled_array = np.full((2,3),8)
print(filled_array)

# creating sequences of numbers in numpy
# arange()
# arange(start,stop,step)
import numpy as np
arr = np.arange(1,10,2)
print(arr)

# creating identity matrices
# eye(size)
import numpy as np
identity_matrix = np.eye(4)
print(identity_matrix)