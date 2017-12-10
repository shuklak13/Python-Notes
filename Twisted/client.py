from twisted.internet.protocol import Protocol

class WelcomeProtocol(Protocol):
    def connectionMade(self):
        self.transport.write("Hello server, I am the client!\r\n")
        self.transport.loseConnection()


from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol

class GreetProtocol(Protocol):
    def sendMessage(self, msg):
        self.transport.write("MESSAGE %s\n" % msg)

def gotProtocol(p):
    p.sendMessage("Hello")
    reactor.callLater(1, p.sendMessage, "This is sent in a second")
    reactor.callLater(2, p.transport.loseConnection)

# the TCP4ClientEndpoint has to give both an IP Address and a Port Number
e_point = TCP4ClientEndpoint(reactor, "localhost", 1234)
d = connectProtocol(e_point, Greeter())   # establish a new connection (given an endpoint)
d.addCallback(gotProtocol)
reactor.run()


# ClientFactory can be useful to reconnect in case of connection error
from twisted.internet.protocol import ClientFactory
from sys import stdout

class EchoProtocol(Protocol):
    def dataReceived(self, data):
        stdout.write(data)

class EchoClientFactory(ClientFactory):
    def startedConnecting(self, connector):
        print('Started to connect.')

    def buildProtocol(self, addr):  # called once connection is established
        print('Connected.')
        return EchoProtocol()

    def clientConnectionLost(self, connector, reason):
        print('Lost connection.  Reason:', reason)
        print('Reattempting connection')
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)


# ReconnectingClientFactory is better for this purpose
from twisted.internet.protocol import ReconnectingClientFactory
class EchoClientFactory(ReconnectingClientFactory):
    def buildProtocol(self, addr):
        print('Connected.')
        print('Resetting reconnection delay')
        self.resetDelay()
        return Echo()

    # call the parent function to attempt reconnect
    def clientConnectionLost(self, connector, reason):
        print('Lost connection.  Reason:', reason)
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)
        ReconnectingClientFactory.clientConnectionFailed(self, connector,
                                                         reason)