#!/usr/bin/env python
"""
mpm_kpi_tracker.py  –  Área: MANAGING PERFORMANCE & MEASUREMENT (MPM)
Propósito : Extrae % de cobertura de coverage.xml y lo guarda en kpi_history.csv
Uso       : python scripts/mpm_kpi_tracker.py coverage.xml
"""
import csv, datetime, pathlib, sys, re
cov_xml = pathlib.Path(sys.argv[1])
pct = 0.0
for line in cov_xml.read_text().splitlines():
    m = re.search(r'line-rate="([\d.]+)"', line)
    if m:
        pct = round(float(m.group(1)) * 100, 2)
        break
hist = pathlib.Path("kpi_history.csv")
with hist.open("a", newline="") as f:
    csv.writer(f).writerow([datetime.date.today().isoformat(), pct])
print(f"✅ KPI registrado: cobertura {pct}%")
