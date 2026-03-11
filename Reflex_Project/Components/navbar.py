import reflex as rx
from Reflex_Project.Styles import styles
from Reflex_Project.Styles.colors import Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text.span("alejo_digital", color=Color.PRIMARY.value),
            style=styles.navbar_title_style_01,
        ),
        rx.spacer(),
        rx.color_mode.button(),
        position="sticky",
        bg=styles.BG_COLOR_NAVBAR,
        padding_x=styles.Size.DEFAULT.value,
        padding_y=styles.Size.SMALL.value,
        z_index="999",
        top="0",
        width="100%",
        align="center",
        border_bottom=f"1px solid {styles.BORDER_COLOR}"
    )
