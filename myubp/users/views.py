from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from users.permissions import UpdateOwnProfile
from users.serializers import UserProfileSerializer
from users.models import UserProfile


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    View's for a user ABM
    """

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    def get_queryset(self):
        """
        Redefined the get query. Only superuser can visualize all the user's profiles.
        """

        user = self.request.user
        if not user.is_superuser:
            return UserProfile.objects.filter(id=user.id)
        return UserProfile.objects.all()


class UserLoginApiView(ObtainAuthToken):
    """
    View for login with oauth's protocol
    """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email

        })
