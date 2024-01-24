from modeltranslation.translator import TranslationOptions, register

from .models import AboutForWe


@register(AboutForWe)
class AboutForWeTranslator(TranslationOptions):
    fields = ('description')