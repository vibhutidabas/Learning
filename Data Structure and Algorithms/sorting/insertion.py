#same as selection, good for small arrays, ADAPTIVE sorting
#if the element before the element is greater then it swaps(many shifts)

def insertion(a):

    for i in range(len(a)):
        j=i

        while j > 0 and a[j-1]>a[j]:
            swap(a,j,j-1)
            j-=1

    return a

def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t

a = [1,6,4,8,2,3] 
print(insertion(a))