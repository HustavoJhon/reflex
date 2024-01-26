import reflex as rx
from me.styles.styles import Size as Size
from me.styles.colors import TextColor as TextColor
from me.styles.colors import Color as Color


def info_text(title : str, body : str) -> rx.Component:
    return rx.box(
        rx.span(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value,
        ),
        f" {body}", 
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value,
    )