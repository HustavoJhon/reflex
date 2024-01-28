import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

# Constants
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    
# Styles

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value + "!important", #delete important in future updates
    
    rx.heading: {
        "size": "lg",
        "color":TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
    },
    
    rx.Button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover": {
            "background_color": Color.SECONDARY.value,
        }
    },
    rx.Link: {
        "text_decoration":"none",
        "_hover":{}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size=Size.LARGE.value,
)

title_style = dict(
    width="100%",
    font_family=Font.TITLE.value,
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_tittle_style = dict(
    font_family=Font.TITLE.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_body_style = dict(
    font_family=Font.DEFAULT.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)

