#Function Assignment

#Theory Questions and Answers
#1. What is the difference between a function and a method in Python?
'''A function is a block of code defined outside of a class, while a method is a function that is defined inside a class and is associated with an object.
Example:
Function: def greet(): return "Hello"
Method: class Person: def greet(self): return "Hello from method!"'''

#2. Explain the concept of function arguments and parameters in Python.
'''Parameters are variables listed in the function's definition, while arguments are the values passed to the function when it is called.
Example: 
def add(a, b): # 'a' and 'b' are parameters
    return a + b
print(add(3, 4)) # 3 and 4 are arguments'''

#3. What are the different ways to define and call a function in Python?
'''Functions can be defined using the 'def' keyword and called by their name followed by parentheses.
Example:
def greet(): return "Hello!"
print(greet()'''

#4. What is the purpose of the `return` statement in a Python function?
'''The `return` statement is used to send a result back to the caller of the function.
Example: 
def square(x): return x * x
print(square(5)) # Output: 25'''

#5. What are iterators in Python and how do they differ from iterables?
'''An iterable is an object that can be looped over, and an iterator is an object that produces the next value when called with `next()`.
Example:
Iterable: [1, 2, 3]
Iterator: iter([1, 2, 3])'''

#6. Explain the concept of generators in Python and how they are defined.
'''Generators are functions that yield values one at a time using the `yield` keyword.
Example:
def gen_numbers(): for i in range(3): yield i'''

#7. What are the advantages of using generators over regular functions?
'''Generators save memory because they produce items one at a time and do not store the entire sequence in memory.
Example:
Generator: def gen(): yield 1
Regular: return [1, 2, 3]'''

#8. What is a lambda function in Python and when is it typically used?
'''Lambda functions are anonymous, single-expression functions often used for short, simple tasks.
Example: 
lambda x: x * 2'''

#9. Explain the purpose and usage of the `map()` function in Python.
'''The `map()` function applies a given function to all items in an iterable.
Example:
map(lambda x: x * 2, [1, 2, 3])'''

#10. What is the difference between `map()`, `reduce()`, and `filter()` functions in Python?
'''map() applies a function to each item, filter() selects items based on a condition, reduce() reduces items to a single value.
Example:
map: map(lambda x: x+1, [1,2,3])
filter: filter(lambda x: x>2, [1,2,3])
reduce: reduce(lambda x,y: x+y, [1,2,3])'''


#Practical Answer 

#1. Function to sum even numbers in a list:
'''def sum_even_numbers(numbers):
  return sum(num for num in numbers if num % 2 == 0)'''


#2. Function to reverse a string:
'''def reverse_string(s):
    return s[::-1]'''


#3. Function to return a list of squares:
'''def square_numbers(numbers):
    return [num ** 2 for num in numbers]'''


#4. Function to check if a number is prime:
'''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True'''


#5. Iterator class for Fibonacci sequence:
'''class Fibonacci:
    def __init__(self, n_terms):
        self.n_terms = n_terms
        self.current = 0
        self.next = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n_terms:
            raise StopIteration
        result = self.current
        self.current, self.next = self.next, self.current + self.next
        self.count += 1
        return result'''


#6. Generator function for powers of 2:
'''def powers_of_two(max_exponent):
    for i in range(max_exponent + 1):
        yield 2 ** i'''

#7. Generator function to read a file line by line:
'''def read_file_line_by_line(filename):
    with open(filename, 'r') as file:
        for line in file:
         yield line.strip()'''


#8. Lambda function to sort tuples by the second element:
'''tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])print(sorted_tuples)'''


#9. map() to convert Celsius to Fahrenheit:
'''celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))print(fahrenheit) '''

#10. filter() to remove vowels from a string:
'''def remove_vowels(s):
    return ''.join(filter(lambda x: x.lower() not in 'aeiou', s))'''

#11. Accounting routine for book shop:
'''orders = [
    [34587, "Learning Python", 4, 40.95],
    [98762, "Programming in C", 3, 56.80],
    [77226, "Head First Java", 2, 32.95],
    [88112, "Data Science Handbook", 1, 24.99]
]

result = list(map(lambda x: (x[0], x[2] * x[3] + (10 if x[2] * x[3] < 100 else 0)), orders))print(result)'''




