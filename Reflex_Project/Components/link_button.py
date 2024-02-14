import reflex as rx
from Reflex_Project.Styles import styles
from Reflex_Project.Styles.styles import Size as Size


def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
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
    