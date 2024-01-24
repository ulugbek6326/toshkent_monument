from modeltranslation.translator import TranslationOptions, register

from .models import News

@register(News)
class NewsTranslation(TranslationOptions):
    fields=('title', 'description', )