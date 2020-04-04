from aiohttp import web
import logging
import traceback
import yaml
import sys
import os


class Server (web.Application):
    def __init__(self, config, adapter):
        self._config = config
        self._adapter = adapter
        super().__init__()

    @staticmethod
    def run(adapter):
        # Load config
        os.chdir(os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__)))
        with open('nteu_adapter_config.yml') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)

        # Create server
        server = Server(config, adapter)
        web.run_app(
            server,
            host=config["adapterServer"]["host"],
            port=config["adapterServer"]["port"]
        )
        return server

    async def translate(self, request) -> web.Response:
        try:
            data = await request.json()
            texts = data["texts"]
            translations = self._adapter.translate(
                texts,
                self._config['translationEngineServer'])
            return web.json_response({
                "translations": translations
            })

        except Exception as e:
            tb = traceback.format_exc()
            tb_str = str(tb)
            logging.error('Error: %s', tb_str)
            return web.Response(text=tb_str, status=500)

    def get_config(self):
        return self._config



