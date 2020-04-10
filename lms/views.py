from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.db import transaction
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models.post_models import Post
from .serializers.post_serializers import PostSerializer,UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser


# @api_view(['GET', 'POST'])
class post_list(APIView):
    def get(self,request):
        if request.method == "GET":
            data = []
            data = Post.objects.all().order_by('-Init_time')
            serializer = PostSerializer(data,context={'request': request} ,many=True);

        print(serializer.data)
        return Response({'data': serializer.data })

    parser_classes = (MultiPartParser, FormParser)

    @transaction.atomic

    def post(self,request):
        if request.method == "POST":
            serializer = PostSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                if validate(request.data):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

                else:
                    print("works")




            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
class videos_post_list(APIView):

    def get(self,request):
        if request.method == "GET":
            data = []
            data = Post.objects.exclude(Video='').order_by('-Init_time')

            serializer = PostSerializer(data,context={'request': request} ,many=True);


            return Response({'data': serializer.data })

# @api_view(['GET', 'POST'])
class images_post_list(APIView):

    def get(self,request):
        if request.method == "GET":
            data = []
            data = Post.objects.exclude(Image='').order_by('-Init_time')

            serializer = PostSerializer(data,context={'request': request} ,many=True);




        return Response({'data': serializer.data })

# @api_view(['GET', 'POST'])
class docs_post_list(APIView):

    def get(sefl,request):
        if request.method == "GET":
            data = []
            data = Post.objects.exclude(Doc='').order_by('-Init_time')

            serializer = PostSerializer(data,context={'request': request} ,many=True);




        return Response({'data': serializer.data })

# @api_view(['GET', 'POST'])

class post_detail(APIView):

    def get(self,request,postId):
        if request.method == "GET":
            data = []
            data = Post.objects.filter(id=postId)
            serializer = PostSerializer(data,context={'request': request} ,many=True);

            print(serializer.data)


            return Response({'data': serializer.data })

# @api_view(['GET', 'POST'])

class search_posts(APIView):

    def get(self,request,postQuery):
        print("bleh")
        if request.method == "GET":
            data = []
            if "%20" in postQuery:
                postQuery = postQuery.replace("%20"," ")
            print(postQuery)
            data = Post.objects.filter(Name__contains=postQuery) | Post.objects.filter(Description__contains=postQuery) |  Post.objects.filter(Author__contains=postQuery)
            serializer = PostSerializer(data,context={'request': request} ,many=True);

            print(serializer.data)


            return Response({'data': serializer.data })

# @api_view(['GET', 'POST'])

def validate(serializer):


    Image_list = [None, "png", "jpg", "jpeg", "svg", "gif"]
    if 'Video' in serializer and str(serializer['Video']).split(".")[-1]  not in Image_list:
        print("1")
        return False

    Video_list = [None, "mp4", "jpg", "jpeg", "svg", "gif"]
    if 'Image' in serializer and str(serializer['Image']).split(".")[-1]  not in Image_list:
        print("2")
        return False

    Doc_list = [None, "docx","pages","py"]
    if 'Doc' in serializer and str(serializer['Doc']).split(".")[-1] not in Doc_list:
        print("3")
        return False


    if len(serializer['Name']) < 5 or len(serializer['Description']) < 5 or len(serializer['Author']) < 5:
        print("4")
        return False

    if not serializer['Name'].replace(" ","").isalnum() or not serializer['Author'].isalnum():
        print("5")
        return False
    try:
        checker = int(serializer['Name'])
        checker = int(serializer['Author'])
        checker = int(serializer['Description'])
        print("6")
        return False
    except:
        print("7")
        return True

# class login(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     def post(self,request):
#         user = auth.authenticate(username=request.data['username'],password=request.data['password'])
#         if user is not None:
#             auth.login(request, user)
#         return Response(request.data)
