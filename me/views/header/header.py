import reflex as rx
import me.constants as const 
import datetime

from me.components.link_icon import link_icon
from me.components.info_text import info_text 
from me.styles.styles import Size as Size
from me.components.title import title

from me.styles.colors import TextColor, Color



def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Gustavo Jhon", 
                size="xl",
                src="/avatar.png",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
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
                    color=Color.PRIMARY.value,
                ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "/icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "/icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),
                    link_icon(
                        "/icons/spotify.svg",
                        const.SPOTIFY_URL,
                        "Spotify"
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    spacing=Size.LARGE.value,
                ),
                align_items="start",
            ),
            spacing=Size.BIG.value,
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text(
                        f"{experience()}+",
                        "years of experience"
                    ),
                    rx.spacer(),
                    info_text(
                        "+19", "years living"
                    ),
                    rx.spacer(),
                    info_text(
                        "+3", "months with lover"
                    ),
                    width="100%"
                ),
                rx.text(
                    f"""
            Soy un programador entusiasta enfocado en mejorar constantemente. 
            Apasionado por Linux, encuentro en su versatilidad un estímulo para la creatividad. 
            Mi interés se extiende al diseño gráfico, explorando la unión entre estética y funcionalidad.
            """,
                    font_size=Size.DEFAULT.value,
                    color=TextColor.BODY.value
                ),
                width="100%",
                spacing=Size.BIG.value
            )
        ),
        width="100%",
        spacing=Size.BIG.value,
        align_items="start"
    )


def experience() -> int:
    return datetime.date.today().year - 2021