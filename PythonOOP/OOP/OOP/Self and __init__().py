# Self

class User(object):
    name = "Anna"
anna = User()
print "anna's name: ", anna.name
User.name = "Bob"
print "anna's name after change:", anna.name
bob = User()
print "bob's name:", bob.name
User.name = "Jess"
print "bob's name after change:", bob.name


class User(object):
    citi = " Calli"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
user1 = User("Anna Propas", "anna@anna.com")
print user1.name
print user1.logged
print user1.email
print user1.citi
User.citi = "hcm"
user2 = User("Jessica Florey", "jessica@florey.com")
print user2.name
print user2.logged
print user2.email
print user1.email
print user2.citi
