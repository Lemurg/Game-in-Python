class Stats():
    '''Отслеживание статистики игры'''
    def __init__(self):
        '''Инициализирует статистику'''
        self.reset_stats()
        '''Игра запускается в активном состоянии'''
        self.game_active = True
        '''Рекордный счет никогда не сбрасываться'''
        with open('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/highscore.txt', 'r') as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        '''Инициализирует статистику, изменяющуюся в ходе игры'''
        self.ships_left = 2
        self.score = 0