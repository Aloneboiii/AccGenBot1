import glob
from pathlib import Path
from AccGenBot.utils import load_plugins
import logging
from AccGenBot import BotzCity

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "AccGenBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("AccsGenBot is now alive")
print("Send /start and party 🥳🥳")

if __name__ == "__main__":
    BotzCity.run_until_disconnected()
