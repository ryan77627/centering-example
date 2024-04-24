###################################
# Entrypoint for Virtualbox script
#
# Author: Ryan Schanzenbacher 2024
###################################
from textual.app import App, ComposeResult
from textual.containers import Center, Middle, Container
from textual.widgets import Footer, LoadingIndicator, Label, Rule, Button
from textual.screen import ModalScreen

class LoadingModal(ModalScreen):
    def compose(self) -> ComposeResult:
        with Container():
            yield Label("Welcome! Please Wait...")
            yield Rule()
            with Center():
                yield LoadingIndicator()

    def key_q(self) -> None:
        """Close Modal"""
        self.app.pop_screen()

class VirtualBoxManager(App):
    """Entrypoint to management app"""
    CSS_PATH = "main.tcss"

    BINDINGS = [
            ("d", "toggle_dark", "Toggle Dark Mode"),
            ("q", "quit", "Quit Application")
        ]
    
    def compose(self) -> ComposeResult:
        """Create a loading screen"""
        yield Button("Press me!")
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def on_button_pressed(self) -> None:
        self.push_screen(LoadingModal())

if __name__ == "__main__":
    VirtualBoxManager().run()
