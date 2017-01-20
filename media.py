#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 19:22:08 2016

@author: pkshreeman
"""
import webbrowser


class Movie():
    '''
    The class Movie is created to iterate through tuples of selected movies
    identified in media-center.py.

    Args:
        movie_title:  Title of the selected movie
        movie_storyline: The summary of the selected movie
        poster_image: Link to image of movie poster_image
        trailer: Youtube video of the selected movie

    show_trailer: opens the youtube movie in a new window

    Note:
        This class will be called in media-center.py


    '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
