
'''12.	Remove an element from a set using remove() and discard().
•	Try removing an element that doesn’t exist using both.'''
demo_set = {10, 20, 30, 40, 50, 60, 70}
print("\nSet before removing a element :", demo_set)
demo_set.remove(20)
demo_set.discard(50)
print("Set after removing a element :", demo_set)


#Trying removing an element that doesn’t exist using both

#demo_set.remove(50) #It will show an error. KeyError: 50

demo_set.discard(20) #Removing an element which does not exist in the set using discard()
                     #It does not show any error