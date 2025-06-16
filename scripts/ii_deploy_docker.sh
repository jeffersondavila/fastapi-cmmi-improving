#!/usr/bin/env bash
# ii_deploy_docker.sh  –  Área: IMPLEMENTATION INFRASTRUCTURE
# Propósito : Levantar la pila FastAPI + Redis + Postgres vía docker-compose.
# Uso       : bash scripts/ii_deploy_docker.sh [dev|prod]   (default dev)
# Variables : STACK_TAG (etiqueta opcional para los contenedores)
set -e
ENV=${1:-dev}
COMPOSE=infra.yml
echo "🚀 Deploy stack ($ENV)…"
docker-compose -f "$COMPOSE" --env-file ".env.$ENV" up -d
echo "✅ Stack ($ENV) desplegado."
