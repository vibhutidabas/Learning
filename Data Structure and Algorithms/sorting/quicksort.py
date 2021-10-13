#comparison so not faster than linear time complexity
#it runs with O(NlogN) and worst is O(N^2), used in primitive programs
#inplace yes but stable no
#to understand again refer lecture.126

def quicksort(a, low, high):

    if low >= high:
        return

    pivot = partition(a, low, high)                        #pivot-->middle index
    quicksort(a, low, pivot-1)
    quicksort(a, pivot+1, high)

def partition(a, low, high):

    pivot = (low + high)//2
    i = low

    for j in range(low, high, 1):
        if a[j] <= a[high]:
            swap(a, i, j)
            i+=1
        
    swap(a, i ,high)
    return i

def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t


a = [1,8,2,6,4,0,9]
quicksort(a, 0 ,len(a)-1)
print(a)