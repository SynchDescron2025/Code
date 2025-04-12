#Reverse the order of items in a list
my_list = [1,2,3,4,5]
new_list = []
length = len(my_list)
while length >= 1:
    new_list.append(my_list[length-1])
    length -= 1
print(new_list)