#Question 1
for fizzbuzz in range(50):
	 if fizzbuzz % 15 == 0:
		 print("FizzBuzz")
		 continue
	 elif fizzbuzz % 3 == 0:
		 print("Fizz")
		 continue
	 elif fizzbuzz % 5 == 0:
		 print("Buzz")
		 continue
	 print(fizzbuzz)

#question 2:
quote = "I'm learing Python"

def replace_string(quote):
    new_string = quote
    for i in range(0, len(quote)):
        if ord(quote[i]) != 32:
            new_string = new_string.replace(quote[i], '_ ')
    print(new_string)
replace_string(quote)

#question 3:
def anagram(s1,s2):
    if(sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
s1 ="dad"
s2 ="mom"
anagram(s1, s2)

#question 4:
list1 = [2,4,6,8,10]
print("Original list is : " + str(list1))
newlist1 = list1[1:4]
print("new list is :" +str(newlist1))

#question 5:
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
print("Index and Values: ")
print ([list((i, list1[i])) for i in range(len(list1))])

#question 6:
dictA = {'A': 55, 'B': 12, 'C': 454, 'E': 78, 'F': 89, 'G': 56, 'H': 55}
print ("Original dictionary is : ")
print(dictA)

print()
new_dictA = {}
for key, value in dictA.items():
   if value in new_dictA:
       new_dictA[value].append(key)
   else:
       new_dictA[value]=[key]

print ("Dictionary after reversed is :  ")
print("keys: values")
for i in new_dictA:
    print(i, " :", new_dictA[i])

# question 7:

def FibonacciNumbers(n):
    f1 = 0
    f2 = 1
    if (n < 1):
        return
    print(f1, end=" ")
    for x in range(1, n):
        print(f2, end=" ")
        next = f1 + f2
        f1 = f2
        f2 = next
FibonacciNumbers(15)



