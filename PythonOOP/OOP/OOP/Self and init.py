
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
    def log_in(self):
        self.logged = True
        return self
    def log_out(self):
        self.logged = False
        return self

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def dis_play(self):
        if self.logged == True:
            print(("User's name:  %s and User's email: %s is logged in.") % (self.name, self.email))
        else:
            print(("User's name:  %s and User's email: %s is not logged in.") % (self.name, self.email))

class My_Users(object):
    def __init__(self):
        self.Users = []
    def add(self, user):
        self.Users.append(user)
        return self
    def display_user(self):
        for user in self.Users:
           user.dis_play()

user1 = User("Anna Propas", 'anna@anna.com')
print(user1.name)
user1.logged = True
user1.dis_play()
user1.logged = False
user1.dis_play()
user2 = User("Jessica Florey", 'jflorey@florey.com')
user2.dis_play()
user2.set_name('huy ngo')
user2.logged = True
user2.dis_play()
myuser1 = My_Users()
print("---------------")
myuser1.add(user1).add(user2)
myuser1.display_user()


