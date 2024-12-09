from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item, Case, Endpoint, Threat
from .serializers import ItemSerializer, CaseSerializer, EndpointSerializer, ThreatSerializer

class ItemList(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaseList(APIView):
    def get(self, request):
        cases = Case.objects.all()
        serializer = CaseSerializer(cases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaseList(APIView):
    def get(self, request):
        cases = Case.objects.all()
        serializer = CaseSerializer(cases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaseDetail(APIView):
    def get(self, request, pk):
        try:
            case = Case.objects.get(pk=pk)
        except Case.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CaseSerializer(case)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            case = Case.objects.get(pk=pk)
        except Case.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CaseSerializer(case, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            case = Case.objects.get(pk=pk)
        except Case.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        case.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EndpointList(APIView):
    def get(self, request):
        endpoints = Endpoint.objects.all()
        serializer = EndpointSerializer(endpoints, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EndpointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EndpointDetail(APIView):
    def get(self, request, pk):
        try:
            endpoint = Endpoint.objects.get(pk=pk)
        except Endpoint.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EndpointSerializer(endpoint)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            endpoint = Endpoint.objects.get(pk=pk)
        except Endpoint.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EndpointSerializer(endpoint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            endpoint = Endpoint.objects.get(pk=pk)
        except Endpoint.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        endpoint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ThreatList(APIView):
    def get(self, request):
        threats = Threat.objects.all()
        serializer = ThreatSerializer(threats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ThreatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ThreatDetail(APIView):
    def get(self, request, pk):
        try:
            threat = Threat.objects.get(pk=pk)
        except Threat.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ThreatSerializer(threat)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            threat = Threat.objects.get(pk=pk)
        except Threat.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ThreatSerializer(threat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            threat = Threat.objects.get(pk=pk)
        except Threat.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        threat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)