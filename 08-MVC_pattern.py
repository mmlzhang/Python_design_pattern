
quotes = ('A man is not complete until he is married. Then he is finished.',
          'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted woman.',
          'Black holes really suck...', 'Facts are stubborn things.')

class QuoteModel(object):
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = "Not Found"
        return value


class QuoteTerminalView(object):
    def show(self, quote):
        print(quote)

    def error(self, msg):
        print("Error is:", msg)

    def select_quote(self):
        return input("输入选择的quote序号：")


class QuoteTermalController(object):
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            n = self.view.select_quote()
            n = int(n)
            valid_input = True
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    controller = QuoteTermalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()
