import reflex as rx
import datetime


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.link(
            f"year> {datetime.date.today().year} GUSTAVO",
            href="https://vercel.com",
            is_external=True
        ),
        rx.text("© 2019-2024 SOFTWARE ENGINNER ♥ .")
    )