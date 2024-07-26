import sys
import glob
import asyncio
import logging
import importlib.util
import urllib3
from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def load_plugins(plugin_name):
    path = Path(f"FLASH/modules/{plugin_name}.py")
    try:
        spec = importlib.util.spec_from_file_location(f"FLASH.modules.{plugin_name}", path)
        load = importlib.util.module_from_spec(spec)
        load.logger = logging.getLogger(plugin_name)
        spec.loader.exec_module(load)
        sys.modules[f"FLASH.modules.{plugin_name}"] = load
        print(f"FLASH ʜᴀꜱ ɪᴍᴘᴏʀᴛᴇᴅ {plugin_name}")
    except Exception as e:
        print(f"ꜰᴀɪʟᴇᴅ ᴛᴏ ʟᴏᴀᴅ ᴘʟᴜɢɪɴ {plugin_name}: {e}")

files = glob.glob("FLASH/modules/*.py")
for name in files:
    patt = Path(name)
    plugin_name = patt.stem
    load_plugins(plugin_name)

print("\nʙᴏᴛ ɪꜱ ᴅᴇᴘʟᴏʏᴇᴅ ꜱᴜᴄᴄᴇꜱꜰᴜʟʟʏ")

async def main():
    await asyncio.gather(
        X1.run_until_disconnected(),
        X2.run_until_disconnected(),
        X3.run_until_disconnected(),
        X4.run_until_disconnected(),
        X5.run_until_disconnected(),
        X6.run_until_disconnected(),
        X7.run_until_disconnected(),
        X8.run_until_disconnected(),
        X9.run_until_disconnected(),
        X10.run_until_disconnected()
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
