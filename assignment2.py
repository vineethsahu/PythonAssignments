name = str(input("Enter the filename :"))
x = name.split(".")
if x[1] == 'py':
    print("The extension of the file is : 'Python'")
else:
    print("Invalid filename")
