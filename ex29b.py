people = 20
cats = 30
dogs = 15


if people < cats:
    print(">>first if", people, cats)
    print("Too many cats!  The world is doomed!")
    print("<< exit", people, cats)

if people > cats:
    print(">>second if", people, cats)
    print("Not many cats!  The world is saved!")
    print("<< exit", peopel, cats)

if people < dogs:
    print(">>>third if", people, dogs)
    print("The world is drooled on!")
    print("<< exit")

if people > dogs:
    print(">> forth if", people, dogs)
    print("The world is dry!")
    print("<< exit")

dogs += 5

if people >= dogs:
    print(">> if dogs number one", people, dogs)
    print("People are greater than or equal to dogs.")
    print("<< exit")

if people <= dogs:
    print(">> if dogg numbe two", people, dogs)
    print("People are less than or equal to dogs.")
    print("<< exit")

if people == dogs:
    print(">>last if statment", people, dogs)
    print("People are dogs.")
    print("<<< exit")
