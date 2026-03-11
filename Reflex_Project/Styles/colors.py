from enum import Enum


class Color(Enum):
    # Accents (Verde terminal y Azul Link)
    PRIMARY = "#238636"   # Success Green
    SECONDARY = "#58A6FF" # Link Blue
    
    # Dark Mode Palette (GitHub Dark)
    BACKGROUND = "#0D1117"
    CONTENT = "#161B22"
    BORDER_DARK = "#30363D"
    
    # Light Mode Palette (GitHub Light)
    BACKGROUND_LIGHT = "#F6F8FA"
    CONTENT_LIGHT = "#FFFFFF"
    BORDER_LIGHT = "#D0D7DE"


class TextColor(Enum):
    # Dark Mode Text
    HEADER = "#E6EDF3"    # Off-white
    BODY = "#8B949E"      # Muted Gray
    
    # Light Mode Text
    HEADER_LIGHT = "#1F2328" # Dark Gray
    BODY_LIGHT = "#636C76"   # Muted Text
    
    FOOTER = "#58A6FF"
