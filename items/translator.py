from modeltranslation.translator import TranslationOptions, register

from .models import Items


@register(Items)
class ItemTranslation(TranslationOptions):
    fields = ('title', 'description',)