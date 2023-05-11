from kivy.app import App 
from kivy.uix.widget import Widget

# class para o pong game
class PongGame (Widget):
    pass

# class para app
class PongApp (App):
    def build(self):
        return PongGame()

if __name__ == '__main__':
    PongApp().run()
    
