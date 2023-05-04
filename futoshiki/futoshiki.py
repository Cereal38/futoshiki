"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

# Futoshiki
import pynecone as pc

# Pages
from futoshiki.pages.game import pageGame

# Text
from futoshiki.utils.text import TEXT_FUTOSHIKI_DESCRIPTION

# Functions
from futoshiki.utils.solver import solve as solveGrid

# Python functions
from typing import List
from random import randint

# Grid
from futoshiki.utils.grids import grids


# Arrows : ᐊᐅᐃᐁ

class State(pc.State):
    """The app state."""

    # Display digits
    gridDigit: List[List[str]] = [
        ['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', ''],
    ]
    
    # Display inequalities
    gridInequal: List[List[str]] = []

    # Contain inequalities
    inequalities: List[List[List[int]]] = []

    def newGrid (self) :
      
      # Load a random grid
      randomGrid = grids[randint(0, len(grids) - 1)]
      
      # Modify state with new datas
      self.gridDigit = randomGrid['gridDigits']
      self.inequalities = randomGrid['gridInequals']
      self.gridInequal = self.create_grid_inequal(self.inequalities)

    def solve (self) :
        solution = solveGrid(self.gridDigit, self.inequalities)
        self.gridDigit = solution

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
            gridInequalsFormat[indexRow][indexCol] = 'ᐃ'
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

    def __init__(self):
        """Initialize the state."""
        super().__init__()
        self.newGrid()
              
          
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
