import requests
import random

class Movie:

    def __init__(self,movie_name):
        self.movie_name = movie_name
        self.imdbID = None
        self.omdb_querystring = {"apikey":"6be91fef"}
        self.tmdb_querystring = {"api_key":"d36fdddf9a3b56ff8f3875bb507e06ef","language":"en-US"}

    def get_imdbID(self):
        url = "http://www.omdbapi.com/"
        self.omdb_querystring["t"] = self.movie_name
        response = requests.request("GET", url,params=self.omdb_querystring)
        response = response.json()
        self.imdbID = response["imdbID"]

        return response["imdbID"]

    def get_details(self):
        if self.imdbID != None:
            imdbID = self.imdbID
        else:   
            imdbID = self.get_imdbID()
        url = "https://api.themoviedb.org/3/movie/"
        url = url+imdbID
        response = requests.request("GET", url,params=self.tmdb_querystring)
        response = response.json()
        overview = response["overview"]
        released_date = response["release_date"]

        return (overview,released_date)


    def get_reviews(self):
        if self.imdbID != None:
            imdbID = self.imdbID
        else:   
            imdbID = self.get_imdbID()
        url = "https://api.themoviedb.org/3/movie/"
        url = url+imdbID+"/reviews"
        response = requests.request("GET", url,params=self.tmdb_querystring)
        response = response.json()

        results = response["results"]
        gender = ["Male","Female"]
        age = ["Teen","Young","Old"]
        reviews=[]
        user=[]        
        for i in range(len(results)):
            user.append([results[i]["author"],gender[random.randint(0,1)],age[random.randint(0,2)]])
            reviews.append(results[i]["content"])
        
        return (user,reviews)

    def get_similarMovies(self):
        if self.imdbID != None:
            imdbID = self.imdbID
        else:   
            imdbID = self.get_imdbID()
        url = "https://api.themoviedb.org/3/movie/"
        url = url+imdbID+"/similar"
        response = requests.request("GET", url,params=self.tmdb_querystring)
        response = response.json()

        results = response["results"]
        similar_movies=[]
        for i in range(len(results)):
            similar_movies.append(results[i]["title"])

        return similar_movies
    



        