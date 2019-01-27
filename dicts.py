name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dibert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid,
"there")

greeting(382)

greeting(3333333)
