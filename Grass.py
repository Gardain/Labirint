from LevelGroup import LevelGroup
from LevelSprite import LevelSprite


class FLour(LevelSprite):
    def __init__(self, row, col, *groups):
        super().__init__(row, col, 'flour.png', groups)


class FlourGroup(LevelGroup):
    def __init__(self, level):
        super().__init__(level)
        self.key = ['.', '@']
        self.sprite_class = Flour
        self.create_sprites()