import reflex as rx
import datetime
from Reflex_Project.Components.title import title
from Reflex_Project.Components.link_icon import link_icon
from Reflex_Project.Styles.styles import Size as Size
from Reflex_Project.Components.info_text import info_text
from Reflex_Project.Styles.colors import TextColor as Tcolor
from Reflex_Project.Styles.colors import Color as Color
import Reflex_Project.Constants as const

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Alejandro Guerrero", 
                size="xl",
                bg=Color.CONTENT.value,
                color=Tcolor.BODY.value,
                src="Profile-removebg.png",
                padding=Size.NANO.value,
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "Alejandro Guerrero",
                    size="lg",
                    padding_x=Size.DEFAULT.value
                ),
                rx.text("@alejo_digital",
                    margin_top=Size.ZERO.value,
                    color=Tcolor.BODY.value,
                    padding_x=Size.MEDIUM.value
                ),
                rx.hstack(
                    link_icon(
                       "instagram.svg",
                       const.INSTAGRAM_URL
                    ),
                    link_icon(
                        "x-twitter.svg",
                        const.TWITTER_URL
                    ),
                    link_icon(
                        "tiktok.svg",
                        const.TIKTOK_URL
                    ),
                    padding_x=Size.MEDIUM.value,
                    spacing=Size.LARGE.value
                ),
            ),
            align_items="start",            
            spacing=Size.VERY_BIG.value,
            padding_left=Size.LARGE.value,
            padding_y=Size.DEFAULT.value
        ),
        rx.flex(
            info_text("+1", "año de experiencia"),
            rx.spacer(),
            info_text("+5", "proyectos freelance"),
            rx.spacer(),
            info_text("+200", "horas de estudio"),
            width="100%"
        ),
        rx.text(
            """
            Soy Politólogo con un Diplomado en Business Intelligence 
            y una Especializacion en Data Analyst.
            Actualmente trabajo Freelance como Python Developer, BI & Data Analyst.
            Aqui en mi website podrás encontrar todos mis enlaces de interes. 
            Bienvenid@s!
            """,
            color=Tcolor.BODY.value,
            font_size=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.BIG.value,
        align_items="start"
    )