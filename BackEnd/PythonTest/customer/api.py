from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class UserList(APIView):
    def get(self, request):
        model = Cust.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)


class UserAdd(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_user(self, employee_id):
        try:
            model = Cust.objects.get(id=employee_id)
            return model
        except Cust.DoesNotExist:
            return Response(f'User with {employee_id} is Not Found', status=status.HTTP_404_NOT_FOUND)

    def get(self, request, employee_id):
        try:
            model = Cust.objects.get(id=employee_id)
        except Cust.DoesNotExist:
            return Response(f'User with {employee_id} is Not Found', status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(model)
        return Response(serializer.data)

    def delete(self, request, employee_id):
        model = self.get_user(employee_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserEdit(APIView):
    def put(self, request, employee_id):
        try:
            model = Cust.objects.get(id=employee_id)
        except Cust.DoesNotExist:
            return Response(f'User with {employee_id} is Not Found', status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
