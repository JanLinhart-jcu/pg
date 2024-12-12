from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):

    def is_position_on_board(self, position):
        return 0 <= position[0] < 8 and 0 <= position[1] < 8

    def possible_moves(self):
        row, col = self.position
        moves = []

        # Pěšák se pohybuje o 1 políčko vpřed, případně o 2 ze startovní pozice
        if self.color == 'white':
            if self.is_position_on_board((row - 1, col)):
                moves.append((row - 1, col))
            if row == 6 and self.is_position_on_board((row - 2, col)):
                moves.append((row - 2, col))
        elif self.color == 'black':
            if self.is_position_on_board((row + 1, col)):
                moves.append((row + 1, col))
            if row == 1 and self.is_position_on_board((row + 2, col)):
                moves.append((row + 2, col))

        # Přidání tahů pro braní figur šikmo (diagonálně)
        if self.color == 'white':
            if self.is_position_on_board((row - 1, col - 1)):
                moves.append((row - 1, col - 1))
            if self.is_position_on_board((row - 1, col + 1)):
                moves.append((row - 1, col + 1))
        elif self.color == 'black':
            if self.is_position_on_board((row + 1, col - 1)):
                moves.append((row + 1, col - 1))
            if self.is_position_on_board((row + 1, col + 1)):
                moves.append((row + 1, col + 1))

        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
    
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce (Bishop).
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []

        # Směry pro diagonální pohyby: (up-right), (up-left), (down-right), (down-left)
        directions = [
            (1, 1),   # diagonálně nahoru a doprava
            (1, -1),  # diagonálně nahoru a doleva
            (-1, 1),  # diagonálně dolů a doprava
            (-1, -1)  # diagonálně dolů a doleva
        ]

        # Pro každý směr zkontroluj, kam může střelec pohnout
        for direction in directions:
            drow, dcol = direction
            r, c = row, col

            # Posunuj se po diagonále, dokud nenarazíš na hranice šachovnice
            while True:
                r += drow
                c += dcol
                if 0 <= r < 8 and 0 <= c < 8:
                    moves.append((r, c))
                else:
                    break
        
        return moves
    
    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'



class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        # Směry pro vertikální a horizontální pohyby: (nahoru), (dolů), (doprava), (doleva)
        directions = [
            (1, 0),   # dolů
            (-1, 0),  # nahoru
            (0, 1),   # doprava
            (0, -1)   # doleva
        ]

        # Pro každý směr zkontroluj, kam může věž pohnout
        for direction in directions:
            drow, dcol = direction
            r, c = row, col

            # Posunuj se ve směru, dokud nenarazíš na hranice šachovnice
            while True:
                r += drow
                c += dcol
                if 0 <= r < 8 and 0 <= c < 8:
                    moves.append((r, c))
                else:
                    break

        return moves

    
    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    
    def possible_moves(self):
        
        row, col = self.position
        moves = []

        # Směry pro pohyby královny: horizontální, vertikální, diagonální
        directions = [
            (1, 0),   # dolů
            (-1, 0),  # nahoru
            (0, 1),   # doprava
            (0, -1),  # doleva
            (1, 1),   # diagonálně nahoru a doprava
            (1, -1),  # diagonálně nahoru a doleva
            (-1, 1),  # diagonálně dolů a doprava
            (-1, -1)  # diagonálně dolů a doleva
        ]

        # Pro každý směr zkontroluj, kam může královna pohnout
        for direction in directions:
            drow, dcol = direction
            r, c = row, col

            # Posunuj se ve směru, dokud nenarazíš na hranice šachovnice
            while True:
                r += drow
                c += dcol
                if 0 <= r < 8 and 0 <= c < 8:
                    moves.append((r, c))
                else:
                    break

        return moves
    
    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):

    def is_position_on_board(self, position):
        return 0 <= position[0] < 8 and 0 <= position[1] < 8

    def possible_moves(self):
        row, col = self.position
        moves = []

        # Směry pro pohyby krále: horizontální, vertikální, diagonální (jen o 1 políčko)
        directions = [
            (1, 0),   # dolů
            (-1, 0),  # nahoru
            (0, 1),   # doprava
            (0, -1),  # doleva
            (1, 1),   # diagonálně nahoru a doprava
            (1, -1),  # diagonálně nahoru a doleva
            (-1, 1),  # diagonálně dolů a doprava
            (-1, -1)  # diagonálně dolů a doleva
        ]

        # Pro každý směr zkontroluj, kam může král pohnout
        for direction in directions:
            drow, dcol = direction
            r, c = row + drow, col + dcol

            # Přidat pohyb, pokud je na šachovnici
            if self.is_position_on_board((r, c)):
                moves.append((r, c))

        return moves
    
    def __str__(self):
        return f'King({self.color}) at position {self.position}'



if __name__ == "__main__":
    piece = Knight("white", (1, 2))
    print(piece)
    print(piece.possible_moves())
    
    piece2 = Bishop("black", (1, 3))
    print(piece2)
    print(piece2.possible_moves())

    piece3 = Rook("black", (1, 1))
    print(piece3)
    print(piece3.possible_moves())

    piece4 = Queen("black", (1, 4))
    print(piece4)
    print(piece4.possible_moves())
    
    piece5 = King("black", (1, 5))
    print(piece5)
    print(piece5.possible_moves())

    piece6 = Pawn("white", (2, 5))
    print(piece6)
    print(piece6.possible_moves())
    

