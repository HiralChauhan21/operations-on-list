lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("length of list: ", len(lst))
print("first element: ", lst[0])
print("Last element: ", lst[-1])

lst.append('papaya')
print("Updated List: ",lst)

lst.remove('Guava')
print("updated list: ", lst)

lst.sort()
print("sorted list: ", lst)

lst.pop(1)
print("updated list: ",lst)

lst.reverse()
print("revrsed list: ", lst)

print("Multiplication on list: ", lst*2)

lst = lst[:4]
print("Sliced List: ", lst)

lst.clear()
print("updated list: ", lst)

