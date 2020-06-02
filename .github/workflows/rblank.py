names = ["Jim", "Sam", "Munene", "Joker"]
print(names)
numbers = [1, 4, 5, 6, 1, 7,]
print(numbers)
names.extend(numbers)
print(names)
names.append("Sarah")
names.insert(2, "Maina")

print(names.index("Maina"))

friends = names.copy()
print(friends)

my_name = [("Maina", "Samuel"), (1, 6), (8, 5), (0, 6)]
print(my_name [1][1])

def mine():
    print("What is your name?")
    your_name = input("Type in your name here: ")
    print("Hello " + your_name)
mine()

def jina(mane, years):
    print("Hello " + mane + " you are " + str(years) + " years old")

jina("Jonas", 67)
