from django.shortcuts import render
# Create your views here.


from service.models import Element, Commodity, Chemical_composition
from service.serializers import ElementSer,CommoditySer, ChemicalSer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ElementList(APIView):
    """     List all element, or create a new element.     """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        elements = Element.objects.all()
        serializer = ElementSer(elements, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ElementSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ElementDetail(APIView):
    """     Retrieve, update or delete a element instance.     """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self, pk):
        try:
            return Element.objects.get(pk=pk)
        except Element.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        elements = self.get_object(pk)
        serializer = ElementSer(elements)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        elements = self.get_object(pk)
        serializer = ElementSer(elements, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        elements = self.get_object(pk)
        if elements:
            elements.active='N'
            elements.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommodityList(APIView):
    """     List all Commodity, or create a new Commodity.     """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        commodity = Commodity.objects.all()
        serializer = CommoditySer(commodity, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommoditySer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommodityDetail(APIView):
    """     Retrieve, update or delete a Commodity instance.     """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self, pk):
        try:
            return Commodity.objects.get(pk=pk)
        except Element.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        commodity = self.get_object(pk)
        serializer = CommoditySer(commodity)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        commodity = self.get_object(pk)
        serializer = CommoditySer(commodity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        commodity = self.get_object(pk)
        if commodity:
            commodity.active='N'
            commodity.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Chemical_composition_List(APIView):
    """     List all Commodity, or create a new Commodity.     """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        chemical = Chemical_composition.objects.all()
        serializer = ChemicalSer(chemical, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChemicalSer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Chemical_composition_Detail(APIView):
    """     Retrieve, update or delete a Commodity instance.     """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self, pk):
        try:
            return Chemical_composition.objects.get(pk=pk)
        except Element.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        chemical = self.get_object(pk)
        serializer = CommoditySer(chemical)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        chemical = self.get_object(pk)
        serializer = ChemicalSer(chemical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        chemical = self.get_object(pk)
        if chemical:
            chemical.active='N'
            chemical.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

