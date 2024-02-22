import reflex as rx
from Reflex_Project.Styles import styles
from Reflex_Project.Styles.styles import Size as Size


def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.button(
            rx.chakra.hstack(
                rx.chakra.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=Size.MEDIUM.value
                ),
                rx.chakra.vstack(
                    rx.chakra.text(title, style=styles.button_title_style),
                    rx.chakra.text(body, style=styles.button_body_style),
                    spacing=Size.SMALL.value,
                    align_items="start",
                    margin=Size.ZERO.value
                ),
                width="100%"
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )
    