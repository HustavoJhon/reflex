import reflex as rx
from me.styles.styles import Size as Size


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "hustavojhon",
            height="40px"
        ),
        position="sticky",
        bg="lightgray",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0", #statica 
    )