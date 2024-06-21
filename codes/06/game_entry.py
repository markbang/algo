class GameEntry:
    """Represents one entry of a list of high scores."""
    
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name 

    def get_score(self):
        return self._score 

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)  # e.g., '(Bob, 98)'


if __name__ == "__main__":
    game_entry_zheng = GameEntry("正峰", 90)
    game_entry_ze = GameEntry("阿泽", 95)

    print(game_entry_zheng.get_name())
    print(game_entry_ze.get_score)

    print(game_entry_zheng)
    print(game_entry_ze)

