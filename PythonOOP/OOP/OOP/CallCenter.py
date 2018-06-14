class Call(object):
    def __init__(self, id, name, phone, time, reason):
        self.id = id
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
    def display(self):
        print(("%s with ID %s has phone number: %s call in center at the time: %s for reason: %s")%(self.name, self.id, self.phone, self.time, self.reason))

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
    def add(self, new_call):
        self.calls.append(new_call)
        self.queue_size += 1
        return self
    def remove(self):
        if self.queue_size >= 1:
            del(self.calls[0])
            self.queue_size -= 1
        else:
            print("We have no call to remove")
    def display_info(self):
        for call in self.calls:
            call.display()
        print(self.queue_size)

call1 = Call(1, "Jessica", 4154136968, "12:30 PM", "I need to talk")
call2 = Call(2, "Jennifer", 4154830000, "2:00 PM", "I don't want to talk")
call3 = Call(3, "Jeff", 4154007000, "10:30 AM", "Do u have anyone answer my phone")
a_center = CallCenter()
a_center.add(call1).add(call2).add(call3)
a_center.display_info()
print("------------")
a_center.remove()
a_center.display_info()