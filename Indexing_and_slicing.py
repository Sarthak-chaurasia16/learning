import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

#Indexing & Slicing(using indexing you fetch data from numpy array)
#INDEXING (Ek baar mein ek hi item ko fetch krte ho)
#print(a1[-1]) # -1 is a index number
#print(a1[1])
# 2d mein interesting hai kuki isme row and column number dena hota hai 
#print(a2[2,3]) # row and column number 0 se start honge like as index
#print(a3[0,1,0])# array , row and column number 0 se start honge like as index(1 3d mein 2 2d hote hai)
#print(a3[0,0,0])
#a4 = np.arange(16).reshape(2,2,2,2)
#print(a4[1,1,0,1])

#SLICING (Ek sath multiple item ko fetch kr skte ho)
#print(a1[2:5:2])#Ek certain number of line chahiye ho
#print(a2[0,:])#0 se matlab hai row konsi chahiye and fir column likhte hai and agar sab column chahiye toh ":"
#print(a2[:,3])
print(a2)
#print(a2[1:,1:3])#1: means 1 wali index row se sari row and 1:3 means 1 se 3 index wale column isko hum range bhi bol skte hai
#print(a2[::2,::3])#::2 means alternate wali chahiye like 1 chhod kar ek and ,::3 means 2 column ko skip krke
#2 bata raha hai ki 1st likhi 2 skip and 3 likhi 4th skip &&&& 3 bata raha hai pehli likhi toh 2,3 skip direct 4th wali likho
print(a2[::3,::2])