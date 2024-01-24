from modeltranslation.translator import TranslationOptions, register

from .models import Books


@register(Books)
class BookTranslator(TranslationOptions):
    fields=('name')