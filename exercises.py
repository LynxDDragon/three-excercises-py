#EXERCISE 1
#Cube Number Test... Print  out all cubed numbers up to the value 1000.
#Meaning that if the cubed number is over 1000 breack the loop.

for num in range(1, 100):
    out = num ** 2
    if out < 1000:
        print(out)

#EXERCISE 2
#Get first prime numbers up to 100

#Definition of and Prime number is a number that is only divided by itself, and has no remainders
for numbs in range(1, 101):
    #"count" is the switch
    count= 0
    # checks if the number is not evenly divisable by any other number other than itself
    # Also checks if it has remainders by dividing it by 2 and floor dividing itself +1
    for i in range (2, (numbs//2+1)):
        #modulo by 2 and (numbs//2+1) and if the remaider is 0 do the next step
        if(numbs % i == 0):
            #change the switch to go to the other if statement
            count = count + 1
            break
    #if the "count" switch is equal to 0 and the number is not equal to 1, go to the next step
    if (count == 0 and numbs != 1):
        print(numbs, end= ' ')


#EXERCISE 3
#Take in a users input for their age, if they are younger than 18 print
#kids, if they're 18 to 65 print adults, else print seniors.

age = int(input("How old are you?"))

if age < 18:
    print("You're children. Y'all should go to Weenie Hut Jr's ")
if 65 >= age >= 18:
    print("Welcome to the Salty Spitoon, how tough are ya?")

if age > 100:
    print("You are sadly not allowed to play with Legos, It is against the Laws of the Universe")
if age > 200:
    print('You should literally be dead right now, stop saying "BRAINS".' )