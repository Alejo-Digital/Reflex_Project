import reflex as rx
from Reflex_Project.Components.link_button import link_button
from Reflex_Project.Components.title import title
from Reflex_Project.Styles.styles import Size as Size
import Reflex_Project.Constants as const


def links() -> rx.Component:
    return rx.vstack(
        title("Perfil"),
        link_button(
            "LinkedIn",
            "mi perfil profesional", 
            "linkedin-in.svg",
            const.LINKEDIN_URL,
        ),
        link_button(
            "Blog",
            "mi blog",
            "blogger-b.svg",
            const.BLOG_URL
        ),
        link_button(
            "GitHub",
            "mi repositorio",
            "github.svg",
            const.GITHUB_URL
        ),
        #link_button(
        #    "Portafolio",
        #    "mis proyectos",
        #    "briefcase-solid.svg",
        #    const.PORTAFOLIO_URL
        #),
        title("Contacto"),
        link_button(
            "Email",
            "mi correo",
            "envelope-solid.svg",
            const.EMAIL_URL
        ),
        link_button(
            "Telegram",
            "mi contacto directo",
            "telegram.svg",
            const.TELEGRAM_URL
        ),
        title("Colaborar"),
        link_button(
            "PayPal",
            "Apoyame con tu donacion",
            "paypal.svg",
            const.PAYPAL_URL
        ),
        width="100%",
        spacing=Size.DEFAULT.value,
        align_items="start"
    )