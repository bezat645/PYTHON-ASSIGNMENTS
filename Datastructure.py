my_list = []
list = [50,60,70]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(2,15)  # Insert 25 at index 2

my_list.extend(list)  # Extend my_list with elements from list
my_list.pop()
my_list.sort()
print(my_list.index(30))  # Find the index of 30