import numpy as np
from numpy import random

# arr = np.size([[1,2,3],[4,5,6]])
# arr = np.shape([[1,2,3],[4,5,6]])
# arr = np.ndim([[1,2,3],[4,5,6]])
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)

# print(arr[1,0])

# arr = np.zeros((10,4))
# print(arr)

# arr = np.eye(5)
# print(arr)

# arr = np.array([10,20,30,40,50,45])
# print(arr[1:4])


# a = arr.reshape(2,3)
# print(a)

# arr = np.ones((2,3))
# print(arr)

# arr = np.array([1,2,3])
# b=np.mean(arr)
# b=np.median(arr)
# b=np.std(arr)
# b=np.min(arr)
# b=np.max(arr)
# b=np.random.rand(3,3)
# b=np.random.randint(1,10,5)
# print(b)

# arr = np.array([[1,2,1],[4,2,6]])

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])   # from1-D to 2 - D
# newarr = arr.reshape(3,4)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])   # from 1-D to 3-D
# newarr = arr.reshape(2,2,3)
# print(newarr)

# a = np.array([1,2,3])   # adding two array into one array
# b = np.array([6,3,5])
# arr = np.concatenate((a,b))
# print(arr)
# print(a + 3)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # split the 1-D array
# newarr = np.array_split(arr,3)
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  #for finding element index number
# new = np.where(arr == 4) # printing value index
# new = np.where(arr%2 == 0)  #odd numbers
# new1 = np.where(arr%2 == 1)  #even numbers
# print(new)
# print(new1)
# x = np.searchsorted(arr, 3)
# print(x)

# arr = np.array([3,5,7,2,4,3,9])  #sorting array
# print(np.sort(arr))

# arr = np.array([1,2,3,4])    #filter array
# x = arr[[True, False, True, True]]
# print(x)

# arr = np.array([1,2,3,4], dtype="i")
# print(arr) 
# print(arr.dtype)

# arr = np.array([1,2,3,4])  
# x = arr.view()
# x = arr.copy()
# arr[0] = 40

# print(arr)
# print(x)

# arr = np.array([[1,2,3],[5,6,7]])  # printing shape of array

# arr = np.array([1,2,3,4] , ndmin=5)
# print(arr)
# print(arr.shape)
# print(arr.ndim)

# arr = np.array([[1,2,3],[5,6,7]])   #iterting the array

# for x in arr:
#     print(x)

# arr = np.array([[1,2,3],[5,6,7]])   #iterting the 2-D array

# for x in arr:
#     for y in arr:
#         print(y)


# x = random.choice(5,1)
# print(x)