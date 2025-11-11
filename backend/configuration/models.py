####################################################
"""
CONFIGURATION MODELS HERE.
"""
####################################################
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from utils.validate_image_size import VALIDATE_IMAGE_SIZE

# CREATE MODELS HERE.

# ================ FAVICON MODEL ==============
class Favicon(models.Model):
    icon = models.ImageField(
        null=True,
        blank=True,
        validators=[VALIDATE_IMAGE_SIZE],
        upload_to=_('favicon/'),
        verbose_name=_('Favicon'),
        help_text=_('Upload your website favicon...'),
    )

    class Meta:
        verbose_name = _('Favicon')
        verbose_name_plural = _('Favicon')

    def __str__(self):
        return f"Favicon"

# =============== LOGO MODEL ==================
class Logo(models.Model):
    image = models.ImageField(
        null=True,
        blank=True,
        validators=[VALIDATE_IMAGE_SIZE],
        upload_to=_('logo/'),
        verbose_name=_('Logo'),
        help_text=_('Upload your website logo...'),
    )
    alt_text = models.CharField(
        null=True,
        blank=True,
        max_length=180,
        validators=[MinLengthValidator(3)],
        verbose_name=_('Logo ALT Text'),
        help_text=_('Enter your logo alt text...'),
    )

    class Meta:
        verbose_name = _('Logo')
        verbose_name_plural = _('Logo')
        
    def __str__(self):
        return f"Logo"

# ============== COPY RIGHT ==================
class CopyRight(models.Model):
    text = models.CharField(
        null=True,
        blank=True,
        max_length=280,
        validators=[MinLengthValidator(3)],
        verbose_name=_('Copy Right Text'),
        help_text=_('Enter your website copy right text...'),
    )

    class Meta:
        verbose_name = _('Copy-Right')
        verbose_name_plural = _('Copy-Right')

    def __str__(self):
        return f"{self.text}"

# ============= SOCIAL LINK ==================
class SocialLink(models.Model):
    name = models.CharField(
        null=True,
        blank=True,
        max_length=180,
        unique=True,
        validators=[MinLengthValidator(1)],
        verbose_name=_('Socail Link Name'),
        help_text=_('Enter your website socail link name...')
    )
    url = models.URLField(
        null=True,
        blank=True,
        max_length=280,
        unique=True,
        validators=[MinLengthValidator(1)],
        verbose_name=_('Socail Link URL'),
        help_text=_('Enter your website socail link url...')
    )

    class Meta:
        verbose_name = _('Social-Link')
        verbose_name_plural = _('Social-Link')

    def __str__(self):
        return f"Socail link added"

# ============= PAYMENT LOGO ==================
class ContactInfo(models.Model):
    number_1 = models.IntegerField(verbose_name=_('Number 1'))
    number_2 = models.IntegerField(verbose_name=_('Number 2'))
    email = models.EmailField(verbose_name=_('Email Address'))

    def __str__(self):
        return f"Contact info"
    