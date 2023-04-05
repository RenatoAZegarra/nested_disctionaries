# 1.)
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

x[1][0]=15
print(x)

students[0]['last_name'] = "Bryant"
print(students)

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z[0]['y'] = 30
print(z)

# 2.)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(key, "-", value)
iterate_dictionary(students)

# 3.)
def iterate_dictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])
iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)

# 4.)
dojo = {
   'locations':['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(dojo):
    for key in dojo:
        print(len (dojo[key]))
        for item in dojo[key]:
            print(item)
        print("----------")
print_info(dojo)

