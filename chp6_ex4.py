# TODO change the string "Where now? Who now? When now?" using a method that
#returns the list separated by the question marks

string_one = "Where now? Who now? When now?"

list_one = string_one.split("?")
list_two = [i+"?" for i in list_one]
list_two.pop()
print(list_one)
print(list_two)
