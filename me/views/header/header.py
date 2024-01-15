import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Gustavo Jhon", size="xl"),
        rx.text("@hustavojhon"),
        rx.text("Hola mi nombre es Jhon Gustavo y un programador entusiasta.")
    )