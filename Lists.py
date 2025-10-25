# === 📋 List Practice and Comprehension in Python ===

# 1️⃣ Creating Lists
fruits = ["apple", "banana", "mango", "grapes", "kiwi"]
print("Original list of fruits:", fruits)

# 2️⃣ Accessing & Slicing
print("First fruit:", fruits[0])
print("Last two fruits:", fruits[-2:])

# 3️⃣ Adding and Removing
fruits.append("orange")
print("After append:", fruits)

fruits.remove("banana")
print("After removing banana:", fruits)

# 4️⃣ Updating an element
fruits[1] = "cherry"
print("After update:", fruits)

# 5️⃣ Looping through a list
print("\nFruits one by one:")
for fruit in fruits:
    print("-", fruit)

# 6️⃣ List Comprehension - Filtering
long_fruits = [f for f in fruits if len(f) > 5]
print("\nFruits with more than 5 letters:", long_fruits)

# 7️⃣ Transforming elements
upper_case = [f.upper() for f in fruits]
print("Fruits in uppercase:", upper_case)

# 8️⃣ Numerical Lists
numbers = [2, 5, 8, 10, 15, 20]
squares = [n**2 for n in numbers]
even_nums = [n for n in numbers if n % 2 == 0]
print("\nOriginal numbers:", numbers)
print("Squared numbers:", squares)
print("Even numbers:", even_nums)

# 9️⃣ Sorting
numbers.sort()
print("\nSorted numbers:", numbers)

# 🔟 Searching
num_to_find = 10
if num_to_find in numbers:
    print(f"{num_to_find} found in the list!")
else:
    print(f"{num_to_find} not found!")

print("\n✅ List Practice Completed Successfully!")
