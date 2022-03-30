from watchlist.models import Movie
from watchlist.api.serializers import MovieSerlializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
 
@api_view(['GET','POST'])  
def movie_list(request): 
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerlializer(movies,many=True )
        return Response(serializer.data)
    if request.method == "POST":
        serializer = MovieSerlializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.error)
            
#  this did not worked
@api_view(['GET','PUT','DELETE '])
def movie_detail(request,pk): 
    if request.method == "GET":
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerlializer(movie) 
        return Response(serializer.data)
    if request.method == "PUT":
        movie = Movie.objects.get(pk=pk)
        # the object needs to be selected before update otherwise new instance will be created
        serializer = MovieSerlializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        else: 
            return Response(serializer.error)
    if request.method == "DELETE":
        movie = Movie.objects.get(pk=pk)
        # the object needs to be selected before update otherwise new instance will be created
        movie.delete() 
        return Response()
    