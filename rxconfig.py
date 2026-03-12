import reflex as rx

config = rx.Config(
    app_name="Reflex_Project",
    # Esto desactivará el aviso del plugin de Sitemap
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
    # Esta línea es clave para que el frontend sepa a dónde hablar
    api_url="https://alejodigital.vercel.app"
)