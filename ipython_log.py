# IPython log file

import numpy
numpy.  # Move your cursor to after the period and press the <tab> key 
get_ipython().run_line_magic('pinfo', 'numpy.sum')
get_ipython().run_line_magic('magic', '')
get_ipython().run_line_magic('magic', '')
get_ipython().run_line_magic('time', 'for var in range(1000): var += var')
get_ipython().run_line_magic('time', 'for var in range(1000): var += var ** var')
get_ipython().run_line_magic('timeit', '%run utils/timeit.py')
def time_it():
    for var in range(1000): 
        var += var ** var
get_ipython().run_line_magic('timeit', 'time_it')
get_ipython().run_line_magic('logstart', '')
4 + 7
print("Groot save the world")
get_ipython().run_line_magic('logoff', '')
