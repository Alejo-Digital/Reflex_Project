import reflex as rx
from Reflex_Project.Styles.styles import Size as Size
from Reflex_Project.Styles.colors import TextColor as Tcolor
from Reflex_Project.Styles.colors import Color as Color


def info_text(title: str, body: str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.span(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value
        ),
        f" {body}", 
        font_size=Size.MEDIUM.value,
        color=Tcolor.BODY.value
    )
