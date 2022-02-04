from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from billProduct.models import BillProduct
from billProduct.serializers import BillProductSerializer


@api_view(['GET', 'POST'])
def billProduct_list(request):
    if request.method == 'GET':
        billProduct = BillProduct.objects.all()
        serializer = BillProductSerializer(billProduct, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BillProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def billProduct_detail(request, pk):
    try:
        billProduct = BillProduct.objects.get(pk=pk)
    except BillProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BillProductSerializer(billProduct)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BillProductSerializer(billProduct, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        billProduct.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)