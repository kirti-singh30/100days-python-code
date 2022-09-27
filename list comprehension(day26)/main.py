# import numbers

# numbers = [1,2,3]
# new_list = [n+1 for n in numbers]
# print(new_list)

# new_numbers = [1,2,3,4,5,6]
# new_list = [n*2 for n in range(1,5)]
# print(new_list)

# name = "kirti"
# new_name_list = [letter for letter in name]
# print(new_name_list)

# names = ["Avinash","Kirti","Anshul","Golu","Kaju","Molu"]
# new_name = [ name for name in names if len(name)< 5]
# #new_name = [ name.upper() for name in names if len(name)> 5] # want a name in upper case
# print(new_name)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)

# even_numbers = [n for n in numbers if n%2 == 0]
# print(even_numbers)
with open("list comprehension(day26)/file1.txt") as file1:
    file1_data = file1.readlines()

with open("list comprehension(day26)/file2.txt") as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file1_data if num in file2_data]
print(result)