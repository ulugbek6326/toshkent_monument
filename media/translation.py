from modeltranslation.translator import TranslationOptions, register

from .models import Media
class MediaTranslations(TranslationOptions):
    fields = ('title',)


