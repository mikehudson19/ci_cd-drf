from rest_framework.response import Response
from core import settings
from rest_framework.views import APIView


class HealthApiView(APIView):
    def get(self, request):
        return Response({'api_status': 'healthy', 'db_status': 'up', 'commit': settings.GIT_COMMIT})
