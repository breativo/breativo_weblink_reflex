import reflex as rx
from web_links.styles.styles import Size as Size
from web_links.styles.color import ColorText as ct
from web_links.styles.color import Color as cl
from web_links.styles.fonts import Font as fo
from web_links.styles.fonts import FontWeight as fw
def info_text (title:str , body:str)-> rx.Component:
    return rx.box(
        rx.vstack(
        rx.text(
            title,
            font_size= Size.VERYBIG.value,
            color= cl.PRIMARY.value),
        rx.text(
            body
            ),

        font_size= Size.MEDIUM.value,
        font_family= fo.DEFAULT.value,
        font_weight= fw.LIGHT.value,
        color= ct.BODY.value,
        spacing="0",
        style={
                "justify-content": "center", 
                "align-items": "center",  
            }
        )
    )