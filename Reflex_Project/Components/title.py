import reflex as rx
import Reflex_Project.Styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.chakra.heading(
        text,
        size="lg",
        style=styles.title_style
        )