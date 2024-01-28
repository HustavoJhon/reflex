import reflex as rx
import me.constants as const 
import datetime

from me.components.link_icon import link_icon
from me.components.info_text import info_text 
from me.styles.styles import Size as Size

from me.styles.colors import TextColor as TextColor



def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Gustavo Jhon", 
                size="xl"
            ),
            rx.vstack(
                rx.heading(
                    "GUSTAVO JHON", 
                    size="lg",
                    color=TextColor.HEADER.value,
                ),
                rx.text(
                    "@hustavojhon",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value,
                ),
                rx.hstack(
                    link_icon("https://x.com/hustavojhon"),
                    link_icon("https://x.com/hustavojhon"),
                    link_icon("https://x.com/hustavojhon"),
                    link_icon("https://x.com/hustavojhon"),
                ),
                align_items="start",
            ),
            spacing=Size.BIG.value,
        ),

        rx.flex(
            info_text("+3", "anios de experiencia"),
            rx.spacer(),
            info_text("+19", "anios viviendo"),
            rx.spacer(),
            info_text("+3", "mese teniendo enamorada xd"),
            rx.spacer(),
            width="100%"
        ),

        rx.text(
            f"""
                Soy un programador entusiasta enfocado en mejorar constantemente. 
                Apasionado por Linux, encuentro en su versatilidad un estímulo para la creatividad. 
                Mi interés se extiende al diseño gráfico, explorando la unión entre estética y funcionalidad. 
                """,
                color=TextColor.BODY.value,
                font_family="Comfortaa",
            ),
        spacing=Size.BIG.value,
        align_items="start",
    )