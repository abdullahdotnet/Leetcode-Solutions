import numpy as np
import random
myarr1 = np.random.randint(500,1500,100)
myarr2 = np.random.randint(500,1500,100)
myarr3 = np.random.randint(500,1500,100)


data = np.resize(myarr1,myarr2,myarr3,axis=1)
print(data)

