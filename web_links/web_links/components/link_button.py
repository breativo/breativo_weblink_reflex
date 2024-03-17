import reflex as rx
import web_links.styles.styles as style
from web_links.styles.styles import Size as Size

def link_button(title : str, body: str, image: str, url: str) -> rx.Component:
    return rx.link( 
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=  Size.LARGE.value,
                    height= Size.LARGE.value,
                    margin= Size.BIG.value,
                    alt= title
                ),
                rx.vstack(
                        rx.text(title, style= style.button_title_style),
                        rx.text(body, style= style.button_body_style),
                        spacing="0",
                        aling_item="start",
                        margin=Size.ZERO.value
                )
            ),
        
        ),
        href=url,
        is_external=True,
        width="100%"
    )