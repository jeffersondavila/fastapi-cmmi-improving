#!/usr/bin/env bash
# -------------------------------------------------------------
# gov_check_compliance.sh  –  Área: GOVERNANCE (CMMI-DEV)
# Propósito : Ejecuta Bandit y falla si hay Medium/High findings.
# Uso       : bash scripts/gov_check_compliance.sh
# Variable  : BANDIT_TARGET (directorio a escanear, default "src")
# -------------------------------------------------------------
set -e
TARGET=${BANDIT_TARGET:-src}
bandit -r "$TARGET" -ll -o bandit.txt -f txt
if grep -Eq "Severity: (Medium|High)" bandit.txt; then
  echo "❌ GOV policy violated (Medium/High findings)."
  exit 1
fi
echo "✅ GOV policy met (no Medium/High findings)."
