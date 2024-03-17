import reflex as rx
import datetime 
from web_links.styles.styles import Size as Size
from web_links.styles.color import ColorText as ct

def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(src="icons/favicon.svg", 
                    height=Size.BIG.value,
                    wight= Size.BIG.value,
                    alt= "Logotipo de breativo. Texto formando el nombre de breativo."),
            rx.text(
                    f"© {datetime.date.today().year} breativo",
                    font_size=Size.MEDIUM.value
            ),
            
            style={
                "justify-content": "center", 
                "align-items": "center",  
                "height": "100%", 
            }
        ),
        padding=Size.BIG.value,
        width="100%",
        color=ct.FOOTER.value
    )
