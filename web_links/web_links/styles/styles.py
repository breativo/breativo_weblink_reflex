import reflex as rx
from enum import Enum
from .color import Color
from .color import ColorText
from .fonts import Font
from .fonts import FontWeight


# Constants
MAX_WIDTH ="650px"

# fonts
STYLESHEETS=[
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap"
]
# Sizes
class Size(Enum):
    ZERO= "0.0em"
    SMALL ="0.5em"
    MEDIUM= "0.8em"
    DEFAULT ="1.0em"
    BIG = "1.5em"
    LARGE ="2.0em"
    VERYBIG ="3.0em"

# Style

BASE_STYLE = {

    "background_color": Color.BACKGRAUND.value,
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    

    rx.heading:{
            "size":"7",
            "color":ColorText.HEADER.value,
            "font_family": Font.DEFAULT.value,
            "font_weight": FontWeight.MEDIUM.value,
    },

    rx.button:{
        "width" : "90%",
        "height" : "100%",
        "display" : "block",
        "margin" : "auto",
        "padding" : Size.DEFAULT.value,
        "background_color": Color.SECONDARY.value,
        "border_radius": Size.DEFAULT.value,
        "color" : ColorText.HEADER.value,
        "_hover" : {
            "background_color" : Color.PRIMARY.value
            }
    },

    rx.link:{
        "text_decoration" : "none",
        "_hover" :{}
    }
}


# Styles component
navbar_title_style = dict (
    font_size= Size.BIG.value,
    Color= ColorText.TEXT.value,
    font_family= Font.DEFAULT.value,
    font_weight= FontWeight.MEDIUM.value,
)

title_style = dict (
    width="100%",
    margin_top=Size.BIG.value,
    color=ColorText.TEXT.value,
    font_family= Font.DEFAULT.value,
    font_weight= FontWeight.MEDIUM.value,
)

button_title_style = dict (
    font_size=Size.BIG.value,
    color=ColorText.TEXT.value,
    font_family= Font.DEFAULT.value,
    font_weight= FontWeight.MEDIUM.value,
)

button_body_style = dict (
    font_size=Size.MEDIUM.value,
    color=ColorText.BODY.value,
    font_family= Font.DEFAULT.value,
    font_weight= FontWeight.LIGHT.value,
)