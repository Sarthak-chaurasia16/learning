import numpy as np
#_______Making array for learning attributes________________________________________________
a1 = np.arange(16)
a2 = np.arange(12, dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)
#print(a1)
#print(a2)
#print(a3)
#___________________________________________________________________________________________

#ndim(Number of dimension)
#print(a2.ndim)
#print(a3.ndim)

#Shape(Har dimension mein kitne items hai)
#print(a2.shape)
#Size
#print(a2.size)
#itemsize(Tell about memory size)
#if i made np.int32 it's memory size is 4 because it takes 4 bits and normally it works with int64 so it is 8
#a4= np.arange(8,dtype= np.int32)
#print(a4.itemsize)

#dtype
#print(a1.dtype)

#-------------------------Changing Datatype------------------------------------------------
#astype()
#print(a3.astype(np.int32).itemsize)
#Array operation



#___________________________________________________________________________________________________
#Array Operation
#a1 = np.arange(12).reshape(3,4)
#a2 = np.arange(12,24).reshape(3,4)
#Scalar Operation or Arithmatic operation
#print(a1*3)
#Relational(Check element condition and give boolean form answer)
#print(a1>5)
#Vector Operation
#print(a1+a2)
#print(a1**a2)
#--------------------------------------------------------------------------------------------------

#____________________________Array Function ______________________________________________________________
a1 = np.random.random((3,3))
a1 = np.round(a1*100)
#print(a1)
#max/min/sum/product
#print(np.max(a1))
#print(np.min(a1))
#print(np.sum(a1))
#print(np.prod(a1))