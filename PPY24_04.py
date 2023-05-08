import LinkedList
import Stack
import Student

myList = LinkedList.LinkedList()

myList.add_node("bbbbb")
myList.add_node("aaaa")
myList.add_node("cccc")

print("Lista po dodaniu elementów:")
print(myList)

myList.delete("aaaa")

print("Lista po usunięciu elementów:")
print(myList)


myStudentList = LinkedList.LinkedList()


filepath = "students0.txt"

with open(filepath) as file_object:
    for line in file_object:
        x = line.rstrip().split(",")
        
       

