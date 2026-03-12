#!/bin/bash

# Script de construcción para despliegue
set -e # Detener el script si ocurre algún error

echo "--- Instalando dependencias ---"
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "--- Inicializando Reflex ---"
reflex init

echo "--- Exportando Frontend (Static) ---"
# Exportamos el frontend
reflex export --frontend-only --no-zip

# Preparamos la carpeta de salida para Vercel
echo "--- Preparando carpeta public ---"
rm -rf public
mkdir -p public
cp -r .web/_static/* public/

echo "--- Construcción completada con éxito ---"
