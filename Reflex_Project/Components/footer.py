import reflex as rx
import datetime
import Reflex_Project.Constants as const
from Reflex_Project.Styles import styles


def footer() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.image(
                src="Reflex.svg",
                height=styles.Size.BIG.value,
                # Forzamos el logo a ser Verde Terminal (#238636) con filtros CSS
                filter="brightness(0) saturate(100%) invert(43%) sepia(87%) saturate(395%) hue-rotate(81deg) brightness(88%) contrast(90%)",
                transition="transform 0.3s ease-in-out",
                _hover={
                    "transform": "scale(1.1)"
                }
            ),
            href=const.REFLEX_URL,
            is_external=True
        ),
        rx.vstack(
            rx.text(
                f"© 2023-{datetime.date.today().year} @Alejo_Digital by Alejandro Guerrero",
                font_size=styles.Size.MEDIUM.value,
                color=styles.Color.PRIMARY.value, # Verde Terminal
                text_align="center"
            ),
            rx.text(
                "This entire website is made in Reflex-Python with <3 from Bogotá to the World.",
                font_size=styles.Size.MEDIUM.value,
                color=styles.Color.PRIMARY.value, # Verde Terminal
                text_align="center"
            ),
            rx.text(
                "Apocalipsis 22:21",
                font_size=styles.Size.MEDIUM.value,
                color=styles.Color.PRIMARY.value, # Verde Terminal
                font_weight="bold"
            ),
            spacing="1",
            align="center",
            width="100%",
            margin_top=styles.Size.LARGE.value
        ),
        padding_y=styles.Size.VERY_BIG.value,
        align="center",
        width="100%",
        padding_x=styles.Size.DEFAULT.value
    )
