from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forex import forex_rate

class CurrencyView(APIView):
    def get(self, request):
        try:
            base_cur = self.request.query_params['from']
            dest_cur = self.request.query_params['to']
            multiplier = self.request.query_params['value']

            rate = forex_rate(base_cur, dest_cur, multiplier)

            context = {
                'rate': rate,
            }
            return Response(context)

        except MultiValueDictKeyError:
            return Response({'error': 'One of arguments not passed'}, status=status.HTTP_400_BAD_REQUEST)
