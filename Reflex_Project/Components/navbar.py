import reflex as rx
import Reflex_Project.Styles.styles as styles
from Reflex_Project.Styles.styles import Size as Size
from Reflex_Project.Styles.colors import Color as Color
from Reflex_Project.Styles.colors import TextColor as Tcolor


def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.box(
            rx.chakra.span("alejo_digital"),
            style=styles.navbar_title_style_01,
            color=Tcolor.BODY.value
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )
