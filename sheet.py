from collections import defaultdict
from collections import deque

# Basics
# Variable assignment and type
a = 10
print(type(a))  # <class 'int'>
a = "20"  # Can re-assign variable types at runtime
print(type(a))  # <class 'str'>

# Multiple assignments
c, d = 1, 2  # Can assign multiple variables at once
e = f = g = 1  # Can assign the same value to multiple variables, safe for immutable types (int, float, str, tuple)

# Conditional and Loop Structures
for i in range(5):  # Starts at 0, increments by +1, end value is not included
    print(i)  # Output: 0, 1, 2, 3, 4

for i in range(5, 1, -1):  # Explicitly starts at 5, decrements by 1
    print(i)  # Output: 5, 4, 3, 2

array = [1, 2, 3, 4, 5]

# Loop through iterable
for element in array:
    if element == 2:
        continue  # Skip the rest of the loop body when element == 2, also works in while loops
    print(element)  # Output: 1, 3, 4, 5

# Enumerate loop
for index, value in enumerate(array):
    if value == 3:
        break  # Terminate loop immediately, also works in while loops
    print(index, value)  # Output: 0 1, 1 2

# While loop with a condition
condition = True
while condition:
    condition = False  # Exit loop after one iteration

# Functions
def main():
    def helper():  # You can define functions within other functions
        print("helper")
    helper()
    return 1

# List Operations
lst = [1, 2, 3]
lst[0]  # Access first element
lst.append(4)
lst.pop()
lst.remove(2)
lst.sort()
lst.reverse()
len(lst)  # Length of the list

# String Operations
s = "hello"
s.upper()
s.lower()
s.split(",")
s.strip()
s.replace("h", "j")

# Sorted function and sort method
sorted_list = sorted(lst)  # Returns a new sorted list
lst.sort()  # Sorts in place

# Tuple Operations
tuple_example = (0, 1)
first, second = tuple_example  # Unpack tuple into variables

# Useful Built-in Functions (work for all iterables)
iterable = [1, 2, 3]
print(sum(iterable))  # Output: 6
print(max(iterable))  # Output: 3
print(min(iterable))  # Output: 1
print(len(iterable))  # Output: 3

# Collections and Data Structures
# Queue
queue = deque(iterable)
queue.popleft()  # Removes and returns the first element at front of queue
queue.append(4) # Add value 4 to end of queue

# Set
set_example = set() # Unordered collection of unique values
set_example.add(4) # Add value 4 to top of set
set_example.remove(4) # Reove value 4 from set

# Stack
stack = [] # Stacks are implemented as lists
stack.append(1) # Add value 1 to top of stack
stack.pop() # Removes and returns the first element at top of stack

# Tuples
tup = (1, 2, 3)
tup[0]  # Output: 1

# Dictionaries
dictionary = {}
default_dict = defaultdict(int)

for value in array:
    if value not in dictionary:  # Check before incrementing
        dictionary[value] = 0
    dictionary[value] += 1  # Encounter key error if value is not in dictionary

    default_dict[value] += 1  # No key error due to default value of 0

value_of_key_zero = default_dict[0]  # Access dictionary values using key
dictionary_keys = dictionary.keys()  # Get dictionary keys
dictionary_values = dictionary.values()  # Get dictionary values
dictionary_items = dictionary.items()  # Get dictionary items (Array of (Key, Value) tuples)

for key, item in dictionary_items:
    print(item, key)

# Classes/OOP in Python
class Dog:
    # Constructor method to initialize attributes
    def __init__(self, name, age):
        self.name = name  # Instance variable 'name'
        self.age = age  # Instance variable 'age'

    def display_info(self):  # Each method in a class must have self as the first parameter
        print(f"Name: {self.name}, Age: {self.age}")

    def bark(self):
        self.display_info()  # Can call other methods in the class using self instance
        print(f"{self.name} says Woof!")

# Example usage of the Dog class
my_dog = Dog("Buddy", 5)
my_dog.bark()  # Output: Name: Buddy, Age: 5 \n Buddy says Woof!
