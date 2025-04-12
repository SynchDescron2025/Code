#Find the maximum element in a list
my_list = [1, 5, 2, 9, 3]
min = my_list[0]
for i in my_list:
    if i >= min:
        min = i
print("Maximum element in this list is " + str(min))