from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, BookSerializer, MarkAsReadSerializer
from .models import Book
from rest_framework import generics, viewsets
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'read_as']
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user.id)

# Class based view to Get User Details using Token Authentication
class MarkAsReadAPI(APIView):
  permission_classes = (IsAuthenticated,)
  def post(self, request):
    serializer = MarkAsReadSerializer(data=request.data)
    if serializer.is_valid():
      data = serializer.data
      try:
        book_data = Book.objects.get(id=data["book_id"])
        book_data.read_as = data["read_as"]
        book_data.save()
        return Response(
          {
            "status": "success", 
            "data": "Record update successfully"
          },
           status=status.HTTP_200_OK
        )
      except Book.DoesNotExist:
        return Response(
          {
            "status": "error", 
            "data": "data with given book_id not exists"
          }, 
          status=status.HTTP_400_BAD_REQUEST
        )
    else:
      return Response(
        {
          "status": "error", 
          "data": serializer.errors
        }, 
        status=status.HTTP_400_BAD_REQUEST
      )

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
