


# Find the shortest distance
# points = [
#     (12, 55),
#     (880, 123),
#     (64, 64),
#     (190, 1024),
#     (77, 33),
#     (42, 11),
#     (0, 90),
#     (45,47),
#     (1,1)
# ]
# distanse = list(range(len(points)))
# z=0
# for (x,y) in points:
#     distanse[z] = math.sqrt((x**2)+(y**2))
#     z+=1
# print(min(distanse))

# Find avarage prices
# prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]
# avg = sum(prices)/len(prices)
# new_list=[]
# for x in prices:
#     if x >= avg:
#         new_list.append(x)
# print(len(new_list))
# print(new_list)
# print(prices)
# prices.sort()

# Count the lengths of the word
# list = input()
# new_list = list.split()
# average = sum(len(word) for word in new_list)/len(new_list)
# print(average)


# ages = { 'Dave' : 24, 'Anna' : 15, 'Bob' : 20,'Kate':34}
# print(ages['Dave'])
# print(ages['Anna'])
# # print('Dave' in ages)
# # print('Kate' not in ages)
# # print('Margaret' in  ages)
# print(ages.get('Dave'))
# print(ages.get('Margaret', 'Anna'))
# print(len(ages))

#Work with dictionaries
# contacts = {
#     'David' : ['123-321-88','david@test.com'],
#     'James' : ['234-789-33','james@test.com'],
#     "Bob": ["987-004-322", "bob@test.com"],
#     "Amy": ["340-999-213", "a@test.com"]
# }
# name = input()
# if name in contacts:
#     print(contacts[name][1])
# else:
#     print('Not found')
# print(contacts['David'])
# print(contacts.get('David'[0]))
# dict = {
#     ('David',24) : 'red',
#     ('Bob', 48) : 'blue'
# }
# print(dict.get(('David',24)))


#Unpacking tuples
# numbers = (1,2,3,5)
# a,b,c,d = numbers
# a,b,c,d= d,c,a,b
# print(a,b,c,d)
# print(a)
# print(b)
# print(c)
# print(d)

# a,b,*c,d = (1,2,3,4,5,6,7,8,9)  # asterics stands for getting all values which left after unpacking previous values
# print(a)
# print(b)
# print(c)
# print(d)
# import math


# first = {1, 2, 3, 4, 5, 6}
# second = {4, 5, 6, 7, 8, 9}
#
# print(first | second)
# print(first & second)
# print(first - second)
# print(second - first)
# print(first ^ second)

# text = 'this is text'
# text2 = 'this is text in word '
# text = 'this are my favorite'
# text2 = 'favorite part of the programm'
# list1 = text.split()
# list2 = text2.split()
# print(list1)
# print(list2)
# print(set(list1))
# print(set(list2))

# print(len(set(list1) & set(list2)))

# print(text.split())
# print(set(text))
# print(len(text.split()))

# s1 = input()
# s2 = input()
# print(len(set(s1).split() & set(s2).split()))


# data = {
#     "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71,
#     "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64,
#     "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27,
#     "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65,
#     "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27,
#     "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12,
#     "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
# }
#
# #print(data.values())
#
# age = int(input())
# profit = 0
# for value in data.values():
#     if value >=18:
#         profit +=20
#     else:
#         profit +=5
# #print(profit)
#
#
# profit2 = 0
# for value in data.values():
#     if value >=age:
#         profit2 +=20
#     else:
#         profit2 +=5
# #print(profit2)
# print(int(((profit2-profit)/profit)*100))