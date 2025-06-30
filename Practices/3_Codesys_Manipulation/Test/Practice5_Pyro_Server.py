import Pyro4

@Pyro4.expose
class Greeting(object):
    def hello(self, name):
        return "Hello " + name

daemon = Pyro4.Daemon()
uri = daemon.register(Greeting)
print("Ready. URI =", uri)
daemon.requestLoop()
