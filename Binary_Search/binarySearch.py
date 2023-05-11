# In a nutshell, this search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison. 

# Compare x with the middle element.
# If x matches with the middle element, we return the mid index.
# Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
# Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.

# Time Complexity: O(log n)

# Program to implement binary search in Python 
# To find the element in the list and return its index

# In Recursive way
# The parameters are: array, lower bound, higher bound, and the element to be searched
def binarySearch (arr, low, high, x):
    # It checks if the high index is greater than or equal to low index
    # ie, eg : [2, 3, 4, 10, 40 ] -> low = 0, high = 4
    if high >= low:
        # It finds the middle element of the array
        # eg: mid = 2
        mid = (high+low)//2
        # It checks if the middle element is equal to the element to be searched
        if arr[mid] == x:
            return mid
        # It checks if the middle element is greater than the element to be searched
        # eg: element to be searched = 10 and mid = 2 and arr[mid] = 4 
        if arr[mid] > x:
            # If the above condition is true then it calls the binarySearch function again
            # By changing the high index to mid-1
            return binarySearch(arr, low, mid-1, x)
        
        if arr[mid] < x:
            return binarySearch(arr, mid+1, high, x)
        
    return -1      

#  Itrative way
def binarySearch(arr, x):

    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low)//2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1    
        
        else:
            return mid


arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)