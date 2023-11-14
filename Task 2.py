print()
print("Out of all of these number which on of these it the biggest number")
Numbers_List = ['87', '45', '65', '97', '32', '67', '65', '45', '65', '78']
print(Numbers_List)
highest_number = Numbers_List[0]
for number in Numbers_List:
    if number > highest_number:
        highest_number = number
print("The highest number in the list is:", highest_number)