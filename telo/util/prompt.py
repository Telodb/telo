from telo.util import color as c

class Prompt:
    def __init__(self, color='white', localInput=True):
        color = color.lower()
        self.color = color if color in ('red', 'green', 'blue') else 'white'
        self.localInput = localInput


    def s(self, text, default=''):
        if not self.color == 'white':
            dark = eval("c." + self.color)
            light = eval("c.light" + self.color)
        else:
            dark = c.white
            light = c.grey

        query = dark(text) + light('[' + default + ']') + dark(': ')
        if self.localInput:
            result = input(query)
            if result == '':
                return default
            else:
                return result
        else:
            return query
