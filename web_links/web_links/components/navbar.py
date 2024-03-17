import reflex as rx
import web_links.styles.styles as style
from web_links.styles.styles import Size as Size
from web_links.styles.color import Color as cl
from web_links.styles.color import ColorText as ct


def navbar () -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.image(src="icons/logo.svg", 
                    height=Size.LARGE.value,
                    wight= Size.LARGE.value,
                    alt= "Logotipo de breativo. Texto formando el nombre de breativo."
            ),
        ),
        background_color=cl.SECONDARY.value,
        position = "sticky",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )