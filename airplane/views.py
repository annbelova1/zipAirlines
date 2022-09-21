from rest_framework import status, viewsets
from rest_framework.response import Response

from airplane.models import Airplane
from .serializers import AirplaneSerializer
from django.conf import settings


class AirlineApiView(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def create(self, request, *args, **kwargs):
        """
            Create a list of model instances if a list is provided or a
            single model instance otherwise.
        """
        try:
            data = request.data
            count = len(data) if isinstance(data, list) else 1

            if count + Airplane.objects.filter(user_id=request.user.id).count() > settings.AIRPLANES_LIMIT:
                raise ValueError(f'You can create only {settings.AIRPLANES_LIMIT} planes')
            if isinstance(data, list):
                serializer = self.get_serializer(data=data, many=True)
            else:
                serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)

            serializer.save(user_id=self.request.user.id)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except (TypeError, ValueError) as error:
            return Response({'error': f'{error.__class__.__name__}: {error}'}, status=status.HTTP_400_BAD_REQUEST)