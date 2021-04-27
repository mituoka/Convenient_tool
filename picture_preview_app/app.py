#-*- coding: utf-8 -*-
from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.app import App

from kivy.uix.widget import Widget

from kivy.properties import StringProperty

from kivy.core.text import LabelBase,DEFAULT_FONT
from kivy.resources import resource_add_path

from random import randint

# デフォルトに使用するフォントを変更する
resource_add_path('/System/Library/Fonts')
#日本語が使用できるように日本語フォントを指定する
LabelBase.register(DEFAULT_FONT, 'PingFang.ttc') 

# イメージフォルダの指定
resource_add_path('./image')
  
class ImageWidget(Widget):
    source = StringProperty('./image/000001.jpg')

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        pass

    def buttonStarted(self):
        self.source= './image/000001.jpg'

    def buttonRandom(self):
        self.source = f'00000{randint(1, 9)}.jpg'

class PictureApp(App):
    def __init__(self, **kwargs):
        super(PictureApp, self).__init__(**kwargs)
        self.title = '取得画像'
 
# プログラム7｜mainを呼び出す
if __name__ == "__main__":
    PictureApp().run()