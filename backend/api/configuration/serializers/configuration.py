# ======================================
"""
CONFIGURATION ALL SERIALIZERS
"""
# ======================================
from rest_framework import serializers
from configuration.models import (
    Favicon,
    Logo,
    CopyRight,
    SocialLink,
    ContactInfo,
)

# ============ FAVICON SERIALIZER ===============
class FaviconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favicon
        fields = '__all__'

# ============ LOGO SERIALIZER ===============
class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'

# ============ COPYRIGHT SERIALIZER ===============
class CopyRightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopyRight
        fields = '__all__'

# ============ SOCIAL LINK SERIALIZER ===============
class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'

# ============== CONTACT INFO ==================
class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'
