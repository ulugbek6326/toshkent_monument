from modeltranslation.translator import TranslationOptions, register

from .models import Memory


@register(Memory)
class MemoryTranslation(TranslationOptions):
    fields=('title', 'description',)