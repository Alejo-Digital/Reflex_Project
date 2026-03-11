import reflex as rx
import datetime
import Reflex_Project.Constants as const

class State(rx.State):
    """El estado global de la aplicación."""
    
    @rx.var(cache=True)
    def years_experience(self) -> int:
        """Calcula automáticamente los años de experiencia."""
        start_date = datetime.date.fromisoformat(const.START_DATE)
        today = datetime.date.today()
        return today.year - start_date.year - ((today.month, today.day) < (start_date.month, start_date.day))
