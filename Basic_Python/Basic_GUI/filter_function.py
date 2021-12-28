friends = [("Viet", 20),
           ("Hai", 16),
           ("Duy", 21),
           ("Linh", 17)]

age = lambda data : data[1]>=18
drink_buddies = list(filter(age, friends))
for i in drink_buddies:
    print(i)