from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from ..models import Pattern
from ..serializers import PatternsSerializer


class PatternsListView(generics.ListCreateAPIView):
    lookup_field = 'pattern_id'
    serializer_class = PatternsSerializer
    extra_kwargs = {'url': {'view_name': 'accounts:patterns-list'}}

    def get_queryset(self):
        return Pattern.objects.filter(plotter_id=self.kwargs.get('pk'))

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        context = {'request': request}
        serializer = PatternsSerializer(queryset, many=True, context=context)
        return Response(serializer.data)


class PatternsDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pattern_id'
    queryset = Pattern.objects.all()
    serializer_class = PatternsSerializer
    extra_kwargs = {'url': {'view_name': 'accounts:patterns-detail'}}

    def get_queryset(self, request, *args, **kwargs):
        context = {'request': request}
        print('==================================================')
        queryset = self.queryset
        queryset = queryset.filter(plotter_id=self.kwargs.get('pk'))
        print(queryset)
        print('==================================================')
        serializer = PatternsSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def get_object(self):
        queryset = self.get_queryset()

        print('==================================================')
        obj = get_object_or_404(queryset, self.lookup_field)
        print(obj)
        print('==================================================')
        return obj

    # def get(self, request, *args, **kwargs):
    #
    #     return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print('==================================================')
        instance = self.get_object()
        print(instance)
        print('==================================================')
        context = {'request': request}
        serializer = self.get_serializer(instance, context=context)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        print('==================================================')
        print('get')
        print('==================================================')
        return self.retrieve(request, *args, **kwargs)
#
# class PlotterUseView(PatchOnlyMixin, UpdateModelMixin,
#                            generics.GenericAPIView):
#     queryset = Plotter.objects.all()
#     serializer_class = UsePlotterSerializer
#
#     @transaction.atomic
#     def patch(self, request, *args, **kwargs):
#         plotter = self.get_object()
#         dealer = plotter.dealer
#         client = Clients.objects.get(dealer=dealer.id, user=request.user.id)
#         if client.limit > 0:
#             Statistics(user=request.user, pattern=dealer, plotter=plotter)
#             client.limit -= 1
#             client.save()
#             return Response({'used': True, 'limit': client.limit})
#         else:
#             return Response({'used': False, 'limit': client.limit})
#
