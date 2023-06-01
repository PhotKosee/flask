# pylint: disable=missing-docstring
from deep_translator import MyMemoryTranslator

# tranlate english to french
def english_to_french(text):
    # return french
    return MyMemoryTranslator(source='english', target='french').translate(text)

# translate french to english
def french_to_english(text):
    # return english
    return MyMemoryTranslator(source='french', target='english').translate(text)
