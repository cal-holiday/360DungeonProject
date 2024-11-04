import Model
import View


class Controller:

    #Controller sees both model and view so
    #constructor needs both
    def __init__(self):
        self.model = Model.Model()
        self.view = View.View(self)

    #always run program in Controller!
    def main(self):
        #runs view main -> GUI
        self.view.main()

    #button behavior
    #caption = button pressed
    def on_button_click(self, caption):
        #button clicked send data to model to calculate
        result = self.model.calculate(caption)
        #send result to view for user
        self.view.value_var.set(result)

if __name__ == '__main__':
    calculator = Controller()
    calculator.main()

