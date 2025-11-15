import logging
from textual.app import App
from textual.logging import TextualHandler

logging.basicConfig(
    level="NOTSET",
    handlers=[TextualHandler()],
)

class LogApp(App):
    """Using logging with Textual."""

    def on_mount(self) -> None:
        logging.debug("Logged via TextualHandler")

if __name__ == "__main__":
    LogApp().run()