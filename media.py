#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 19:22:08 2016

@author: pkshreeman
"""
import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
