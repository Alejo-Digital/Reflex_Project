import reflex as rx
from Reflex_Project.Styles.styles import title_style, TEXT_COLOR_HEADER

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="6",
        style=title_style,
        color=TEXT_COLOR_HEADER
        )