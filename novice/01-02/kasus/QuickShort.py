def QuickSort(A,start,end):
    if start<end:
        pindex=partition(A,start,end)
        QuickSort(A,start,pindex-1)
        QuickSort(A,pindex+1,end)

    def partition(A,start,end):
        pivot = A[end]
        pindex = start
        for i in range(start,end):
            if (A[i] <= pivot):
                A[i],A[pindex]=A[pindex],A[i]
                pindex += 1
        A[pindex],A[end] = A[end],A[pindex]
        return pindex

A = [54,26,93,17,77,31,44,55,20]
QuickSort(A,0,len(A)-1)
print(A)