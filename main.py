from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (400,600)






Builder.load_file("main.kv")
class Calculator(Widget):
    # number functions
    def numbers(self,num):
        number = self.ids.input.text
        if number == '0' or number == 'Error':
            self.ids.input.text = ''
        self.ids.input.text += f'{num}'

    # arithmatic operators
    def operator(self,op):
        self.ids.input.text += f'{op}'

    # clear the textinput
    def clear(self):
        self.ids.input.text = '0'
    
    def del_last(self):
        if len(self.ids.input.text) == 1:
            if self.ids.input.text != '0':
                text = '0'
                self.ids.input.text = text
            else:
                pass
        else:
            text = self.ids.input.text[:-1]
            self.ids.input.text = text

    # equal
    def equal(self):
        x = self.ids.input.text
        try:
            self.ids.input.text = str(eval(x))
        except:
            self.ids.input.text = 'Error'

        

class CalculatorApp(App):
    def build(self):
        return Calculator()
    
    
if __name__ == '__main__':
    CalculatorApp().run()