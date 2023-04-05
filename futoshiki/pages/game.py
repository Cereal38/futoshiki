
# Futoshiki
import pynecone as pc


# def gridItem(value):
#     return pc.grid_item(row_span=1, col_span=1, bg="lightgrey", width=50, height=50),


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
                pc.foreach(State.grid, lambda gridItem: pc.grid_item(
                    row_span=1, col_span=1, bg="lightgrey", width=50, height=50)),
                template_columns="repeat(4, 1fr)",
                template_rows="repeat(4, 1fr)",
                height='fit-content',
                width="fit-content",
                gap=1,
                padding=5,
            ),

            # Buttons
            pc.center(
                pc.button('New', size='lg'),
                pc.button('Solve', size='lg', color_scheme='blue'),
                gap=5,
            )

        )
    )
