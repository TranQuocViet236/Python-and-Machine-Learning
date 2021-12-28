store =  (("jeans",20),("jacket",25),("sock",10),("hat",12))
Store = list(store)
to_dollar = lambda data: (data[0],data[1]*23)
dollar_store = list(map(to_dollar,store))
for i in dollar_store:
    print(i)