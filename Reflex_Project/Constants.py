import reflex as rx

# Perfil Profesional
NAME = "Alejandro Guerrero"
USER_NAME = "@alejo_digital"
DESCRIPTION = """
            Soy Politólogo con un Diplomado en Business Intelligence 
            y una Especialización en Data Analyst.
            Actualmente trabajo Freelance como Python Developer, BI & Data Analyst.
            Aquí en mi website podrás encontrar todos mis enlaces de interés. 
            ¡Bienvenid@s!
            """
PROFILE_IMAGE = "Profile-removebg.png"
FAVICON = "favicon.ico"

# Estadísticas
PROJECTS_COUNT = "+5"
STUDY_HOURS = "+200"

# URLs
LINKEDIN_URL = "https://www.linkedin.com/in/alejo-digital/"
PORTAFOLIO_URL = "https://alejodigital.dev"
GITHUB_URL = "https://github.com/Alejo-Digital"
BLOG_URL = "https://digitalalejo.blogspot.com/"
REDDIT_URL = "https://www.reddit.com/user/Alejo_Digital"

# Redes Sociales
TWITTER_URL = "https://twitter.com/Alejo_Digital"
INSTAGRAM_URL = "https://www.instagram.com/alejo_digital/"
TIKTOK_URL = "https://www.tiktok.com/@alejo_digital"

#Contacto
EMAIL_URL = "mailto:digital.alejo@gmail.com"
TELEGRAM_URL = "https://t.me/Alejo_Digital"

#Reflex Website
REFLEX_URL = "https://reflex.dev/"

#Colaborar
PAYPAL_URL = "https://paypal.me/alejodigital22?country.x=CO&locale.x=es_XC"

# Fechas
START_DATE = "2024-02-14" # Puedes ajustar la fecha real aquí

import datetime
_start_date = datetime.date.fromisoformat(START_DATE)
_today = datetime.date.today()
YEARS_EXPERIENCE = _today.year - _start_date.year - ((_today.month, _today.day) < (_start_date.month, _start_date.day))
