
x = 50
a = 2
b = 3
age = 18
password = "python1123"

def firstProblem():
    if x%2==0:
        print("Число парне")
    else:
        print("Число непарне")

def secondProblem():
    if x == 0:
        print("equals zero")
    if x > 0:
        print("more than 0")
    if x<0:
        print("less than 0")
  
def thirdProblem():
    if age>=18:
        print("Confirmed")
    if age<18:
        print("Denied")

def fourthProblem():
    if x <= 10 & x>= 1:
        print("The right number")
    else:
        print("No it's not")

def fifthProblem():
    if password == "python123":
        print("Password is correct")
    else:
        print("Password isn't correct")

def sixthProblem():
    if a > b:
        print(a)
    else:
        print(b)


def seventhProblem():
    if x >= 90:
        print("excelent")
        return
    if x >= 70:
        print("good")
        return
    if x >= 50:
        print("OK")
        return
    if x < 50:
        print("Bad")
        return

#list = ["Nigga","Gooner",67]

#print(list)


#set = {"Nigga",67,"Mustard"}
#set.add(67)
#print(set)



for i in range(5):
    print(i+1)

while x != 0:
    print("NIIIIGGGGAAAAAAA")
    break


