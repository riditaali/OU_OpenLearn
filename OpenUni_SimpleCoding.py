
"""
#https://www.open.edu/openlearn/science-maths-technology/simple-coding/content-section-7
"""

#SELECTION

# scenario

bill = 100
tip = 0.1*bill

total = bill + tip

bill2 = 100

#Activity 3

people = 6

if people <= 6:
  tip_act = 0
else:
  tip_act = 0.1 * bill2

total_for_activity = bill2 + tip_act

#Activity 4

#first group

people = 3

if people > 6:
  tip2 = 0.1 * bill2
else:
  tip2 = 0

total2 = bill2 + tip2

#Activity 5

#third scenario - Activity 6

bill3 = 50    
    
people = int(input("Enter the number of people in the group: "))  #specifying no of people should be integers 

if people <= 6:
    tip3 = 0
elif people > 6 and people < 15:    
    tip3 = 0.1 * bill3
else:
    tip3 = 0.15 * bill3
    
total3 = bill3 + tip3
total3

#Iteration - Activity 7

#items
items = [2, 4, 5.3, 1, 7.5]

#expenses
expenses = 0

#print total price of all the items
for i in items:
    expenses = expenses + i
print('Total = ', expenses)

#if 'print' is typed with a tab, just below expenses then it will print total price item by item

#Functions - Activity 8

expenses = 54
people = int(input('The number of people: '))
if people >= 15:
    percentage = 0.15
elif people > 6:
    percentage = 0.10
else:
    percentage = 0
tip = expenses * percentage
bill = expenses + tip
print("Total bill:", bill)

#Iteration (part 2) - Activity 9

expenses = 50
while True:
    customers = input("The number of customers: ")
    if customers == "stop":
        break
    else:
        customers = int(customers)
        if customers >= 15:
            percentage = 0.15
        elif customers > 6 and people < 15:
            percentage = 0.10
        else:
            percentage = 0
        tip = expenses * percentage
        bill = expenses + tip
        bill = bill + (0.2*expenses)
print("Total bill:", bill)

#Activity 10

# Euclid's greatest common divisor algorithm

#https://www.freecodecamp.org/news/euclidian-gcd-algorithm-greatest-common-divisor/

"""
a = 5
b = 7

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, (a % b))
"""

# ask user for an integer greater than zero

asking_integer1 = int(input("Enter an integer greater than zero (0): "))

# store it in n

n = asking_integer1

# ask user for an integer greater than zero

asking_integer2 = int(input("Enter an integer greater than zero (0): "))

# store it in m

m = asking_integer2

# while n and m are different: 
while n != m:
    if n > m:
      n = n - m
    else:
      m = m - n
print("Their greatest common divisor is", n)



