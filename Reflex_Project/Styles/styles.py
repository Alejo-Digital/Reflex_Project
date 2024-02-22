from enum import Enum
import reflex as rx
from .colors import Color as Color
from .colors import TextColor as Tcolor
from .fonts import Font, FontWeight


# Constants
MAX_WIDTH = "600px"


#Fonts
STYLESHEETS=[
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]


# Sizes
class Size(Enum):
    ZERO = "0px 1important"
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
    "background_color": Color.BACKGROUND.value,
    rx.chakra.heading: {
        "size": "lg",
        "color": Tcolor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
        "white_space": "normal",
        "text_align": "start",
        "width": "100%"
    },
    rx.chakra.Button:{
        "width": "100%",
        "height": "100%",
        "dosplay": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": Tcolor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECONDARY.value,
            "color": Color.CONTENT.value
        }
    },
    rx.chakra.Link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style_01 = dict(
    font_family=Font.LOGO.value,
    font_size=Size.LARGE.value,
    font_weight=FontWeight.MEDIUM.value
)

navbar_title_style_02 = dict(
    font_family="Source Code Pro",
    font_size=Size.LARGE.value
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_size=Size.DEFAULT.value,
    font_weight=FontWeight.MEDIUM.value,
    color=Tcolor.HEADER.value
    )

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.MEDIUM.value,
    color=Tcolor.BODY.value,

    )