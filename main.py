
# for flask
# if __name__ == "__main__":
#     app.run(debug=True)

celsius = 0
kelvin = 0
print("Enter the temperatures:")

celsius=input("In celsius: ")
print(int(celsius) +273.15)

kelvin=input("In kelvin: ")
print(int(kelvin) +273.15)

farenheit=input("In farenheit: ")
print(int(farenheit)*(1.8)+32)


grade = int (input("Enter your grade: "))
if (grade<0 or grade>100):
    print ("Invalid")
elif (grade>=96 and grade <=100):
    print ("Your equivalent grade is 4")
elif (grade>=90 and grade <=95):
    print ("Your equivalent grade is 3.5")

num=int(input("Enter Number: "))
if (num%2==0):
    # print (str(num) + " is even")
    print(f"{num} is even")
else:
    print (str(num) + " is odd")

n=10
i=int(input("Type the number: "))
for x in range (n):
    print (i*(x+1))

i=10
for x in range (i):
    if x==6:
        break
    print(int (x))
