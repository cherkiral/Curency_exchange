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

            response = forex_rate(base_cur, dest_cur)

            if response.status_code == 200:
                json_response = response.json().get('data')
                if not json_response:
                    return Response({'error': 'apidown'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    if multiplier.isnumeric():
                        rate = float(json_response[dest_cur]['value']) * float(multiplier)
                    else:
                        return Response({'error': 'value should be an integer'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'errors': response.json().get('errors')}, status=status.HTTP_400_BAD_REQUEST)

            context = {
                'rate': rate,
            }
            return Response(context)

        except MultiValueDictKeyError:
            return Response({'error': 'One of arguments not passed'}, status=status.HTTP_400_BAD_REQUEST)
