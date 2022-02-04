from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from client.models import Client
from client.serializers import ClientSerializer
import csv, pandas as pd
from django.http import HttpResponse
from bill.models import Bill
from client.models import Client


@api_view(['GET', 'POST'])
def client_list(request):
    if request.method == 'GET':
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def client_download(request, pk):
        if request.method == 'GET':
            response = HttpResponse("", content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="bill_client.csv"'

            writer = csv.writer(response)
            writer.writerow(['first_name', 'last_name', 'document' ,'quantity'])

            for client in Client.objects.all():
                bills = Bill.objects.filter(client_id = pk)
                count = bills.count()
        
                row = [client.first_name, client.last_name, client.document, count]
                writer.writerow(row)

            return response

@api_view(['GET'])
def client_massive(self, request):
        if request.method == 'POST':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            file = serializer.validated_data['file']
            reader = pd.read_csv(file)
            for _,row in reader.iterrows():
                serializer_client = ClientSerializer(data=dict(row))
                serializer_client.is_valid(raise_exception=True)
                serializer_client.save()
            
            return Response({"message": "Archivo cargado correctamente."}, status=status.HTTP_201_CREATED)


