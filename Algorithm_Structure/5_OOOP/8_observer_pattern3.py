class SubscriberOne(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{0} {1}".format(self.name, message))

class SubscriberTwo(object):
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print("{0} {1}".format(self.name, message))

class Publisher(object):
    def __init__(self):
        self.lunch = Event()
        self.dinner = Event()

class Event():
    def __init__(self):
        self.subscribers = set()

    def register(self, callback):
        self.subscribers.add(callback)

    def unregister(self, callback):
        self.subscribers.discard(callback)

    def dispatch(self, message):
        for callback in self.subscribers:
            callback(message)

if __name__ == "__main__":
    pub = Publisher()

    astin = SubscriberOne("Astin")
    james = SubscriberOne("James")
    jeff = SubscriberTwo("Jeff")

    pub.lunch.register(astin.update)
    pub.lunch.register(james.update)
    pub.dinner.register(jeff.receive)

    pub.lunch.dispatch("It's lunch time")
    pub.lunch.unregister(james.update)
    pub.lunch.dispatch("Finished")

    pub.dinner.dispatch("It's lunch time")
    pub.dinner.unregister(jeff.receive)
    pub.dinner.dispatch("Finished")