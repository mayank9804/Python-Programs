def quickSort(alist,start,end):
    if start<end:
        # print(start,end)
        # print(f"I just got {alist[start:end+1]}")
        # print("Going to calculate the split point! Heading towards partition")
        splitpoint = partition(alist,start,end)
        # print(f"I got {splitpoint} as the splitpoint.")
        # print(f"QuickSort to left half of {alist[start:end+1]}")
        quickSort(alist,start,splitpoint-1)
        # print(f"QuickSort to right half of {alist[start:end+1]}")
        quickSort(alist,splitpoint+1,end)

def partition(alist,start,end):
    # Mark the first element as pivot element
    pivot = alist[start]

    leftmark = start+1
    rightmark = end
    done = False

    # print(f"Parition is ready to operate on {alist[start:end+1]} with pivot as {pivot}")


    while not done:

        while(alist[leftmark]<=pivot and leftmark<=rightmark):
            leftmark+=1

        while(alist[rightmark]>=pivot and rightmark>=leftmark):
            rightmark-=1

        if rightmark<leftmark:
            done = True
        else:
            alist[leftmark],alist[rightmark]=alist[rightmark],alist[leftmark]
            # print(f"I just swapped left {leftmark} and right {rightmark} marks! See me--->{alist[start:end+1]}")

    alist[start],alist[rightmark]=alist[rightmark],alist[start]
    # print(f"I just swapped pivot and right mark! See me--->{alist[start:end+1]}")

    return rightmark
alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist,0,len(alist)-1)
print(alist)
