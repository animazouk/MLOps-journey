print("\n")
# Lists---->
friends = ["adarsh","divyansh","Deepak"]
jobs = ["painter","labour","contractor"]
print(friends)
print(jobs)
print("\n")
    #Indexing & slicing
print(friends[0])  # fetches the first value
friends[1] = "Divyanshi"
print(friends[-1]) #fetches the last value
print(friends[0:])#this will return all elements from 1 till end
print(friends[0:2])# this says fetch include elements on index 1,2 which can be said to till 3(excluding 3).

print("\n")
    #List functions
friends.extend(jobs);print(friends) #concatinates job at the end of friends list
friends.append("ADHYA");print(friends)  #adds the passed elements at the end of the list 
friends.insert(2,"Luv");print(friends)  # enters at a perticular position in the list
friends.remove("ADHYA");print(friends)  #passes elemnet gets removed from the list
friends.index("Deepak");print(friends)  #retuens the postion of the passed elements first occurance in the list.
friends.count("ADHYA");print(friends)  # counts the number of tiume the oassed elemnt has ben occured
friends.sort();print(friends) #sorts elements of a list 
friends.reverse();print(friends)  # revers the elements of the list
f1 = friends.copy();print(friends)  # copies the content of the list to another one 
friends.pop();print(friends)  # just removes the last element from the list 
# friends.clear();print(friends)  # clear the list completly [makes it empty]


print("\n")
#TUPLES------->

coordinate = (4,5) # tuples are immutable every change actually returns a copy without effecting the actual tupple
print()

# List of Tuples
coordinates = [(4,5),(6,4),(-3,6)]
print(coordinates[0]) # prints the first tuple
print(coordinates[0][1]) # prints the second element of the first tuple

print("\n")
#Functions------>
def sayhi(name):
    print("hello "+ name)

print("top")
sayhi("Adarsh")
print("bottom")

def cube(num):
    return num*num*num

result = cube(3)
print(result)

#if/else/elif/nested elif---->
is_male = True
is_tall = True

if is_male or is_tall:
    if is_male and is_tall:
        print("tall male")
    elif is_male and not(is_tall):
        print("male but not tall")
    else:
        print("not male probably not tall")

#if statements using comparisons--->

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>=num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(1,2,3))

#Dictionaries ------->
 
month_conversion = {
   "Jan":"January",
    "Feb":"February",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
 }

print(month_conversion.get("Feb","Not a valid key")) 
''' the second argument is a default argument 
passed so the if the key dont exists 
in the dictionary the defult value gets 
return and the program keep s running 
without any errors. '''

# While loop

i = 1
while i <= 10:
    print(i)
    i += 1

#For loop -------->

for letter in "Air Force School":
    print(letter)

for friend in friends:
    print(friend)

for x in range(3,10):
    print(x)

#Exponent Function

def raistopower(base,power):
    result = 1
    for index in range(power):
        result = result * base
    return result

a = raistopower(2,3)
print(a)


