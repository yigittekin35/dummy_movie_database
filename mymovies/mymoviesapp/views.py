from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_movies(request):
    movies = [
    {"title": "The Shawshank Redemption", "rank": 9.3},
    {"title": "The Godfather", "rank": 9.2},
    {"title": "The Dark Knight", "rank": 9.0},
    {"title": "Pulp Fiction", "rank": 8.9},
    {"title": "Schindler's List", "rank": 8.9},
    {"title": "The Lord of the Rings: The Return of the King", "rank": 8.9},
    {"title": "Forrest Gump", "rank": 8.8},
    {"title": "Fight Club", "rank": 8.8},
    {"title": "Inception", "rank": 8.7},
    {"title": "The Matrix", "rank": 8.7},
    {"title": "The Silence of the Lambs", "rank": 8.6},
    {"title": "The Usual Suspects", "rank": 8.6},
    {"title": "Gladiator", "rank": 8.5},
    {"title": "Se7en", "rank": 8.6},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "rank": 8.8},
    {"title": "Goodfellas", "rank": 8.7},
    {"title": "Saving Private Ryan", "rank": 8.6},
    {"title": "The Shawshank Redemption", "rank": 9.3},
    {"title": "Schindler's List", "rank": 8.9},
    {"title": "The Godfather: Part II", "rank": 9.0},
    {"title": "The Lord of the Rings: The Two Towers", "rank": 8.7},
    {"title": "The Matrix", "rank": 8.7},
    {"title": "The Dark Knight", "rank": 9.0},
    {"title": "The Shawshank Redemption", "rank": 9.3},
    {"title": "Pulp Fiction", "rank": 8.9},
    {"title": "The Godfather", "rank": 9.2},
    {"title": "The Lord of the Rings: The Return of the King", "rank": 8.9},
    {"title": "Forrest Gump", "rank": 8.8},
    {"title": "Fight Club", "rank": 8.8},
    {"title": "Inception", "rank": 8.7},
    {"title": "Schindler's List", "rank": 8.9},
    {"title": "The Matrix", "rank": 8.7},
    {"title": "The Silence of the Lambs", "rank": 8.6},
    {"title": "The Usual Suspects", "rank": 8.6},
    {"title": "Gladiator", "rank": 8.5},
    {"title": "Se7en", "rank": 8.6},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "rank": 8.8},
    {"title": "Goodfellas", "rank": 8.7},
    {"title": "Saving Private Ryan", "rank": 8.6}
]
   
    return Response(movies)
