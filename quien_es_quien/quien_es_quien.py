
import reflex as rx
from rxconfig import config
from quien_es_quien import style
from quien_es_quien import state
from quien_es_quien.state import State
from quien_es_quien import personajes



def zona_de_personajes() -> rx.Component:
    return rx.center(
        rx.grid(
            rx.foreach(
                rx.Var.range(24), lambda i: 
                    rx.card(
                        rx.inset(
                            rx.image(
                                src=f"{i + 1}.jpg", width="100%", height="100%"
                            ),
                            height="13em",
                            width="7.5em"
                    )
                ),
            ),
            columns="8",
            spacing="4",
            width="60%",
        )
    )

def barra_de_accion() -> rx.Component:
    return rx.box(
        rx.input(
            value=State.pregunta_usuario,
            placeholder="Ej: ¿Lleva gafas?", 
            on_change=State.set_pregunta_usuario,
            width="75%"
            
        ),
        rx.button(
            "Enviar",
            on_click=State.mensaje_usuario
            ),
        style = style.caja_texto,

    )

    
def personaje_a_adivinar() -> rx.Component:
    return rx.box(
        state.escoger_carta(),
        style = style.personaje_misterioso
    )

def index() -> rx.Component:
    return rx.box(
        zona_de_personajes(),
        personaje_a_adivinar(),
        barra_de_accion(),
    )

app = rx.App()
app.add_page(index)