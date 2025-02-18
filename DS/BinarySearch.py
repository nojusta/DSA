def binary_search(array, target):
    """
    Performs binary search on a sorted array.
    
    Parameters:
        array (list): A sorted list of elements.
        target (any): The value to search for in the array.
        
    Returns:
        int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1
    
    return -1 

if __name__ == "__main__":
    # Example 1: searching for an element that exists:
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    index = binary_search(sorted_array, target)
    if index != -1:
        print(f"Target {target} found at index {index}.")
    else:
        print(f"Target {target} not found in array.")

    # Example 2: Searching for an element that does not exist
    target = 8
    index = binary_search(sorted_array, target)
    if index != -1:
        print(f"Target {target} found at index {index}.")
    else:
        print(f"Target {target} not found in array.")
    
"""
Benefits and use cases
    Efficiency:
     Binary search runs in O(log n)ime. 
    Prerequisite:
     The array (or list) must be sorted to use BS.
    Use cases:
     Searching for records in a sorted database.
     Debugging or finding specific values in large datasets.
     Useful in algorithms where the problem can be reduced to a search problem.
"""
