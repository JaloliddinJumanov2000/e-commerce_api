from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from store.models import Category
from store.serializers import CategorySerializer
@api_view(['GET', 'POST'])
def category_list_or_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
