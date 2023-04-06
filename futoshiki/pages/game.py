
# Futoshiki
import pynecone as pc

def displayDigit(value):

    return pc.grid_item(
        value,
        row_span=1, col_span=1,
        bg="lightgrey",
        width='60px', height='60px',
        display='flex',
        justifyContent='center',
        alignItems='center',)

def displayInequal(value):

    return pc.grid_item(
        value,
        row_span=1, col_span=1,
        width='20px', height='20px',
        display='flex',
        justifyContent='center',
        alignItems='center',)


def pageGame(State) -> pc.Component:

    return pc.center(
        pc.vstack(

            # Header
            pc.box(
                pc.link(
                    'Futoshiki',
                    href='/',
                    font_size='2em',
                ),
                width='100vw',
                padding=5,
            ),

            pc.box(
                width='100vw',
                padding=5,
            ),

            # Grid
            pc.box(
                pc.grid(
                    pc.foreach(
                        State.gridInequal, lambda line:
                        pc.foreach(line, displayInequal)
                    ),
                    template_columns="repeat(15, 1fr)",
                    template_rows="repeat(15, 1fr)",
                    height='fit-content',
                    width="fit-content",
                    gap='0',
                    position='absolute',
                ),
                pc.grid(
                    pc.foreach(
                        State.gridDigit, lambda line:
                        pc.foreach(line, displayDigit)
                    ),
                    template_columns="repeat(4, 1fr)",
                    template_rows="repeat(4, 1fr)",
                    height='fit-content',
                    width="fit-content",
                    gap='20px',
                ),
                position='relative',
            ),

            # Buttons
            pc.center(
                pc.button('New', size='lg'),
                pc.button(
                    'Solve',
                    size='lg',
                    color_scheme='blue',
                    on_click=State.solve
                ),
                gap=5,
            )

        )
    )
