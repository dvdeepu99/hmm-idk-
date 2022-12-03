#this is a test
name = 'Koyla'
age = 55

print("Hi {0}, your age is {1}. Good Morning.".format(name, age))
print(f'Hi {name}, your age is {age}, Good Morning.')
print("Hi " + name + ", your age is " + str(age) + ", Good Morning.")
print("He said \"Hello, <your name>, your age is <age>, Good Morning\"")
year = int(input("What year were you born?"))
age = 2022 - year
print("Your age is " + str(age) + " Years")

pwd = input("Enter your password")
lth = len(pwd)
print(lth)
print(type(lth))

i = 1
pswd = ''
for i in pwd:
  pswd = (str(pswd) + '*')
print(type(pswd))
print(f"Your password {pswd} has a length of {lth} characters")