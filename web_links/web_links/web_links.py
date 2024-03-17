
import reflex as rx
from web_links.components.navbar  import navbar
from web_links.views.header.header import header
from web_links.views.links.link import links
from web_links.components.footer import footer
import web_links.styles.styles as styles


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
            navbar(),
            rx.center(
            rx.vstack(
                header(),
                links(),
                max_width= styles.MAX_WIDTH,
                width = "100%",
                margin_y= styles.Size.BIG.value
            ),
            ),
            footer()
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index,
            title="breativo | Full Stack Developer by iOS, Android y web.",
            description="",
            image="favicon.png")
app.compile()
