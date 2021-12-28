usernames = ("Viet", "Hai", "Duy", "Linh")
passwords = ("p@ssword", "guest", "elements", "kkhihi")
login_date = ("1","2","3","4")

Users = zip(usernames,passwords,login_date)

for i in Users:
    print(i)

print(__name__)