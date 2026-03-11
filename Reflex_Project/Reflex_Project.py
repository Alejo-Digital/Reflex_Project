import reflex as rx
from Reflex_Project.Components.navbar import navbar
from Reflex_Project.Views.Header.header import header
from Reflex_Project.Views.Links.links import links
from Reflex_Project.Components.footer import footer
from Reflex_Project.Styles import styles
import Reflex_Project.Constants as const


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                padding=styles.Size.BIG.value,
                margin_y=styles.Size.BIG.value,
                align="center",
                spacing="7"
            )
        ),
        footer(),
        style=styles.PAGE_STYLE
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        has_background=True,
    ),
)

app.add_page(
    index,
    title=f"{const.NAME} | Python Developer & Data Analyst",
    description=const.DESCRIPTION,
    image=const.FAVICON,
    meta=[
        {"name": "og:title", "content": f"{const.NAME} | Portafolio Personal"},
        {"name": "og:description", "content": const.DESCRIPTION},
        {"name": "og:image", "content": f"https://alejodigital.dev/{const.FAVICON}"},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": const.USER_NAME},
    ]
)
