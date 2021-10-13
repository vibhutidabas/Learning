#divide and conquer sort, best for sorting linked list
#time complexity-->O(NlogN)
#in-place no but stable yes
#introsort = quicksort + heapsort
#timsort = insertion_sort + mergesort

def merge_sort(a):

    if len(a)==1:
        return

    middle = int(len(a)/2)

    left = a[:middle]
    right = a[middle:]

    merge_sort(left)
    merge_sort(right)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i+=1
        else:
            a[k] = right[j]
            j+=1
        
        k+=1
    
    while i < len(left):
        a[k] = left[i]
        i+=1
        k+=1

    while j < len(right):
        a[k] = right[j]
        j+=1
        k+=1

a = [9,2,7,4,5,3,1,10]
merge_sort(a)
print(a)