# 3 . Write a Python function to count the occurrences of a specific element in a list.

def count_element(list, element):
  return list.count(element)

# Example usage:
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(count_element(numbers, 3))  

# Output: 3