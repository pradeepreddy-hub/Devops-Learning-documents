mylist = [10, 19, 21, 80, 22, 47, 50, 70]

print("\n")

sum_of_elements = 0
for num in mylist:
    sum_of_elements += num
print("Sum of all elements:", sum_of_elements)

print("\n")

even_numbers = []
for num in mylist:
    if num % 2 == 0:
        even_numbers.append(num)
print("Even Numbers:", even_numbers)

print("\n")
