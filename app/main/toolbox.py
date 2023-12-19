import sys
from app.models import Character
from app.main.forms import CharacterForm

class Converters:

    def str_to_class(str):
        return getattr(sys.modules[__name__], str)