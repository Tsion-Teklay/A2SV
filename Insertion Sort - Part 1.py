def insertionSort1(n, arr):
    n=len(arr)
    stored=arr[n-1]
    
    for i in range(n-2,-1,-1):
        if arr[i]>=stored:
            arr[i+1]=arr[i]
            print(' '.join(map(str,arr)))
        else:
            arr[i+1]=stored
            break
    
    if arr[0]>stored:
        arr[1]=arr[0]
        arr[0]=stored
    print(' '.join(map(str,arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
