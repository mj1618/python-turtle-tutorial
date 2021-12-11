from .config import CELL_WIDTH, NUM_GRID_ROWS

def pause():
    input("Press escape to exit...")

def position_to_coord(x,y):
    return (x * CELL_WIDTH + CELL_WIDTH/2 - NUM_GRID_ROWS / 2 * CELL_WIDTH, y * CELL_WIDTH + CELL_WIDTH/2 - NUM_GRID_ROWS / 2 * CELL_WIDTH)