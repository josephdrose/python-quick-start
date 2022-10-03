from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from decimal import Decimal

from sample.models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['post'])
    def apply_taxes(self, request, pk=None):

        order = Order.objects.get(pk=pk)
        order.total *= Decimal(1.07)
        order.save()

        return Response({'status': 'done'})


