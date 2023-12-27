arr = [8,4,5,9, 10, 12, 20, 200, 1000, 1]
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
def selection_sort(arr):
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                swap(arr, i, j)
    return arr

# selection_sort(arr) 

def merge(left, right, arr, i, j, a, b):
    if a<b:

        if (j <= 0) or(i>0 and left[i-1]>right[j-1]):
            arr[b-1] = left[i-1]
            i = i-1
        else:
            arr[b-1] = right[j-1]
            j = j-1
        merge(left, right, arr, i, j, a, b-1)
def merge_sort(arr, a = 0, b = None):
    
    if b is None: b = len(arr)
    if 1< b -a:
        c = (a+b+1)//2
        merge_sort(arr, a, c)
        merge_sort(arr, c, b)
        left = arr[a:c]
        right = arr[c:b]
        merge(left, right, arr, len(left), len(right), a, b)

        
merge_sort(arr, 0, None)

print(arr) 