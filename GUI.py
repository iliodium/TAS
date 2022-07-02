from kivymd.app import MDApp
from kivy.lang.builder import Builder


class TAS(MDApp):
    def build(self):
        '''Загрука файла GUI.kv'''
        return Builder.load_file("GUI.kv")


if __name__ == '__main__':
    TAS().run()
