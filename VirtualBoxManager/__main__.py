###################################
# Entrypoint for Virtualbox script
#
# Author: Ryan Schanzenbacher 2024
###################################
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class VirtualBoxManager(App):
    """Entrypoint to management app"""

    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]
    
    def compose(self) -> ComposeResult:
        """Create children"""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

if __name__ == "__main__":
    app = VirtualBoxManager()
    app.run()
