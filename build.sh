#!/bin/bash

# Script de construcción para despliegue
set -e # Detener el script si ocurre algún error

echo "--- Instalando dependencias ---"
pip install --upgrade pip
pip install -r requirements.txt

echo "--- Inicializando Reflex ---"
reflex init

echo "--- Exportando Frontend (Static) ---"
# Limpiamos exportaciones anteriores
rm -rf .web/_static
reflex export --frontend-only --no-zip

# Si usas un servidor tipo Vercel o Netlify, el contenido suele ir a una carpeta 'dist' o 'public'
# Aquí lo preparamos para ser servido estáticamente
mkdir -p public
cp -r .web/_static/* public/

echo "--- Construcción completada con éxito ---"
