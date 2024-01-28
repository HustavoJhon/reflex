import reflex as rx
import me.styles.styles as styles
from me.styles.styles import Size as Size
from me.styles.colors import Color as Color



def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("Gustavo", color=Color.PRIMARY.value),
            rx.span(" Jhon", color=Color.SECONDARY.value),
            style=styles.navbar_title_style,
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0", #statica 
    )