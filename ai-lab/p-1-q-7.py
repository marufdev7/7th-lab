# Experiment No: 07
# Experiment Name:
# Write a program using Python to find out Union and Intersection of two lists.
# Source Code:
list1 = [1, 2, 3, 4]
list2 = [6, 4, 5, 7]
union = list(set(list1) | set(list2))
intersection = list(set(list1) & set(list2))
print("Union =", union)
print("Intersection =", intersection)

# Output:
# Union = [1, 2, 3, 4, 5, 6, 7]
# Intersection = [4]