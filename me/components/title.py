import reflex as rx
import me.styles.styles as styles


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="lg", 
        style=styles.title_style
    )