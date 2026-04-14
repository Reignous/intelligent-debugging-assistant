Python 3.14.3 (v3.14.3:323c59a5e34, Feb  3 2026, 11:41:37) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
# Bug 1: Off-by-one error
def get_last_items(lst, n):
    return lst[len(lst) - n - 1:]  # Returns one extra item

# Bug 2: Mutable default argument
def append_item(item, collection=[]):
...     collection.append(item)
...     return collection  # Shared across all calls!
... 
... # Bug 3: Integer division surprise
... def average(numbers):
...     return sum(numbers) / 2  # Divides by 2 instead of len(numbers)
... 
... # Bug 4: Wrong variable in loop
... def multiply_all(numbers, factor):
...     result = []
...     for num in numbers:
...         result.append(numbers * factor)  # Should be num, not numbers
...     return result
... 
... # Bug 5: Missing return in recursion
... def factorial(n):
...     if n == 0:
...         return 1
...     n * factorial(n - 1)  # Forgot return keyword
... 
... # Bug 6: String vs integer comparison
... def is_adult(age):
...     if age > "18":  # Comparing int to string
...         return True
...     return False
... 
... # Bug 7: Shallow copy trap
... def double_matrix(matrix):
...     result = matrix[:]  # Shallow copy — inner lists still shared!
...     for row in result:
...         for i in range(len(row)):
...             row[i] *= 2
...     return result  # Also modifies original matrix
... 
... # Bug 8: Exception swallowed silently
... def safe_divide(a, b):
...     try:
...         return a / b
...     except:
