import reflex as rx
from me.components.link_button import link_button
from me.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("About Me"),
        link_button(
            "blog", 
            "aprende linux", 
            "https://github.com/hustavojhon"
        ),
        link_button(
            "Discord", 
            "comunidad de Pacman", 
            "https://github.com/hustavojhon"
        ),
        link_button(
            "Website", 
            "sobre mi", 
            "https://github.com/hustavojhon"
        ),
        width="100%"
    )