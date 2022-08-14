name = input("What is your name? ")
def reverse(nme):
    arr=""
    for x in nme:
        arr=x+arr     
    return arr 
print("Your name reversed is:", reverse(name))