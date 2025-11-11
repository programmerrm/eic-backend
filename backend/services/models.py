####################################################
"""
SERVICES MODELS HERE.
"""
####################################################
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from utils.validate_image_size import VALIDATE_IMAGE_SIZE
from utils.validate_image_extension import VALIDATE_IMAGE_EXTENSION

# CREATE MODELS HERE.

# ========== SERVICE PAGE TOP BAR ============
class ServicePageTopBar(models.Model):
    title = models.CharField(
        max_length=280,
        verbose_name=_('Title'),
        help_text=_('Enter your service page top bar title...')
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Enter your service page top bar description...'),
    )

    class Meta:
        verbose_name = _('Service Page Top Bar')
        verbose_name_plural = _('Service Page Top Bar')

    def __str__(self):
        return f"Service page top bar title is {self.title[:50]}"

class Service(models.Model):
    image = models.ImageField(
        upload_to=_('services'),
        validators=[VALIDATE_IMAGE_EXTENSION, VALIDATE_IMAGE_SIZE],
        verbose_name=_('Image'),
        help_text=_('Upload your service image...'),
    )
    title = models.CharField(
        unique=True,
        max_length=280,
        validators=[MinLengthValidator(1)],
        verbose_name=_('Title'),
        help_text=_('Enter your service title...'),
    )
    slug = models.SlugField(
        unique=True,
        max_length=280,
        editable=False,
        verbose_name=_('Slug'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Enter your service description...'),
    )

    def __str__(self):
        return f"Service title : {self.title[:50]}"

class ServiceItemMain(models.Model):
    normal_title = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Normal Title'),
        help_text=_('Enter your service main normal title...'),
    )
    span_title = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Span Title'),
        help_text=_('Enter your service main normal span title...'),
    )

    def __str__(self):
        return f"Service item main infomation added."

class ServiceItem(models.Model):
    image = models.ImageField(
        upload_to='services',
        validators=[VALIDATE_IMAGE_EXTENSION, VALIDATE_IMAGE_SIZE],
        verbose_name=_('Image'),
        help_text=_('Upload your service item image...'),
    )
    title = models.CharField(
        max_length=280,
        validators=[MinLengthValidator(1)],
        verbose_name=_('Title'),
        help_text=_('Enter your service title...'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description'),
        help_text=_('Enter your service description...'),
    )

    def __str__(self):
        return f"Service item title : {self.title[:50]}"

class Faq(models.Model):
    title = models.CharField(
        max_length=280,
        validators=[MinLengthValidator(1)],
        verbose_name=_('Title'),
        help_text=_('Enter your faq title...'),
    )
    image = models.ImageField(
        upload_to=_('faq/'),
        validators=[VALIDATE_IMAGE_EXTENSION, VALIDATE_IMAGE_SIZE],
        verbose_name=_('Image'),
        help_text=_('Upload your faq image...'),
    )

    def __str__(self):
        return f"Faq infomation added."

class FaqItem(models.Model):
    faq = models.ForeignKey(
        Faq,
        related_name='faq_items',
        on_delete=models.CASCADE,
        verbose_name=_('Faq'),
        help_text=_('Select the FAQ this item belongs to...'),
    )
    question = models.CharField(
        unique=True,
        max_length=280,
        validators=[MinLengthValidator(1)],
        verbose_name=_('Question'),
        help_text=_('Enter your faq item question...'),
    )
    answer = models.TextField(
        unique=True,
        verbose_name=_('Answer'),
        help_text=_('Enter your faq item answer...'),
    )

    def __str__(self):
        return f"Faq item infomation added."
