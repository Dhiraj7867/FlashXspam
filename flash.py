import os
import logging
from flask import Flask
from flask_restful import Resource, Api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    api = Api(app)

    class Greeting(Resource):
        def get(self):
            logger.info("ɢʀᴇᴇᴛɪɴɢ ᴇɴᴅᴘᴏɪɴᴛ ᴡᴀꜱ ʀᴇᴀᴄʜᴇᴅ")
            return "ᴜᴘ ᴀɴᴅ ʀᴇᴀᴅʏ ꜰᴏʀ ᴅᴇꜱᴛʀᴜᴄᴛɪᴏɴ"

    api.add_resource(Greeting, '/')
    
    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"ꜱᴛᴀʀᴛɪɴɢ ꜱᴇʀᴠᴇʀ ᴏɴ ᴘᴏʀᴛ {port}")
    app.run(host="0.0.0.0", port=port)
