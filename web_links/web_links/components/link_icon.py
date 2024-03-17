import reflex as rx
from web_links.styles.styles import Size as Size

def link_icon(image: str, url :str )-> rx.Component:
    return rx.link(
            rx.image(
                src=image,
                width=  Size.BIG.value,
                height= Size.BIG.value,
                margin= Size.ZERO.value,
            ),
            href=url,
            is_external=True,
    )