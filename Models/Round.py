from Models.TicTacToeBoard import TicTacToeBoard
from Models.MachinePlayer import MachinePlayer
from Models.PersonPlayer import PersonPlayer
from Models.Player import Player
from random import shuffle

class Round:
    def __init__(self, machine_player: bool = True):
        self.__winner = None
        self.__winner_name = None
        self.__moves = []

        self.machine_player = machine_player
        self.game_board = TicTacToeBoard()
        self.players = self.__start_players(machine_player, self.game_board)

    def __start_players(self, machine_player: bool, game_board: TicTacToeBoard) -> dict:
        players: list[Player] = [
            PersonPlayer(game_board),
            MachinePlayer(game_board) if machine_player else PersonPlayer(game_board)
        ]
        shuffle(players)
        symbols = game_board.symbols.copy()
        for i in range(len(symbols)):
            players[i].symbol = symbols.pop()

        return {f'Player {i}': player for i, player in zip(range(1, len(players) + 1), players)}
    
    def __show_players_types(self):
        for player_name, player in self.players.items():
            machine = '(machine)' if isinstance(player, MachinePlayer) else ''
            print(f'{player_name} {machine}: {player.symbol}')
    
    def start(self):
        while self.game_board.empty_spots:
            for player_name, player in self.players.items():
                self.game_board.display()
                self.__show_players_types()
                if not self.game_board.empty_spots:
                    self.__show_tie()
                    break

                print(f'\n{player_name}\'s turn.')
                move_made = player.play()

                if move_made:
                    self.__moves.append(player.last_move)

                if self.game_board.winner_exists:
                    self.game_board.display()
                    p_name, winner = self.__get_winner()
                    self.__show_winner(p_name, winner)
                    return

    def __show_winner(self, winner_name: str, winner: Player):
        print(f'{winner_name}({winner.symbol} ) won!')

    def __show_tie(self):
        print(f'There\'s been a tie')

    def __get_winner(self):
        winner_symbol = self.game_board.winner
        winner = None
        for p_name, p in self.players.items():
            if p.symbol == winner_symbol:
                winner = p
                self.__winner_name, self.winner = p_name, p
                return (p_name, winner)
            
        return None
    
    def get_data(self):
        return {
            'winner_name': self.__winner_name,
            'winner_player': self.__winner,
            'all_moves': self.__moves,
            'players': self.players
        }