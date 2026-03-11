from enum import Enum
import reflex as rx
from .colors import Color as Color
from .colors import TextColor as Tcolor
from .fonts import Font, FontWeight


# Constants
MAX_WIDTH = "560px"

# Colores Reactivos (Variables Dinámicas)
TEXT_COLOR_HEADER = rx.color_mode_cond(light=Tcolor.HEADER_LIGHT.value, dark=Tcolor.HEADER.value)
TEXT_COLOR_BODY = rx.color_mode_cond(light=Tcolor.BODY_LIGHT.value, dark=Tcolor.BODY.value)

BG_COLOR_PAGE = rx.color_mode_cond(light=Color.BACKGROUND_LIGHT.value, dark=Color.BACKGROUND.value)
BG_COLOR_CONTENT = rx.color_mode_cond(light=Color.CONTENT_LIGHT.value, dark=Color.CONTENT.value)
BG_COLOR_NAVBAR = rx.color_mode_cond(light=Color.CONTENT_LIGHT.value, dark=Color.CONTENT.value)

# Colores de bordes (Variables, no strings)
BORDER_COLOR = rx.color_mode_cond(light=Color.BORDER_LIGHT.value, dark=Color.BORDER_DARK.value)

BUTTON_HOVER_STYLE = {
    "background_color": Color.PRIMARY.value,
    "color": "#FFFFFF",
    "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
    "border": f"1px solid {Color.PRIMARY.value}"
}


#Fonts
STYLESHEETS=[
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]


# Sizes
class Size(Enum):
    ZERO = "0px !important"
    NANO = "0.125em"
    MICRO = "0.25em"
    SMALL = "0.5em"
    MEDIUM = "0.75em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


#Styles    
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

# Define el estilo del contenedor principal de la página
PAGE_STYLE = {
    "background_color": BG_COLOR_PAGE,
    "min_height": "100vh",
    "width": "100%"
}

navbar_title_style_01 = dict(
    font_family=Font.LOGO.value,
    font_size=Size.LARGE.value,
    font_weight=FontWeight.MEDIUM.value
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_size=Size.DEFAULT.value,
    font_weight=FontWeight.MEDIUM.value,
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.MEDIUM.value,
)
