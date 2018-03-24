# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render
from django.shortcuts import render,redirect

from movie import Movie
from analyze import SentimentAnalyzer

# homepage of the website
class Index(generic.View):
    template_name = 'movierating/index.html'

    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        movie_name = request.POST["movie"]
        request.session['movie_name'] = movie_name
        return redirect('details')


# details page of the website
class Details(generic.View):
    template_name = 'movierating/details.html'

    def get(self,request):
        movie_name = request.session.get('movie_name')

        # calling api for gathring reviews
        movie = Movie(movie_name)
        overview,released_date = movie.get_details()
        similar_movies = movie.get_similarMovies()

        #  calling the analyzer class
        analyzer = SentimentAnalyzer(movie)
        label = analyzer.get_label()
        pos_review,neg_review = analyzer.average_sentiment(label)

        # calling the graph class
        

        movie = {'movie_name':movie_name,'similar_movies':similar_movies}
        details = {'overview':overview,'released_date':released_date}
        review = {'pos_review':int(pos_review),'neg_review':int(neg_review)}

        return render(request,self.template_name,{'movie':movie,'details':details,'review':review})