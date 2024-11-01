import pygame


class Config:
    def __init__(self):
        self.dict = {}

    def get_value(self, param):
        return self.dict.get(param, None)

    def set_value(self, param, value):
        self.dict[param] = value

    def set_values(self, dict_values):
        for key in dict_values:
            self.dict[key] = dict_values[key]

    def get_all_values(self):
        return self.dict

    def get_list_values(self, *keys):
        return [self.get_value(param) for param in keys]


config = Config()
config.set_values(
    {'width': 550, 'height': 550, 'level': 'level1', 'tile_size': 50, 'level_end_event': pygame.USEREVENT + 1})
