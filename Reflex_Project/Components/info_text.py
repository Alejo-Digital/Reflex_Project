import reflex as rx
from Reflex_Project.Styles.styles import Size as Size, TEXT_COLOR_BODY
from Reflex_Project.Styles.colors import Color as Color


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text.span(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value
        ),
        f" {body}", 
        font_size=Size.MEDIUM.value,
        color=TEXT_COLOR_BODY
    )
