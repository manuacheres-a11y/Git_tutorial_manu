my_list=["a","b","c","d","e"]
print(my_list[0])
print(my_list[2])
my_list[1] = "youpi"
print(my_list[1])
my_list.append(26)
print(my_list)
divers = my_list.copy
print(divers)
my_list.append("a")
print(my_list)
print(my_list.count("a"))
my_list.extend([2,"bug","coucou",True])
print(my_list)
my_list.pop(5)
print(my_list)
word = "HELLO"
#print(word.lower())
print(word.upper())
word = word.lower()
print(word)
word = word.capitalize()
print(word)
