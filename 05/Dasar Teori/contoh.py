file = open('myfile.txt', 'w')
file.write("This will create a new file")
file.close()

with open("myfile.txt", "r") as file:
    print(file.read())
