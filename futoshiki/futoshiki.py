"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

# Futoshiki
import pynecone as pc

# Pages
from futoshiki.pages.game import pageGame

# Text
from futoshiki.utils.text import TEXT_FUTOSHIKI_DESCRIPTION

# Type
from typing import List

filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    grid:List[List[str]] = [
        ['0', '.', '1', 'l', '0', '.', '0'],
        ['u', '.', '.', '.', '.', '.', 'd'],
        ['0', '.', '1', 'l', '0', 'r', '0'],
        ['u', '.', '.', '.', '.', '.', 'd'],
        ['0', '.', '1', 'l', '0', '.', '0'],
        ['u', '.', '.', '.', '.', '.', 'd'],
        ['0', '.', '1', 'l', '0', '.', '0'],
    ]

    def solve (self):
        self.grid[0][0] = 3


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading('Futoshiki', font_size="2em"),
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
app.add_page(index, route='/', title='Futoshiki')
app.add_page(lambda: pageGame(State), route='/game', title='Futoshiki')
app.compile()
