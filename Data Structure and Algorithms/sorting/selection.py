#almost same as bubblesort but a little better(good for smaller arrays), linear search--> O(N)
#it finds the smallest element and swaps it to the left element

def selection(a):
    for i in range(len(a)-1):

        index = i
        for j in range(i+1, len(a), 1):
            if a[j] < a[index]:
                index = j

        if index != i:
            swap(a, index, i)

    return a

def swap(a, index, i):
    t = a[index]
    a[index] = a[i]
    a[i] = t

a = [1,8,3,3,5,2,6,9]
print(selection(a))