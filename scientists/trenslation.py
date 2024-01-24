from modeltranslation.translator import TranslationOptions, register

from .models import Scientists

@register(Scientists)
class Scientisttranslator(TranslationOptions):
    fields=('name', 'degree', 'description',)