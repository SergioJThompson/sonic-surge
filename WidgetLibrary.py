class WidgetLibrary:
    widgets = {}

    @classmethod
    def add(cls, name, button):
        cls.widgets[name] = button

# TODO: Should SoundMemoryBank also use a global variable? Probably. What about msglibrary and the others?
