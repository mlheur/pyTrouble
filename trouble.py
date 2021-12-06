#!/usr/bin/env python3  

class Cell(object):

    def __init__(self,head,occupant=None) -> None:
        super().__init__()
        self.occupant = occupant
        if head is None:
            self.next = self
            self.last = self
        else:
            self.next = head
            self.last = head.last
            head.last = self
        self.exit_id = None

    def is_occupied(self):
        return self.occupant is not None

    def clear(self):
        token = self.occupant
        self.occupant = None
        return token

    def occupy(self,token):
        if self.is_occupied():
            return self.occupant
        self.occupant = token
        return None
    
    def set_exit(self,player):
        self.exit_id = player.id
        self.exit = player.base

    def seek_ahead(self,player,amount):
        ahead = self
        while amount > 0:
            amount -= 1
            ahead = ahead.get_next(player)
            if ahead is None: return ahead
        return ahead
    
    def get_next(self,player):
        if self.exit_id == player.id:
            return self.exit
        return self.next
    
    def __str__(self) -> str:
        if self.is_occupied(): return str(self.occupant)
        return "__"


class HomeCell(Cell):
    def __init__(self, player, head, occupant) -> None:
        super().__init__(head, occupant)
        print("Create Home Cell occupant:{}".format(self.occupant))
        self.player = player
        self.exit_id = player.id
        self.exit = player.start
    
    def __str__(self) -> str:
        if self.is_occupied(): return str(self.occupant)
        return "{}H".format(self.player)
    
    def seek_ahead(self, player, amount, for_display = False):
        if not for_display: return super().seek_ahead(self,player,amount)
        ahead = self
        while amount > 0:
            amount -= 1
            ahead = ahead.next
            if ahead is None: return ahead
        return ahead
        


class BaseCell(Cell):
    def __init__(self, player, head) -> None:
        super().__init__(head, None)
        self.player = player
    def __str__(self) -> str:
        if self.is_occupied(): return str(self.occupant)
        return "{}B".format(self.player)


class Token(object):
    def __init__(self,player,id) -> None:
        super().__init__()
        self.player = player
        self.id     = id
        print ("Created Token p:{} id:{}\n".format(player,id))
    def __str__(self) -> str:
        return "{}{}".format(self.player,self.id)


class Player(object):

    def __init__(self,board,id) -> None:
        super().__init__()
        self.board = board
        self.id = id
        if id == 0:
            self.start = board.head
        else:
            self.start = Cell(board.head)

        self.home = HomeCell(self,None,Token(self,0))
        self.base = BaseCell(self,None)
        for t in range(1,board.token_qty):
            self.last_home = HomeCell(self,self.home,Token(self,t))
            self.last_base = BaseCell(self,self.base)
        self.last_base.next = None

        for c in range(1,board.cells_per_player):
            Cell(board.head)
    
    def __str__(self) -> str:
        return self.board.C[self.id]


class Board(object):

    def __init__(self,colors,C,token_qty,cells_per_player) -> None:
        super().__init__()
        self.colors           = colors
        self.C                = C
        self.players          = list()
        self.head             = Cell(None)
        self.cells_per_player = cells_per_player
        self.token_qty        = token_qty
        for p in range(len(colors)):
            self.players.append(Player(self,p))
        
        for p in self.players: p.start.last.set_exit(p)
    
    def run(self):
        print(str(self))

    def __str__(self) -> str:
        board_str = ""

        # print Home cells
        for line_no in range(self.token_qty):
            line = "HOME_{:02d}---".format(line_no)
            for p in self.players:
                line = "{}{}-".format(line,p.home.seek_ahead(p,line_no,True))
            board_str = "{}{}\n".format(board_str,line)

        # print Game cells
        for line_no in range(self.cells_per_player):
            line = "GAME_{:02d}---".format(line_no)
            for p in self.players:
                line = "{}{}-".format(line,p.start.seek_ahead(p,line_no))
            board_str = "{}{}\n".format(board_str,line)

        # print Base cells
        for line_no in range(self.token_qty):
            line = "BASE_{:02d}---".format(line_no)
            for p in self.players:
                line = "{}{}-".format(line,p.base.seek_ahead(p,line_no))
            board_str = "{}{}\n".format(board_str,line)

        return board_str


if __name__ == "__main__":
    colors = ("red","green","yellow","blue")
    C      = ("R",  "G",    "Y",     "B")
    Board(colors,C,4,7).run()
