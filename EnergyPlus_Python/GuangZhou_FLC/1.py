# @Time    : 2024/2/18 16:08
# @Author  : Bobby Johnson
# @Project : Reinforcement Learning 
# @File    : 1
# @Software: PyCharm
# @Targets :
from pyfmi import load_fmu
import numpy as np
model = load_fmu('cond_test.fmu')
opts = model.simulate_options()
print(opts)
a = np.linspace(1,10,10)
print(a)