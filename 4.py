#Nested to Flat List

def nested_to_flattened(lst):
    flattened = []
    
    for item in lst:
        if isinstance(item, list):
            flattened.extend(nested_to_flattened(item))  # Recursively flatten the nested list
        else:
            flattened.append(item)  # Append the non-list element
    
    return flattened

# Example usage
L = [1, 2, [3, 4, 5], 6, [7, 8], 9]
print(nested_to_flattened(L))
