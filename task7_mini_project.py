student = ["Emeka Builds", 22, "Computer Science", 4.5, "Nigeria"]

# Initial Print
print(f"Name: {student[0]}")
print(f"Age: {student[1]}")
print(f"Department: {student[2]}")
print(f"CGPA: {student[3]}")
print(f"Country: {student[4]}")

# Mutation
student[2] = "Software Engineering"
student[3] = 4.8

print("\n--- Updated Record ---")
print(student)

print("\n--- Reversed Record ---")
print(student[::-1])

print("\n--- First Three Values ---")
print(student[:3])
