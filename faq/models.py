# models.py

from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .utils import translate_text

class FAQ(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]

    question = models.TextField(_("Question in English"))
    answer = RichTextField(_("Answer"))
    
    question_hi = models.TextField(_("Question in Hindi"), blank=True, null=True)
    question_bn = models.TextField(_("Question in Bengali"), blank=True, null=True)
    
    language = models.CharField(_("Language"), max_length=2, choices=LANGUAGE_CHOICES, default='en')

    def get_translated_question(self, lang='en'):
        """Returns the translated question if available, otherwise falls back to English"""
        return getattr(self, f'question_{lang}', self.question) or self.question

    def __str__(self):
        return f"{self.get_translated_question()}"

# Move the receiver function below the FAQ model
@receiver(pre_save, sender=FAQ)
def auto_translate_faq(sender, instance, **kwargs):
    if not instance.question_hi:
        instance.question_hi = translate_text(instance.question, 'hi')
    if not instance.question_bn:
        instance.question_bn = translate_text(instance.question, 'bn')