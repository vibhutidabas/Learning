
#very slow but in-place sorting so memory efficient, time-->O(N^2)
#checks if the next element is smaller, if it is it swaps places with it

def bubble(array):
    
    for i in range(len(array)-1):
        for j in range(0, len(array)-1-i, 1):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
            
    return array

def swap(array, i, j):
    t = array[i]
    array[i] = array[j]
    array[j] = t

a = [2,1,5,3,4]
print(bubble(a))