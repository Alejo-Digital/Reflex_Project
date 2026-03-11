import reflex as rx
from Reflex_Project.Components.link_icon import link_icon
from Reflex_Project.Components.info_text import info_text
from Reflex_Project.Styles import styles
from Reflex_Project.Styles.colors import Color
import Reflex_Project.Constants as const
from Reflex_Project.state import State


def header() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.avatar(
                name=const.NAME,
                size="7",
                src=const.PROFILE_IMAGE,
                padding=styles.Size.NANO.value,
                border=f"4px solid {Color.PRIMARY.value}",
                fallback="AG"
            ),
            rx.vstack(
                rx.heading(
                    const.NAME,
                    size="8",
                    color=styles.TEXT_COLOR_HEADER
                ),
                rx.text(
                    const.USER_NAME,
                    margin_top=styles.Size.ZERO.value,
                    color=Color.PRIMARY.value,
                    font_weight="bold"
                ),
                rx.hstack(
                    link_icon(
                        "instagram.svg",
                        const.INSTAGRAM_URL
                    ),
                    link_icon(
                        "x-twitter.svg",
                        const.TWITTER_URL
                    ),
                    link_icon(
                        "tiktok.svg",
                        const.TIKTOK_URL
                    ),
                    spacing="4"
                ),

                align_items="start",
            ),
            align="start",
            spacing="5",
            flex_direction=["column", "row"],
            width="100%"
        ),
        rx.flex(
            info_text(f"+{State.years_experience}", "año de experiencia"),
            rx.spacer(),
            info_text(const.PROJECTS_COUNT, "proyectos freelance"),
            rx.spacer(),
            info_text(const.STUDY_HOURS, "horas de estudio"),
            width="100%"
        ),
        rx.text(
            const.DESCRIPTION,
            color=styles.TEXT_COLOR_BODY,
            font_size=styles.Size.DEFAULT.value,
            width="100%"
        ),
        spacing="6",
        align_items="start",
        width="100%"
    )
