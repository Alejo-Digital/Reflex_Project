import reflex as rx
from Reflex_Project.Styles import styles


def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=styles.Size.MEDIUM.value,
                    # Filtro reactivo para que el icono coincida con el texto
                    filter=rx.color_mode_cond(
                        light="brightness(0) invert(0.2)", # Gris oscuro en modo claro
                        dark="none" # Blanco original en modo oscuro
                    ),
                    # Cuando pasamos el mouse sobre el BOTÓN, el icono debe ser blanco
                    # para contrastar con el fondo verde del hover.
                    _group_hover={
                        "filter": "brightness(0) invert(1)"
                    }
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style, color=styles.TEXT_COLOR_HEADER),
                    rx.text(body, style=styles.button_body_style, color=styles.TEXT_COLOR_BODY),
                    spacing="1",
                    align_items="start",
                    margin=styles.Size.ZERO.value
                ),
                width="100%",
                align="center"
            ),
            background_color=styles.BG_COLOR_CONTENT,
            border=f"1px solid {styles.BORDER_COLOR}",
            width="100%",
            padding_y=styles.Size.SMALL.value, 
            padding_x=styles.Size.DEFAULT.value,
            height="auto",
            _hover=styles.BUTTON_HOVER_STYLE,
            border_radius=styles.Size.DEFAULT.value,
            role="group" # Necesario para que el icono sepa cuando el botón recibe hover
        ),
        href=url,
        is_external=True,
        width="100%"
    )
