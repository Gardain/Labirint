from LevelGroup import LevelGroup
from LevelSprite import LevelSprite


class FLoor(LevelSprite):
    def __init__(self, row, col, *groups):
        super().__init__(row, col, 'floor.png', groups)


class FloorGroup(LevelGroup):
    def __init__(self, level):
        super().__init__(level)
        self.key = ['.', '@', '2']
        self.sprite_class = FLoor
        self.create_sprites()
