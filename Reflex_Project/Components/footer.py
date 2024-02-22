import reflex as rx
import datetime
import Reflex_Project.Constants as Const
from Reflex_Project.Styles.styles import Size as Size
from Reflex_Project.Styles.colors import TextColor as Tcolor 
from Reflex_Project.Styles.colors import Color as Color



def footer() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.link(
            rx.chakra.image(
                src="Reflex.svg",
                height=Size.BIG.value,
                bg=Tcolor.HEADER.value,
                padding="2px",
                border="4px",
                ),
            href=Const.REFLEX_URL,
            is_external=True
        ),
        rx.chakra.text(
            f"@ 2023-{datetime.date.today().year} @Alejo_Digital By Alejandro Guerrero ∆",
            font_size=Size.MEDIUM.value,
            margin_top=Size.LARGE.value
            ),
        rx.chakra.text(
            "This entire website is made in Reflex-Python with <3 from Bogotá to the World.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value,
            padding_x=Size.LARGE.value,
        ),
        rx.chakra.text(
            "Apocalipsis 22:21",
            font_size=Size.MEDIUM.value,
        ),
        padding_y=Size.VERY_BIG.value,
        color=Tcolor.FOOTER.value
    )
