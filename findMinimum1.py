#############################
#Models and file needed
import findMinimum
import numpy as np

#############################
#The main block
if __name__=='__main__':
    arr=np.array([1,2,4,5,6,7,8])
    m=findMinimum.findMin(arr)
    print(m)