class GameEntry:
    
    def __init__(self, name, score):
        self._name = name
        self._score = score
        
    def get_name(self):
        return self._name
    
    def get_score(self):
        return self._score
    
    def __str__(self):
        return '({0}: {1})'.format(self._name, self._score)
        
  
class Scoreboard:
    
    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = 0
        
    def __getitem__(self, k):
        return self._board[k]
    
    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))
    
    def add(self, entry):
        score = entry.get_score()
        
        good = self._n < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._n < len(self._board):
                self._n += 1
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry
        
    
if __name__ == '__main__':
    board = Scoreboard()
    gamer_list = {
        'Tom': 1100,
        'Jerry': 750,
        'Mickey': 800,
        'Donald': 1900,
        'Daisy': 1000,
        'Goofy': 950,
        'Kjjd': 590,
        'Lo': 941,
        'Tyu': 579,
        'Wq': 1000,
        'Qw': 1003,
        'Wgh': 1540
    }
    for name, score in gamer_list.items():
        board.add(GameEntry(name, score))
    print(board)

        
    
    