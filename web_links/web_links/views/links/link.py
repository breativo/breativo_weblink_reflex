import reflex as rx
from web_links.components.link_button import link_button
from web_links.components.title import title
from web_links.styles.styles import Size as Size
from web_links.styles.color import Color as cl
import web_links.constants as cont


def links () ->  rx.Component:
    return rx.vstack(
        title("Enlaces interes"),

            link_button(
                        "breativo.com", 
                        "Web oficial breativo",
                        "icons/code.svg",
                        cont.WEB_URL),

            link_button(
                        "Linkedin", 
                        "Información sobre breativo",
                        "icons/linkedin.svg",
                        cont.LINKEDIN),

            link_button(
                        "GitHub",
                        "Cursos y proyectos de código abierto",
                        "icons/github.svg",
                        cont.GITHUB),

            link_button(
                        "Twitch", 
                        "Transmisiones sobre desarrollo de aplicaciones móviles y web.",
                        "icons/twitch.svg",
                        cont.TWITCH_URL),

            link_button(
                        "You Tube",
                        "Tutoriales sobre el desarrollo de aplicaciones móviles y web. ",
                        "icons/youtube.svg",
                        ""),

            link_button(
                        "Discord", 
                        "El chat de la comunidad para intercambiar conocimientos.",
                        "icons/discord.svg",
                        ""),

        title("Destacados"),
                        
        title("Cursos"),

                link_button(
                            "Python by breativo", 
                            "Domina Python con breativo",
                            "icons/python.svg",
                            cont.PYTHON,
                            ),

        title("Contacto"),

            link_button(
                        "Mis lecturas", 
                        "Mi listado de libros sobre programación.",
                        "icons/book.svg",
                        ""),

            link_button(
                        "Email",
                        "breativo@breativo.com",
                        "icons/correo.svg",
                        ""),
            
            width="100%",
            spacing="3"
    )