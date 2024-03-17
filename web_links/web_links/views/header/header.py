import reflex as rx
from web_links.components.link_icon import link_icon
from web_links.components.info_text import info_text
from web_links.styles.styles import Size as Size
from web_links.styles.color import ColorText as ct
from web_links.styles.color import Color as cl

def header()-> rx.Component:
    return rx.vstack(
        
            rx.image(
                    src="icons/logo.svg",
                    margin_top= Size.BIG.value,
                    alt= "Logotipo de breativo. Texto formando el nombre de breativo."),

                    rx.hstack(
                        link_icon(
                            "icons/twitter.svg",
                            "https://twitter.com/breativo"
                            ),

                        link_icon(
                            "icons/instagram.svg",
                            "https://www.instagram.com/breativo/"
                            ),

                        link_icon(
                            "icons/tiktok.svg",
                            "https://www.tiktok.com/@breativo"
                            ),
                    ),

        rx.flex(
                info_text("+2", "Años de experiencia"),
                rx.spacer(),
                info_text("+5", "Lenguajes de programación"),
                rx.spacer(),
                info_text("+50", "Proyectos realizados"),
                width="100%"
        ),

        rx.text("""
                Breativo surge de una profunda pasión y un sueño persistente: avanzar y evolucionar constantemente como profesional en el vibrante mundo del desarrollo de software. A lo largo de los últimos años, he dedicado mi carrera a dominar una diversidad de lenguajes de programación y tecnologías, incluyendo Java, JavaScript, Python, Kotlin y Swift, cada uno aportando su propia esencia y conjunto de desafíos al arte del desarrollo de software.                """,
                color=ct.BODY.value,
                margin_top=Size.BIG.value,
                font_size=Size.DEFAULT.value
                ),
        
        rx.text("""
                La misión de Breativo es sencilla pero poderosa: compartir y devolver a la comunidad el caudal de conocimientos y experiencias acumuladas durante estos años de aprendizaje y práctica. Creo firmemente en el crecimiento colectivo y en el impacto positivo que podemos generar al compartir nuestras habilidades y descubrimientos con otros. 
                """,
                color=ct.BODY.value,
                margin_bottom=Size.BIG.value,
                font_size=Size.DEFAULT.value
                ),   
                width="90%",
                margin="auto",
                aling_item="start",
                spacing= "8"
    )