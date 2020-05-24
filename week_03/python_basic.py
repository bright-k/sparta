num = 10
num2 = num + 5

text = "hello"

aList = []
aList.append(1)
aList.append('hello')
aList.append([1, 2])

aDict = {}
aDict["hello"] = "world"
aDict["dict"] = {"hello": "world"}
aDict["list"] = [1, 2]

def f(x):
    return 2*x+3

def sumAll(a, b, c):
    return a + b + c

def oddeven(num):
    if num % 2 == 0:
        return True
    else:
        return False

fruits = ['사과','배','감','귤']
# for fruit in fruits:
    # print(fruit)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count = 0
for fruit in fruits:
    if '배' == fruit:
        # count = count + 1
        count += 1

def countFruit(name):
    count = 0
    for fruit in fruits:
        if name == fruit:
            count += 1
    return count

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

for person in people:
    print(person['name'], person['age'])

def getAge(name):
    for person in people:
        if name == person['name']:
            return person['age']
    return "없는 이름입니다"

print(getAge('jo'))
