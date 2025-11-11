# ==========================================
"""
CONFIGURATION ALL ROUTES
"""
# ==========================================
from rest_framework.routers import DefaultRouter
from api.configuration.views.configuration import (
    FaviconViewSet,
    LogoViewSet,
    CopyRightViewSet,
    SocialLinkViewSet,
    ContactInfoViewSet
)

router = DefaultRouter()
router.register(r'favicon', FaviconViewSet, basename='favicon')
router.register(r'logo', LogoViewSet, basename='logo')
router.register(r'copy-right', CopyRightViewSet, basename='copy_right')
router.register(r'social-link', SocialLinkViewSet, basename='social_link')
router.register(r'contact-info', ContactInfoViewSet, basename='contact_info')

urlpatterns = router.urls
