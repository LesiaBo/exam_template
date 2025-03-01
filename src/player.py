class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        #TODO: returnera True om det inte står något i vägen
        #if 0 < self.pos_x + x < grid.width - 1 and 0 < self.pos_y + y < grid.height - 1:
        maybe_item = grid.get(self.pos_x + x, self.pos_y + y)
        #if isinstance(maybe_item, grid.wall):
        if maybe_item == grid.wall:
            print("Oooops, it was a wall!")
            return False
        else:
            return True


