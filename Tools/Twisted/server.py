# Servers
#   twisted.internet.protocol.Factory - persistent info; creates Protocols
#   twisted.internet.protocol.Protocol - represent connections; this is where the majority of the code is

from twisted.internet.protocol import Protocol

# server that echoes data sent to it
class EchoProtocol(Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


# upon making a connection, sends a fixed message
class QuoteOfTheDay(Protocol):
    def connectionMade(self):
        self.transport.write("An apple a day keeps the doctor away\r\n")
        self.transport.loseConnection()


class CounterProtocol(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write(
            "Welcome! There are currently %d open connections.\n" %
            (self.factory.numProtocols,))

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1


from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint

class QuoteOfTheDayFactory(Factory):
    def buildProtocol(self, addr):
        return QuoteOfTheDay()

# We create a service, QuoteOfTheDayFactory,
# that can create multiple connections fpr the QuoteOfTheDay protocol
qotd = QuoteOfTheDayFactory()

# The reactor is the event loop
    # it waits for event to arrive, then dispatches the relevant event handler.
# There is always exactly one reactor in any Twisted application.
from twisted.internet import reactor

# The QuoteOfTheDayFactory service can be attached to multiple ports
endpoint8007 = TCP4ServerEndpoint(reactor, 8007); endpoint8007.listen(quotd)
endpoint8008 = TCP4ServerEndpoint(reactor, 8008); endpoint8008.listen(quotd)
reactor.run()


# LineReceiver allows protocols to read in data by line
from twisted.protocols.basic import LineReceiver
class LoggingProtocol(LineReceiver):
    def lineReceived(self, line):
        self.factory.fp.write(line + '\n')

# startFactory(), stopFactory()
class LogfileFactory(Factory):
    protocol = LoggingProtocol
    def __init__(self, fileName):
        self.file = fileName

    def startFactory(self):
        self.fp = open(self.file, 'a')

    def stopFactory(self):
        self.fp.close()


# Good comprehensive example
class ChatProtocol(LineReceiver):
    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = "GETNAME"  # this Protocol is a State Machine

    def connectionMade(self):
        self.sendLine("What's your name?")

    def connectionLost(self, reason):
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):   # event handler function
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            self.handle_CHAT(line)

    def handle_GETNAME(self, name):
        if name in self.users:
            self.sendLine("Name taken, please choose another.")
            return
        self.sendLine("Welcome, %s!" % (name,))
        self.name = name
        self.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):
        message = "<%s> %s" % (self.name, message)
        for name, protocol in self.users.iteritems():
            if protocol != self:
                protocol.sendLine(message)

class ChatFactory(Factory):
    def __init__(self):
        self.users = {} # maps user names to Chat instances

    def buildProtocol(self, addr):
        return ChatProtocol(self.users)

# reactor.listenTCP() is a lower-level function that TCP4ServerEndpoint wraps
    # they can be used in equivalent situations
reactor.listenTCP(8123, ChatFactory())
reactor.run()