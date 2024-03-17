import reflex as rx
import web_links.styles.styles as style

def title(text : str) -> rx.Component:
    return rx.heading(
        text, 
        size="5",
        style= style.title_style,
        padding="2%"
    )