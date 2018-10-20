
"""

    责任链模式
"""


class Event(object):
    """事件"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget(object):

    def __init__(self, parent=None):
        self.parent = parent

    def handler(self, event):
        handler = "handler_{}".format(event)
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handler(event)
        elif hasattr(self, "handler_default"):
            self.handler_default(event)


class MainWindow(Widget):

    def handler(self, event):
        print("MainWindow: {}".format(event))

    def handler_default(self, event):
        print("MainWindow Default: {}".format(event))


class SendDialog(Widget):

    def handler_paint(self, event):
        print("SendDialog: {}".format(event))


class MsgText(Widget):

    def handler_down(self, event):
        print("MsgText: {}".format(event))


def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)

    for e in ("down", "paint", "unhandler", "close"):
        evt = Event(e)
        print("\nSending event -{}- to MainWindow".format(evt))
        mw.handler(evt)
        print("Sending event -{}- to SendDialog".format(evt))
        sd.handler(evt)
        print("Sending event -{}- to MsgText".format(evt))
        msg.handler(evt)


if __name__ == '__main__':
    main()
