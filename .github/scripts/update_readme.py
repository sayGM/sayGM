import json
import re
import urllib.request
from datetime import datetime, timezone

URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

with urllib.request.urlopen(URL, timeout=20) as r:
    data = json.load(r)

btc = data["bitcoin"]["usd"]
eth = data["ethereum"]["usd"]
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

block = (
    "<!-- MARKER_START -->\n\n"
    f"**BTC** ${btc:,.0f} · **ETH** ${eth:,.0f}\n\n"
    f"<sub>Updated {now}</sub>\n\n"
    "<!-- MARKER_END -->"
)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"<!-- MARKET:START -->.*?<!-- MARKET:END -->",
    block,
    content,
    flags=re.DOTALL,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
