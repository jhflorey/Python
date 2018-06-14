#Assignment: Bike

class Bike(object):
    def __init__(self, price, max_speed, total_miles=0):
        self.price = price
        self.max_speed = max_speed
        self.total_miles = total_miles

    def displayInfo(self):
        print ("Price :" + str(self.price), "Max_speed :" + self.max_speed +"mph", "Total Miles :" + str(self.total_miles))

    def ride(self):
        print ("Riding")
        self.total_miles += 10
        return self

    def reverse(self):
        if self.total_miles == 0:
            print("Your total miles is 0, you can't reverse")
            return self
        print ("Reversing")
        self.total_miles -= 5
        return self


bike1 = Bike(200, "20mph")
bike2 = Bike(150, "15mph")
bike3 = Bike(100, "10mph")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().ride().reverse().displayInfo()
bike3.ride().ride().ride().reverse().displayInfo()


bike1.ride().ride().reverse().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.ride().ride().reverse().reverse().displayInfo()


bike1.reverse().reverse().reverse().displayInfo()
bike2.reverse().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()



for t in range(5):
    bike1.reverse().displayInfo()
    bike2.reverse().displayInfo()
    bike3.reverse().displayInfo()


