"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

# Futoshiki
import pynecone as pc

# Pages
from futoshiki.pages.game import pageGame

# Text
from futoshiki.utils.text import TEXT_FUTOSHIKI_DESCRIPTION

# Funcions
from futoshiki.utils.solver3 import solve as solveGrid

# Type
from typing import List


# Arrows : ᐊᐅᐃᐁ

class State(pc.State):
    """The app state."""

    gridDigit: List[List[str]] = [
        ['4', '', '', ''],
        ['', '', '3', ''],
        ['', '', '', ''],
        ['', '', '', ''],
    ]

    gridInequal: List[List[str]] = [
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', 'Δ', '', '', '', '', '', '', '', 'ᐊ', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', 'ᐅ', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', 'ᐁ', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', 'ᐊ', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ]
    # gridInequal: List[List[str]] = [
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    # ]

    def solve(self):
        solution = solveGrid(self.gridDigit, [[[0, 1], [1, 1]]])
        self.gridDigit = solution
        self.gridInequal = self.create_grid_inequal([
            [[1, 1], [0, 1]],
            [[1, 1], [1, 2]],
            [[1, 1], [2, 1]],
            [[1, 1], [1, 0]],
        ])

    def create_grid_inequal(self, constraints):
      """
      Format constraints to display it
      """

      gridInequalsFormat = [['' for i in range(15)] for j in range(15)]

      for constraint in constraints :
          # Check row
          maxValue = max(constraint[0][0], constraint[1][0])
          if (maxValue == 0) :
              indexRow = 1
          else :
            if (constraint[0][0] == constraint[1][0]) :
              indexRow = maxValue * 4 + 1
            else :
              indexRow = maxValue * 4 - 1

          # Check column
          maxValue = max(constraint[0][1], constraint[1][1])
          if (maxValue == 0) :
              indexCol = 1
          else :
              if (constraint[0][1] == constraint[1][1]) :
                indexCol = maxValue * 4 + 1
              else :
                indexCol = maxValue * 4 - 1
          
          # Up
          if (constraint[0][0] > constraint[1][0]) :
            gridInequalsFormat[indexRow][indexCol] = 'Δ'
          # Down
          elif (constraint[1][0] > constraint[0][0]) :
            gridInequalsFormat[indexRow][indexCol] = 'ᐁ'
          # Left
          elif (constraint[0][1] > constraint[1][1]) :
            gridInequalsFormat[indexRow][indexCol] = 'ᐊ'
          # Right
          elif (constraint[1][1] > constraint[0][1]) :
            gridInequalsFormat[indexRow][indexCol] = 'ᐅ'
      
      return gridInequalsFormat
          
              
              
          
          


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
