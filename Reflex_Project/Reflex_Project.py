"""This entire website is made in Reflex!"""

import reflex as rx
from Reflex_Project.Components.navbar import navbar
from Reflex_Project.Views.Header.header import header
from Reflex_Project.Views.Links.links import links
from Reflex_Project.Components.footer import footer
import Reflex_Project.Styles.styles as styles
from Reflex_Project.Styles.styles import Size as Size


#class State(rx.State):
    #pass


def index() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                padding=Size.BIG.value,
                margin_y=styles.Size.BIG.value
            )
        ),
        footer()
    )
    

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Alejo_Digital | Analisis de Datos y Programacion Python",
    image="favicon.ico"
)
#bogapp.compile()


# Run the app
if __name__ == "__main__":
    app.run()