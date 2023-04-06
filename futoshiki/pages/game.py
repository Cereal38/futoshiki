
# Futoshiki
import pynecone as pc


def displayCar(value):

    return pc.grid_item(
        value,
        row_span=1, col_span=1,
        bg="lightgrey",
        width=50, height=50,
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

            # Grid
            pc.grid(
                # pc.foreach(State.grid, lambda line, index: pc.grid_item(
                #     line[0], row_span=1, col_span=1, bg="lightgrey", width=50, height=50)),
                pc.foreach(
                    State.grid, lambda line:
                    pc.foreach(line, displayCar)
                ),
                template_columns="repeat(7, 1fr)",
                template_rows="repeat(7, 1fr)",
                height='fit-content',
                width="fit-content",
                gap=1,
                padding=5,
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
