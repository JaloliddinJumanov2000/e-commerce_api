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

@api_view(['GET', 'PUT', 'DELETE'])
def category_retrieve_update_or_delete(request,pk):
     try:
         category = Category.objects.get(id=pk)
     except Category.DoesNotExist:
         return Response({"message": "Not Found!"})

     if request.method == 'GET':
         serializer = CategorySerializer(category)
         return Response(serializer.data)

     elif request.method == 'PUT':
         serializer = CategorySerializer(category, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors)

     elif request.method == 'DELETE':
         category.delete()
         return Response({"message": "Category deleted!"})

     return None






