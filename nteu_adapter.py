from nteu_adapter.server import Server
from nteu_adapter.adapter_base import AdapterBase


class FakeAdapter(AdapterBase):
    def translate(self, texts, config):
        return


server = Server.run(FakeAdapter)
