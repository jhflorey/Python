# class Structure

class User(object):
    #the init method is called everytime a new object is created
    def __init__(self, name, email):
        # set some instance variable, just like any variable we can call these anything
        self.name = name
        self.email = email
        self.logged = True
    # this is a method we created a help a user login
    def login(self):
        self.logged = True
        print self.name + " is logged in. "
        return self
    def logout(self):
        self.logged = False
        print self.name + " is not logged in."
        return self
    def show(self):
        print "My name is {}. You can emaill me at {}".format(self.name, self.email)
        return self
# now create on instance of the class
new_user = User("Anna", "anna@anna.com")
print(new_user.email)
print(new_user.name)
new_user.show()
new_user.login()
new_user.logout()






