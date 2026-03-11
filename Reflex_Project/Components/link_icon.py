import reflex as rx
from Reflex_Project.Styles import styles

def link_icon(image: str, url: str) -> rx.Component:
    """
    Componente de icono social con efecto de brillo 'Terminal Glow'.
    """
    # Filtro para que el icono tome el color del texto del header (Blanco roto en dark, Gris oscuro en light)
    # y cambie a Verde Terminal en hover.
    
    return rx.link(
        rx.image(
            src=image,
            width=styles.Size.DEFAULT.value,
            height=styles.Size.DEFAULT.value,
            # Aplicamos un filtro base que sincronice con el color del texto
            filter=rx.color_mode_cond(
                light="brightness(0) invert(0.2)", # Gris oscuro
                dark="brightness(0) invert(0.95)"   # Blanco roto
            ),
            transition="all 0.3s ease-in-out",
            _hover={
                # Cambia a verde terminal (#238636) y añade un resplandor sutil
                "filter": "brightness(0) saturate(100%) invert(43%) sepia(87%) saturate(395%) hue-rotate(81deg) brightness(88%) contrast(90%)",
                "transform": "scale(1.1)",
                "drop_shadow": f"0 0 8px {styles.Color.PRIMARY.value}"
            }
        ),
        href=url,
        is_external=True
    )
