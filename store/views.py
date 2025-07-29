from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.models import Category
from store.serializers import StoreSerializer  # ✅ Bu joy muhim!

@api_view(['GET'])
def home(request):
    categories = Category.objects.all()
    serializer = StoreSerializer(categories, many=True)  # ✅ To‘g‘ri serializer nomi
    return Response(serializer.data)
