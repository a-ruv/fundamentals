#1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#a
x[1][0] = 15
print(x)

#b
students[0]["last_name"] = "Bryant"
print(students[0])

#c
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

#d
z[0]['y'] = 30
print(z)

#2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(array): 
    for i in range(len(array)):
        print(f"first_name - {array[i]['first_name']} last_name - {array[i]['last_name']}")
iterateDictionary(students)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#3
def iterateDictionary2(key, array):
    for i in range(len(array)):
        print(array[i].pop(key))
iterateDictionary2("first_name",students)
iterateDictionary2("last_name",students)

#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    print('*********************************************************************')
    print(f"{len(some_dict['locations'])} {'locations'.upper()}")
    for i in range(len(some_dict['locations'])):
        print(some_dict['locations'][i])
    print('*********************************************************************')
    print(f"{len(some_dict['instructors'])} {'instructors'.upper()}")
    for i in range(len(some_dict['instructors'])):
        print(some_dict['instructors'][i])
    print('*********************************************************************')
printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon





