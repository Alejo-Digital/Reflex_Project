#!/bin/bash

# Script de construcción para despliegue en Vercel
set -e # Detener el script si ocurre algún error

echo "--- Instalando uv si no está presente ---"
# Ya sabemos que uv está en el PATH de Vercel por los logs anteriores.

echo "--- Creando entorno virtual con Python 3.12 ---"
uv venv .venv --python 3.12

echo "--- Activando entorno virtual ---"
source .venv/bin/activate

echo "--- Instalando dependencias ---"
# Usamos uv pip para mayor velocidad y compatibilidad
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
uv pip install -r reqs.txt

echo "--- Inicializando Reflex ---"
python -m reflex init

echo "--- Exportando Frontend (Static) ---"
python -m reflex export --frontend-only --no-zip

# Preparamos la carpeta de salida para Vercel
echo "--- Preparando carpeta public ---"
rm -rf public
mkdir -p public
cp -r .web/_static/* public/

echo "--- Construcción completada con éxito ---"
