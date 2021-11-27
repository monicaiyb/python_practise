cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")
# for loop to use the range function
for i in range(3):
    print("Hello!")

# for loops can be used to modify lists
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
    print(capitalized_cities)

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    names=name.replace(" ", "_")
    usernames=names.lower()
    print(usernames)
    
    

print(usernames)