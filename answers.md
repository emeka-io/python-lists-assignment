# Assignment Answers

## Task 6: Memory Model
- **Both lists changed** because lists are mutable objects and `b = a` creates a reference, not a copy.
- **The IDs are the same** because both variables point to the same memory location.
- **This means** that any changes made to `b` are actually being made to the object that `a` also points to.
