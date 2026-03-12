#!/bin/bash

# Script de construcción para despliegue en Vercel
set -e # Detener el script si ocurre algún error

echo "--- Instalando dependencias ---"
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "--- Inicializando Reflex ---"
# Usamos python3 -m reflex para asegurar que encuentre el ejecutable
python3 -m reflex init

echo "--- Exportando Frontend (Static) ---"
python3 -m reflex export --frontend-only --no-zip

# Preparamos la carpeta de salida para Vercel
echo "--- Preparando carpeta public ---"
rm -rf public
mkdir -p public
cp -r .web/_static/* public/

echo "--- Construcción completada con éxito ---"
