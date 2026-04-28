a = [1, 2, 3]
b = a

b[0] = 100

print("List a:", a)
print("List b:", b)
print("ID of a:", id(a))
print("ID of b:", id(b))

"""
ANSWERS:
1. Why did both lists change? 
   Because 'b = a' does not create a new list; it creates a reference. 
   Both variables point to the same object in memory.

2. Why are ids same? 
   The id() function returns the memory address. Since both variables 
   refer to the exact same list object, their addresses are identical.

3. What does this mean? 
   This is called 'aliasing'. It means modifying the list through one 
   variable will reflect in the other because they are not independent copies.
"""
