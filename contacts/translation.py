from modeltranslation.translator import TranslationOptions , register

from .models import Contacts

@register(Contacts)
class ContactTranslator(TranslationOptions):
    fields = ('description',)