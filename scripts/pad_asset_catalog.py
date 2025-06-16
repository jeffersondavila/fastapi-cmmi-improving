#!/usr/bin/env python
"""
pad_asset_catalog.py  –  Área: PROCESS ASSET DEVELOPMENT (PAD)
Propósito : Genera assets_catalog.json listando scripts y docs.
Uso       : python scripts/pad_asset_catalog.py
"""
import json, pathlib, time
root = pathlib.Path(__file__).resolve().parent.parent
assets = [
    {"name": p.name,
     "path": str(p.relative_to(root)),
     "mtime": time.strftime("%Y-%m-%d", time.localtime(p.stat().st_mtime)),
     "owner": "jefferson"}
    for p in root.glob("scripts/*")
]
catalog = root / "assets_catalog.json"
catalog.write_text(json.dumps(assets, indent=2))
print(f"✅ Catálogo generado en {catalog}")
