class WidgetDict:
    widgets = {}

    @classmethod
    def add(cls, name, button):
        cls.widgets[name] = button
