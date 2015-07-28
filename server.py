import msgpack
from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory


class WSP(WebSocketServerProtocol):
    def onConnect(self, request):
        self._count = 0

    def onOpen(self):
        payload = msgpack.packb([1, 2, 3])
        self.sendMessage(payload, True)

    def onMessage(self, payload, isBinary):
        assert isBinary

        if self._count < 10:
            self._count += 1
        else:
            return
        payload = msgpack.unpackb(payload)
        print payload
        payload = map(lambda x: x + 1, payload)
        payload = msgpack.packb(payload)
        reactor.callLater(1, lambda: self.sendMessage(payload, True))


class WSF(WebSocketServerFactory):
    protocol = WSP



reactor.listenTCP(8000, Site(File('www')))
reactor.listenTCP(8888, WSF())
reactor.run()

