from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from shiplocation.models import ShipLocation, ShipName
from shiplocation.serializers import ShipLocationSerializer, ShipSerializer


class ShipView(viewsets.ModelViewSet):
    queryset = ShipName.objects.all()
    serializer_class = ShipSerializer


class ShipLocationView(viewsets.ViewSet):
    queryset = ShipLocation.objects.all()
    serializer_class = ShipLocationSerializer

    def retrieve(self, request, pk=None):
        ship = get_object_or_404(ShipName, imo=pk)
        queryset = ship.shiplocation_set.all().order_by('-ship_date')
        serializer = ShipLocationSerializer(queryset, many=True)
        return Response(serializer.data)
