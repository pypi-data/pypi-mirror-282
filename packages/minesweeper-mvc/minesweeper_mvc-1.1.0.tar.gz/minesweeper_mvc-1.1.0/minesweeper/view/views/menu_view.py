import sys

import pygame

from .view import BaseView
from ..elements.button import Button
from ..elements.image import Image
from ...assets.colors import SECONDARY_COLOR
from ...config import (
    CAPTION,
    ICON,
    FRAME_RATE,
    FONT,
    FONT_SIZE,
    SOUNDS,
    MENU_BACKGROUND,
)
from ...utils.get_path import get_path_to_file_from_root


class MenuView(BaseView):
    def __init__(self, controller):
        BaseView.__init__(
            self,
            caption=CAPTION,
            width=600,
            height=800,
            background_color=pygame.Color(SECONDARY_COLOR),
            frame_rate=FRAME_RATE,
            icon=pygame.image.load(get_path_to_file_from_root(ICON)),
        )
        self.objects = []
        self.font = pygame.font.Font(get_path_to_file_from_root(FONT), FONT_SIZE)
        self.background_image = None
        self.mouse_handlers = []
        self.menu_buttons = []
        self.sound_effect = pygame.mixer.Sound(get_path_to_file_from_root(SOUNDS["click"]))
        self.controller = controller
        self.controller.set_view(self)
        self.create_menu()

    def create_menu(self):
        def start_game():
            self.sound_effect.play()
            self.controller.set_view_state("game")
            self.view_run = False

        def on_play_easy(button):
            self.controller.set_game_mode("easy")
            start_game()

        def on_play_medium(button):
            self.controller.set_game_mode("medium")
            start_game()

        def on_play_hard(button):
            self.controller.set_game_mode("hard")
            start_game()

        def on_scoreboard(button):
            self.sound_effect.play()
            self.controller.set_view_state("records")
            self.view_run = False

        def on_quit(button):
            sys.exit()

        self.background_image = Image(
            pygame.image.load(get_path_to_file_from_root(MENU_BACKGROUND)), 0, 0, 600, 800
        )
        self.objects.append(self.background_image)
        for i, (text, click_handler) in enumerate(
            (
                ("EASY", on_play_easy),
                ("MEDIUM", on_play_medium),
                ("HARD", on_play_hard),
                ("RECORDS", on_scoreboard),
                ("QUIT", on_quit),
            )
        ):
            b = Button(
                225,
                300 + (50 + 10) * i,
                150,
                50,
                text,
                click_handler,
                padding=5,
                font=self.font,
                corner_radius=15,
            )
            self.objects.append(b)
            self.menu_buttons.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)

    def update(self):
        pass
