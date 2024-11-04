class Model:

    #model is not aware of view or controller so you don't
    #pass either class in constructor
    def __init__(self):
        self.previous_value = ''
        self.value = ''
        self.operator = ''

    def calculate(self, caption):
        if caption == 'C':
            self.value = ''
            self.previous_value = ''
            self.value = ''
            self.operator = ''
        elif caption == '+/-':
            #if user value is negative then return everything after negative sign, otherwise add negative sign
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
        elif caption == '.':
            #check if decimal point is in value already
            if not caption in self.value:
                self.value += caption
        elif caption == '%':
            value = float(self.value) if '.' in self.value else int(self.value)
            self.value = str(value/100)
        elif caption == '=':
            value = self._evaluate()
            if '.0' in str(value):
                value = int(value)
            self.value = str(value)
        elif isinstance(caption, int):
            self.value += str(caption)
        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ''

        return self.value


    def _evaluate(self):
        return eval(self.previous_value + self.operator + self.value)