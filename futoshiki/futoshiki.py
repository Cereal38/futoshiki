"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

# Futoshiki
import pynecone as pc

# Pages
from futoshiki.pages.game import pageGame

# Text
from futoshiki.utils.text import TEXT_FUTOSHIKI_DESCRIPTION

filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Futoshiki", font_size="2em"),
            pc.text(TEXT_FUTOSHIKI_DESCRIPTION, font_size='1em', width='80%'),
            pc.link(
                "Start playing",
                href='/game',
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, route='/')
app.add_page(pageGame, route='/game')
app.compile()
