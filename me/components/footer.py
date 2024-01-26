import reflex as rx
import datetime
from me.styles.colors import Color as Color
from me.styles.colors import TextColor as TextColor

from me.styles.styles import Size as Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.link(
            f"year> {datetime.date.today().year} GUSTAVO",
            href="https://vercel.com",
            is_external=True,
            font_size=Size.MEDIUM.value,
        ),
        rx.text(
            "© 2019-2024 SOFTWARE ENGINNER ♥ .",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value,
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value,
    )