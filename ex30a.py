people = 20
cars = 21
trucks = 15


if cars > people:
    print(">>> first if", cars, people)
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
print("<<< exit")

if trucks > cars:
    print(">>> second if", trucks, cars)
    print("That's too many trucks.")
elif trucks < cars:
    print(">>> second if", trucks, cars)
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")
print("<<< exit")

if people > trucks:
    print(">>> third if", people, trucks)
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
print("<<< exit")
