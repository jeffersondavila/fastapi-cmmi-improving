#!/usr/bin/env python
"""
pcm_gate_pipeline.py  –  Área: PROCESS MANAGEMENT (PCM)
Propósito : Falla el pipeline si CHANGELOG.md no existe.
Uso       : python scripts/pcm_gate_pipeline.py
"""
import pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
changelog = root / "CHANGELOG.md"
if not changelog.exists():
    print("❌ PCM gate: falta CHANGELOG.md")
    sys.exit(1)
print("✅ PCM gate: CHANGELOG.md presente")
