class WidgetDict:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.widgets = {}

    def add(self, i, button):
        self.widgets[i] = button
