print('Enter elements in a list')

l = [int(elements) for elements in input().split(",")]
print("The list is: ", l)

new_l = []
for elements in l:
    if elements>0:
        new_l.append(elements)
        print(elements, end=",")

print("The new list is: ", new_l)
