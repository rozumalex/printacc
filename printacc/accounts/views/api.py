from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response

from rest_framework.permissions import AllowAny


class API(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return Response({
                'openapi': reverse("openapi", request=request),
                'signup': reverse("accounts:signup", request=request),
                'login': reverse("accounts:login", request=request),
            })
        else:
            result = {
                'plotters': reverse("accounts:plotters-list", request=request),
            }
            if request.user.is_dealer:
                result.update({'users': reverse("accounts:users-list",
                                                request=request),
                               'plotters': reverse("accounts:plotters-list",
                                                   request=request)})
            if request.user.is_admin:
                result.update({'dealers': reverse("accounts:dealers-list",
                                                  request=request)})
            result.update({'openapi': reverse("openapi", request=request)})
            return Response(result)
