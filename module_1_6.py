# 1st program
my_dict ={'Sergey': 1999, 'Anna': 2002, 'Victor': 1956}
print(my_dict)
print(my_dict['Sergey'])
my_dict.update({'Sasha': 2008, 'Pavel': 1998})
print(my_dict)
print(my_dict.get("Vasya"))
a = my_dict.pop("Victor")
print(my_dict)
print(a)
print("Dict:",(my_dict))
print("Existing value:", (my_dict['Sergey']))
print("Not existing value:", (a))
print("Modifield dictionary:", (my_dict))
# 2rd program
my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, "Pavel", True, (1, 2, 3)}
print(my_set)
list_ =[1, 2, 3, 4, 5, 1, 2, 3, 4, "Pavel", True, (1, 2, 3)]
list_ = set(list_)
print(list_)
print(list_.add("Bones"))
print(list_.add(6))
print(list_)
print((list_.discard(3)))
print(list_)
print("Set:", (my_set))
print("Modified set:", (list_))