# 11th June - Python (Functions Assignment) - 1
"""

1. What is a lambda function in Python, and how does it differ from a regular function?

a lambda function is a small anonymous function.It is also known as an inline function or a lambda expression.
Unlike regular functions defined using the def keyword, lambda functions are created using the lambda keyword.

primarily used for simple tasks, while regular functions are named, multi-line functions that can handle more
complex operations. The choice between using a lambda function or a regular function depends on the specific
requirements and context of the code.

"""
"""
2. Can a lambda function in Python have multiple arguments? If yes, how can you define and use
them?

Yes, a lambda function in Python can have multiple arguments.

add_lambda = lambda x, y: x + y

result = add_lambda(3, 5)
print(result)  # Output 8 
"""
""""
3. How are lambda functions typically used in Python? Provide an example use case.

lambda functions are typically used in Python in combination with higher-order functions such as map(), filter(),
and reduce().

example

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

even_numbers_list = list(even_numbers)

print(even_numbers_list)  # Output: [2, 4, 6, 8, 10]
"""
"""

4. What are the advantages and limitations of lambda functions compared to regular functions in
Python?

Advantages of Lambda Functions:

Concise syntax: Lambda functions allow you to write simple.

No function name required: Since lambda functions are anonymous, they do not require a function name.
This makes them useful for small, temporary tasks that do not need to be referenced elsewhere in the code.

Ideal for higher-order functions: Lambda functions are often used as arguments to higher-order functions like map(),
filter(), and reduce(). They are well-suited for these functional programming constructs, 
where concise and simple functions are often needed.

Limitations of Lambda Functions:

Single expression limitation: Lambda functions are restricted to a single expression,
which means they cannot contain multiple statements or complex logic. 

Lack of readability: While lambda functions can be concise, they can also become hard to read if the expression becomes
 too complex. 

Limited error messages: Since lambda functions don't have a name, error messages may not provide as much context

when debugging. Regular functions with meaningful names can provide better error messages, making debugging easier.

"""
"""
5. Are lambda functions in Python able to access variables defined outside of their own scope?
Explain with an example.

Yes, lambda functions in Python can access variables defined outside of their own scope.

def multiplier_factory(factor):
    return lambda x: x * factor
multiply_by_5 = multiplier_factory(5)

result1 = multiply_by_5(2)  # 2 * 5 = 10
result2 = multiply_by_5(3)  # 3 * 5 = 15

print(result1)  # Output: 10
print(result2)  # Output: 15

"""
"""
6. Write a lambda function to calculate the square of a given number.

square_lambda = lambda x: x ** 2

"""
"""
7. Create a lambda function to find the maximum value in a list of integers.

find_max = lambda lst: max(lst)

numbers = [10, 7, 25, 14, 32, 18]
result = find_max(numbers)
print(result)  # Output: 32

"""
"""
8. Implement a lambda function to filter out all the even numbers from a list of integers.


filter_even = lambda lst: list(filter(lambda x: x % 2 == 0, lst))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even(numbers)
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

"""
"""

9.Write a lambda function to sort a list of strings in ascending order based on the length of each
string.

sort_by_length = lambda lst: sorted(lst, key=len)

words = ["apple", "banana", "orange", "grape", "kiwi"]
sorted_words = sort_by_length(words)
print(sorted_words)  # Output: ['kiwi', 'grape', 'apple', 'banana', 'orange']
"""

"""
10. Create a lambda function that takes two lists as input and returns a new list containing the
common elements between the two lists.""



find_common_elements = lambda lst1, lst2: list(filter(lambda x: x in lst2, lst1))

"""
"""
11 Write a recursive function to calculate the factorial of a given positive integer.

def factorial(n):
    # Base case: Factorial of 0 is 1
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)  # Calculate the factorial of 5
print(result)  # Output: 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)

"""
"""
12. Implement a recursive function to compute the nth Fibonacci number.

def fibonacci(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
"""

"""

13.Create a recursive function to find the sum of all the elements in a given list.
def list_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + list_sum(lst[1:])

"""

"""
14. Write a recursive function to determine whether a given string is a palindrome.


def is_palindrome(s):
    # Base case: If the string has zero or one character, it is a palindrome
    if len(s) <= 1:
        return True
    # Recursive case: Check if the first and last characters are the same,
    # and recursively check the substring between them
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

word = "yes you can"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")

"""
"""
15. Implement a recursive function to find the greatest common divisor (GCD) of two positive integers.

def gcd(a, b):
    if b == 0:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(b, a % b)
"""











































