#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 19:25:24 2016
@author: pkshreeman
The image sources are from imdb, google, and youtube.

"""
import fresh_tomatoes
import media

movie1 = media.Movie(
                     "Inception",
                     "A thief, who steals corporate secrets through use of "
                     "dreamsharing technology, is given the inverse task of "
                     "planting an idea into the mind of a CEO",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1._SY209_CR0,0,140,209_.jpg",  # noqa
                     "https://www.youtube.com/watch?v=8hP9D6kZseM")

movie2 = media.Movie(
                     "Slumdog Millionaire",
                     "A Mumbai teen reflects on his upbringing in the slums "
                     "when he is accused of cheating on the Indian Version of "
                     "'Who Wants to be a Millionaire?'",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NTA5NzI0N15BMl5BanBnXkFtZTcwMjUxMjYxMg@@._V1._SY209_CR0,0,140,209_.jpg",  # noqa
                     "https://www.youtube.com/watch?v=AIzbwV7on6Q")

movie3 = media.Movie(
                    "Good Will Hunting",
                    "Will Hunting, a janitor at M.I.T., has a gift for "
                    "mathematics, but needs help from a psychologist to find "
                    "direction in his life.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BOTI0MzcxMTYtZDVkMy00NjY1LTgyMTYtZmUxN2M3NmQ2NWJhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1._SX140_CR0,0,140,209_.jpg",  # noqa
                    "https://www.youtube.com/watch?v=QSMvyuEeIyw")

movie4 = media.Movie(
                     "Mr. Nobody",
                     "A boy stands on a station platform as a train is about"
                     " to leave. Should he go with his mother or stay with his"
                     " father? Infinite possibilities arise from this "
                     "decision. As long as he doesn't choose, anything is "
                     "possible.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4ODkzMDQ3Nl5BMl5BanBnXkFtZTgwNTEwMTkxMDE@._V1._SY209_CR0,0,140,209_.jpg",  # noqa
                     "https://www.youtube.com/watch?v=mpi0qsp3v_w")

movie5 = media.Movie(
                     "Equilibrium",
                     "In a facist future where all forms of feelings are"
                     " illegal, a man in charge of enforcing the law rises to"
                     " overthrow the system",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzMzA1OTI3N15BMl5BanBnXkFtZTYwMzUyMDg5._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                     "https://www.youtube.com/watch?v=raleKODYeg0",)

movie6 = media.Movie(
                     "How to Train Your Dragon",
                     "A hapless young Viking who aspires to hunt dragons "
                     "becomes the unlikely friend of a young dragon himself, "
                     "and learns there may be more to the creatures than he"
                     " assumed.",
                     "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQXN1SHpyRdsyk-c6M8nKtyHjco31sXqn8zC-WuOnBAf-jyLmDcSBzr9PoCDK3L5LDTR6am",  # noqa
                     "https://www.youtube.com/watch?v=oKiYuIsPxYk")

movie7 = media.Movie(
                     "The Mask",
                     "'The Mask' stars Jim Carrey as mild-mannered bank clerk "
                     "Stanley Ipkiss, who discovers a mysterious ancient mask "
                     "that brings his innermost desires to wild, "
                     "screaming life!",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/The_Mask_%28film%29_poster.jpg/220px-The_Mask_%28film%29_poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=hOqVRwGVUkA")

movie8 = media.Movie(
                     "Wall-e",
                     "In the distant future, a small waste-collecting robot "
                     "inadvertently embarks on a space journey that will "
                     "ultimately decide the fate of mankind. ",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                     "https://www.youtube.com/watch?v=alIq_wG9FNk")

movie9 = media.Movie(
                     "Pay It Forward",
                     "A young boy attempts to make the world a better place "
                     "after his teacher gives him that chance.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BNjI3ODI5NDEwMl5BMl5BanBnXkFtZTYwNDYyMjU3._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                     "https://www.youtube.com/watch?v=qfW0wCV9iFI")

movie10 = media.Movie(
                      "Yes Man",
                      "A guy challenges himself to say 'yes' to everything "
                      "for an entire year.",
                      "https://i.ytimg.com/vi_webp/z7gt5bYo5Io/movieposter.webp",  # noqa
                      "https://www.youtube.com/watch?v=M3ar1tBj_Zk")

movies = [
    movie1,
    movie2,
    movie3,
    movie4,
    movie5,
    movie6,
    movie7,
    movie8,
    movie9,
    movie10]


fresh_tomatoes.open_movies_page(movies)  # Creates and open the html file
