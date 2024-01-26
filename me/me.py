import reflex as rx
# STYLE
import me.styles.styles as styles
from me.styles.styles import Size as Size

# COMPONENTS
from me.components.navbar import navbar
from me.components.footer import footer

# VIEWS
from me.views.header.header import header
from me.views.links.links import links




class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        # navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value
            ),
        ),
        footer()
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
app.compile()