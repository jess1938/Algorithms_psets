##################################################
##  Problem 3.4. Find order
##################################################

# Given a list of positive integers and the starting integer s, return x such that x is the smallest value greater than
# or equal to s that's not present in the list
def find_first_missing_element(arr, s):
    '''
    Inputs: 
        arr        (list(int)) | List of sorted, unique positive integer order id's
        s          (int)       | Positive integer
    Output: 
        -          (int)       | The smallest integer greater than or equal to s that's not present in arr
    '''
    
    #if array is empty
    if not arr: 
        return s
    
    #3 pointers: left (l), right (r), and middle (mid)
    l = 0 
    r = len(arr)-1
    mid = (l + r) // 2

    while l != mid: 
        if arr[mid] > s: #binary search left side 
            r = mid 
            mid = (l+r) // 2
        elif arr[mid] < s: #binary search right side 
            l = mid 
            mid = (l+r) // 2
        else: 
            break
    
    if arr[mid] == s: #if s in array then find smallest missing element
        l = mid 
        r = len(arr) - 1
        mid = (l + r) // 2
        
        while l != mid: 
            #if no missing element search right side
            if (mid - l) == (arr[mid] - arr[l]): 
                l = mid 
                mid = (l+r) // 2
            #if find a missing element keep looking in left side
            else:
                r = mid 
                mid = (l+r) // 2
    else: 
        return s
    
    #check if after l=mid the right side has a missing element
    if (r - mid) == arr[r]-arr[mid]: 
        return arr[len(arr)-1]+1
    else:
        return arr[l] + 1
     
    