# 🚀 Alejo_Digital Portafolio (Reflex-Python)

Este es un portafolio personal moderno y profesional, construido íntegramente con el framework **Reflex** (antes Pynecone). La aplicación sigue una arquitectura de componentes escalable y utiliza una estética técnica denominada **"The Dev Terminal"**, inspirada en los editores de código y herramientas de desarrollo.

---

## 🎨 Características Visuales
- **Modo Oscuro/Claro:** Implementación reactiva basada en la paleta de GitHub (Dark/Light).
- **Terminal Glow:** Efectos de brillo neón en iconos y botones interactivos.
- **Diseño Responsivo:** Optimizado para dispositivos móviles y escritorio.
- **Arquitectura de Componentes:** Separación clara entre Vistas, Componentes, Estilos y Constantes.

---

## 🏗️ Arquitectura del Proyecto
El proyecto está organizado siguiendo las mejores prácticas de Reflex para facilitar la mantenibilidad:

```text
Reflex_Project/
├── Components/         # Componentes atómicos (Botones, Iconos, Navbars)
├── Views/             # Secciones completas de la página (Header, Links)
├── Styles/            # Configuración de colores, fuentes y estilos globales
├── Constants.py       # Único punto de verdad para los datos del perfil
├── state.py           # Gestión del estado global de la aplicación
└── Reflex_Project.py  # Punto de entrada y configuración de páginas/SEO
```

---

## 🛠️ Tecnologías Usadas
- **Framework:** [Reflex](https://reflex.dev/) (Full-stack Python Web)
- **Lenguaje:** Python 3.10+
- **Estilos:** CSS3 (via Reflex Radix/Chakra primitives)
- **Despliegue:** Reflex Cloud / Vercel

---

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/Alejo-Digital/Reflex_Project.git
cd Reflex_Project
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Ejecutar en modo desarrollo
```bash
reflex run
```
La aplicación estará disponible en `http://localhost:3000`.

---

## 📦 Despliegue
Para preparar la aplicación para producción:
```bash
chmod +x build.sh
./build.sh
```

---

## 📜 Licencia e Información
© 2023-2026 @Alejo_Digital by Alejandro Guerrero.
Este proyecto está bajo la licencia MIT.

> "This entire website is made in Reflex-Python with <3 from Bogotá to the World." 🌍✨
