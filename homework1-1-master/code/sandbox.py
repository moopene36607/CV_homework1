import numpy as np
import scipy.ndimage as ndimage

arr3D = np.array([[[1, 2, 2, 3, 4, 5], [1, 2, 2, 3, 4, 5], [1, 2, 2, 3, 4, 5]], 
                  [[1, 1, 2, 3, 4, 5], [1, 1, 2, 3, 4, 5], [1, 1, 2, 3, 4, 5]], 
                  [[1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 3, 4]],
                  [[1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 3, 4], [1, 1, 2, 2, 3, 4]],])
#arr3D.size = 72
#len(arr3D) = 4,        i.e y=4
#len(arr3D[0]) = 3,     i.e x=3
#len(arr3D[0][0]) = 10  i.e channel=10
#t_arr3D = [ii for ii in arr3D.shape if ii > 0]
#print(t_arr3D)

imfilter = np.array([[1,1,1], [1,1,1], [1,1,1]])
output = np.zeros_like(arr3D)
for ch in range(arr3D.shape[2]):
    print(arr3D[:,:,ch]) 
    output[:,:,ch] = ndimage.filters.correlate(image[:,:,ch], imfilter, mode='constant')


print("---")
print(arr3D.size)
print(arr3D)
arr3D = np.pad(arr3D, ((0, 0), (0, 0), (2, 2)), 'constant')
a=len(arr3D)
b=len(arr3D[0])
c=len(arr3D[0][0])
print(a)
print(b)
print(c)
d=arr3D.shape[0] 
e=arr3D.shape[1]
f=arr3D.shape[2]
print(d)
print(e)
print(f)


print (arr3D)
print ("-----------")
#print ('constant:  \n' + str(np.pad(arr3D, ((10, 1), (0, 0), (1, 1)), 'constant')))

'''
print ('edge:  \n' + str(np.pad(arr3D, ((0, 0), (1, 1), (2, 2)), 'edge')))
print ('linear_ramp:  \n' + str(np.pad(arr3D, ((0, 0), (1, 1), (2, 2)), 'linear_ramp')))
print ('maximum:  \n' + str(np.pad(arr3D, ((0, 0), (1, 1), (2, 2)), 'maximum')))
print ('mean:  \n' + str(np.pad(arr3D, ((0, 0), (1, 1), (2, 2)), 'mean')))
print ('median:  \n' + str(np.pad(arr3D, ((0, 0), (1, 1), (2, 2)), 'median')))
print ('minimum:  \n' + str(np.pad(arr3D, ((0, 0), (1, 1), (2, 2)), 'minimum')))
print ('reflect:  \n' + str(np.pad(arr3D, ((0, 0), (1, 1), (2, 2)), 'reflect')))
print ('symmetric:  \n' + str(np.pad(arr3D, ((0, 0), (1, 1), (2, 2)), 'symmetric')))
print ('wrap:  \n' + str(np.pad(arr3D, ((0, 0), (1, 1), (2, 2)), 'wrap')))
'''