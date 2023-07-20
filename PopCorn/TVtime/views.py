from django.shortcuts import render
from .models import Movies
from .serializer import Movieserializer,MovieModelSer,UserSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import status,permissions,authentication
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from .models import Movies,UserProfile
from .serializer import MovieSerializer,UserProfileSerializer
from tmdbv3api import TMDb
from tmdbv3api import Movie
from imdb import IMDb
from rest_framework.decorators import action



# from rest_framework.decorators import action

class UserReg(APIView):
    def post(self,req,*args,**kwargs):
        ser=UserSerializer(data=req.data)
        data={}
        if ser.is_valid():
            account=ser.save()
            data['response']='Registration Completed Successfully'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=ser.errors
        return Response(data)
        

# Create your views here.
class MoviesApiMV(ModelViewSet):
    serializer_class=MovieModelSer
    queryset=Movies.objects.all()
    model=Movies
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]

    # @action(detail=True,methods=["post"])
    # def add_reviews(self,req,*args,**kwargs):
    #     id =kwargs.get("pk")
    #     mv=Movies.objects.get(id=id)
    #     user=req.user
    #     ser=ReviewSerializer(data=req.data,context={"user":user,"movie":mv})
    #     if ser.is_valid():
    #         ser.save()
    #         return Response ({"msg":"Added"})
    #     else:
    #         return Response({"MSG":ser.erros},status=status.HTTP_100_CONTINUE)
        
    # @action(detail=True,methods=["get"])   
    # def get_reviews(self,req,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     try:
    #         mv=Movies.objects.get(id=id)
    #         rv=Review.objects.filter(movie=mv)
    #         dser=ReviewSerializer(rv,many=True)
    #         return Response(data=dser.data)
    #     except:
    #         return Response({"Message":"Invalid ID"},status=status.HTTP_400_BAD_REQUEST)
        


# views.py


class MovieList(APIView):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]
    def get_user_data(self, user):
        user_data = {
            "username": user.username,
            "email": user.email,
            # Add other fields from the User model as needed
        }
        return user_data
    def get(self, request):
        tmdb = TMDb()
        tmdb.api_key = 'dee4eee45142faa55cf89a2f052e57e6'
        mv = Movie()
        pplr = mv.popular()
        path = "https://www.themoviedb.org/t/p/original"
        mv_list = []

        for i in pplr:
            mv_dict = {
                "title": i.title,
                "bgimg": path + i.backdrop_path,
                "poster": path + i.poster_path,
                "rate": i.vote_average,
                "overview": i.overview,
                "release_date": i.release_date,
              
            }
            mv_list.append(mv_dict)

        user = request.user
        if user.is_authenticated:
            user_data = self.get_user_data(user)
        else:
            user_data = None

        response_data = {
            "user": user_data,
            "movies": mv_list,
        }

        return Response(response_data, status=status.HTTP_200_OK)

class MovieSearch(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        tmdb = TMDb()
        tmdb.api_key = 'dee4eee45142faa55cf89a2f052e57e6'

        query = request.data.get('query')  # Use request.data instead of request.POST
        ia = IMDb()
        movies = ia.search_movie(query)

        film = None
        if movies:
            movie = movies[0]
            ia.update(movie, ['main', 'plot'])

            poster_url = movie.get('full-size cover url') or movie.get('cover url')

            search = Movie().search(query)
            id = search[0].id
            movie_details = Movie().details(id)

            vd = movie_details.trailers.youtube
            link = None
            for i in vd:
                if (i['type'] == "Trailer") and ("official" or "Trailer" in i['name']):
                    link = i['source']
                    trailer = f"https://www.youtube.com/watch?v={i['source']}"
                    break
            if link is None:
                trailer = "https://www.youtube.com/watch?v=aDm5WZ3QiIE&ab"

            film = {
                'movie_id': movie.get('imdbID'),
                'title': movie.get('title'),
                'year': movie.get('year'),
                'genres': movie.get('genres', []),
                'cast': movie.get('cast', []),
                'plot': movie.get('plot'),
                'poster_url': poster_url,
                'runtimes': movie.get('runtimes'),
                'languages': movie.get('languages'),
                'airdate': movie.get('original air date'),
                'rating': movie.get('rating'),
                'kind': movie.get('kind'),
                'trailer': trailer
            }

        return Response({'film': film})
    
        


class UserCreation(APIView):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]

    def post(self, req, *args, **kwargs):
        req.data['user'] = req.user.id  # Set the user field to the logged-in user's ID
        ser = UserProfileSerializer(data=req.data)
        if ser.is_valid():
            ser.save()
            return Response({"Message": "Registration Completed"})
        else:
            return Response({"Message": "Registration Failed"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_edn(self, request):
        # Get the UserProfile object for the logged-in user
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found."}, status=404)

        # Serialize the UserProfile object and return the data
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)
    
