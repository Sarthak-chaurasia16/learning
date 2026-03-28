#Creating numpy array
"""
import numpy as np
#1D array 
arr_1D = np.array([10,23,45]) #Vector
print(arr_1D,"\n")
#2D array & 3D array
arr_2D = np.array([[1,2,3], [56,45,67]]) #Matrices
print(arr_2D,"\n")

arr_3D = np.array([[1,2,3], [56,45,67],[98,78,98]]) #Tensor
print(arr_3D,"\n")

# dtype Function
Data_type1=np.array([1,2,3],dtype = float)
print(Data_type1)

                                    #OR
Data_type2=np.array([1,2,3],dtype = bool)
print(Data_type2)
                                    #OR
Data_type3=np.array([1,2,3],dtype = complex)
print(Data_type3)


#Arange function(like loop)
arange1 = np.arange(1,7,1)#np.arange(Start,Stop,Step which skip)
print(arange1)

#reshape function(Andar woh value hi de skte ho jisse exact utna bada shape bann raha hoga ) 
reshape1 = np.arange(0,24).reshape(2,3,4) #This make a array from vector to any other type or shape like matrices
print(reshape1,"\n")

#np.ones & np.zeros(For making inner elements is ones or zeroes)
#Utlity is that if i want to initialize a value fast , i use this functions
ones1 =np.ones((3,4))
print(ones1)
zeroes1 = np.zeros((2,3))
print(zeroes1,"\n")

#np.random(For initialize the random value in the matrices)
random1 = np.random.random((3,4)) #np.random is function in numpy and extra .random is function in python for random value
print(random1)

#np.linspace(Linear space or linearly separate krta hai)
#ye given range mein equal distance par point generate krta hai
a = np.linspace(-10,10,10)
print(a)

#np.identity use for making identity matrices
b = np.identity(3)
print(b)
"""