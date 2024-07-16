import os


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self,ai_game):
        """初始化统计信息"""
        self.settings=ai_game.settings
        self.reset_stats()
        # 在任何情况下都不应重置最高分
        self.high_score=self._load_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left=self.settings.ship_limit
        self.score=0
        self.level=1

    def _get_high_score_file_path(self):
        """获取存储最高分的文件路径"""
        return os.path.join(os.path.dirname(__file__), 'high_score.txt')
    
    def _load_high_score(self):
        """从文件中加载最高分"""
        file_path = self._get_high_score_file_path()
        try:
            with open(file_path, 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return 0
        
    def save_high_score(self):
        """将最高分保存到文件中"""
        file_path = self._get_high_score_file_path()
        with open(file_path, 'w') as file:
            file.write(str(self.high_score))