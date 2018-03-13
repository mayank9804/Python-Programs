# The code below applies the merge sort on an array and apply binary search on it
# Uncomment the comment part to follow the recursion and backtracking properly

def mergeSort(alist):

    if len(alist) > 1:
        # print("Splitting {}".format(alist))
        mid = len(alist) //2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]
        # print("------>leftHalf={}".format(leftHalf))
        # print("------>rightHalf={}".format(rightHalf))
        # print("Heading to left side")
        mergeSort(leftHalf)
        # print("Heading to right side")
        mergeSort(rightHalf)
        # print(f"Currently I am at {alist}.My left and right halves are {leftHalf} and {rightHalf} respectively.")
        # print("Let's merges the two halves")
        # print(f"Merging {leftHalf} and {rightHalf}")
        merge(leftHalf,rightHalf,alist)
        # print(f"Left and right half got merged in sorted order!{alist}")
        # print("Going back")

    # else:
    #     print("Can't split it more! Going back")

# Merge Algorithm
def merge(leftHalf,rightHalf,alist):
    il=jr=0
    result = []
    while(len(result)<len(leftHalf)+len(rightHalf)):
        if leftHalf[il]<=rightHalf[jr]:
            result.append(leftHalf[il])
            il+=1
        elif leftHalf[il]>rightHalf[jr]:
            result.append(rightHalf[jr])
            jr+=1

        if (il == len(leftHalf)):
            result.extend(rightHalf[jr:])
        elif (jr == len(rightHalf)):
            result.extend(leftHalf[il:])
    j = 0
    for i in result:
        alist[j]=i
        j+=1

alist = [7,6,5,4,3,2,1,32,65,3,6,95]
mergeSort(alist)
print(alist)



# Apply's Binary Search on sorted Array
def binarySearch(n,alist):
    if len(alist) <=0:
        return False
    else:
        midpoint = (len(alist)-1)//2
        if alist[midpoint] == n:
            return True
        elif alist[midpoint] > n:
            return binarySearch(n,alist[:midpoint])
        elif alist[midpoint]<n:
            return binarySearch(n,alist[midpoint+1:])
n = int(input("Enter the number you want to search").strip())
print(binarySearch(n,alist))
