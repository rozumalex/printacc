from rest_framework import generics
from rest_framework.response import Response

from ..models import Plotter, Clients
from ..serializers import PlottersSerializer


class PlottersListView(generics.ListCreateAPIView):
    queryset = Plotter.objects.all()
    serializer_class = PlottersSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.is_dealer:
            queryset = self.get_queryset().filter(dealer__in=user.id)
        elif user.is_admin:
            queryset = self.get_queryset().all()
        else:
            dealers = Clients.objects.filter(user=user.id).values('dealer')
            queryset = self.get_queryset().filter(dealer__in=dealers)
        context = {'request': request}
        serializer = PlottersSerializer(queryset, many=True, context=context)
        return Response(serializer.data)


class PlottersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plotter.objects.all()
    serializer_class = PlottersSerializer
