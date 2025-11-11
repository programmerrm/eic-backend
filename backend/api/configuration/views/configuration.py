######################################################
"""
CONFIGURATION ALL VIEWS
"""
######################################################
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from configuration.models import (
    Favicon,
    Logo,
    CopyRight,
    SocialLink,
    ContactInfo,
)
from api.configuration.serializers.configuration import (
    FaviconSerializer,
    LogoSerializer,
    CopyRightSerializer,
    SocialLinkSerializer,
    ContactInfoSerializer,
)

# ======== FAVICON VIEW =========== 
class FaviconViewSet(viewsets.ModelViewSet):
    serializer_class = FaviconSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            queryset = Favicon.objects.first()
            if queryset is None:
                return Response({"message": "No favicon records found."}, status=status.HTTP_404_NOT_FOUND)
            return Response(FaviconSerializer(queryset).data, status=status.HTTP_200_OK)
        except Favicon.DoesNotExist:
            return Response({"message": "No favicon records found."}, status=status.HTTP_404_NOT_FOUND)

# ======== LOGO VIEW =========== 
class LogoViewSet(viewsets.ModelViewSet):
    serializer_class = LogoSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            queryset = Logo.objects.first()
            if queryset is None:
                return Response({
                    "success": True,
                    "message": "No logo records found.",
                    "data": [],
                }, status=status.HTTP_200_OK)
            return Response({
                "success": True,
                "message": "", 
                "data": LogoSerializer(queryset).data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ======== COPY RIGHT VIEW =========== 
class CopyRightViewSet(viewsets.ModelViewSet):
    serializer_class = CopyRightSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            queryset = CopyRight.objects.first()
            if queryset is None:
                return Response({
                    "success": True,
                    "message": "No logo records found.",
                    "data": [],
                }, status=status.HTTP_200_OK)
            return Response({
                "success": True,
                "message": "", 
                "data": CopyRightSerializer(queryset).data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ======== SOCIAL LINK VIEW =========== 
class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        if not self.queryset.exists():
            return Response({"message": "No social link records found."}, status=status.HTTP_404_NOT_FOUND)
        return super().list(request, *args, **kwargs)

# ======== CONTACT INFO VIEW =========== 
class ContactInfoViewSet(viewsets.ModelViewSet):
    serializer_class = ContactInfoSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAdminUser()]

    def list(self, request, *args, **kwargs):
        try:
            queryset = ContactInfo.objects.first()
            if queryset is None:
                return Response({
                    "success": True,
                    "message": "No contact info records found.",
                    "data": [],
                }, status=status.HTTP_200_OK)
            return Response({
                "success": True,
                "message": "", 
                "data": ContactInfoSerializer(queryset).data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
