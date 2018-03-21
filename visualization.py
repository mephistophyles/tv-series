from math import floor

import matplotlib.pyplot as plt
import numpy as np

from data import *

plt.style.use('ggplot')

shows = ["The Walking Dead", "Game of Thrones", "Lost", "Breaking Bad", "The Wire"]

def unpack_show(show_name):
    seasons = len(tv[show_name].keys())
    tvcom = np.array([])
    imdbcom = np.array([])
    for i in range(1, seasons+1):
        tvcom = np.concatenate((tvcom, np.array(tv[show_name][i])))
        imdbcom = np.concatenate((imdbcom, np.array(imdb[show_name][i])))
    return tvcom, imdbcom

# Analyze
def analyze_show(show_name, tv, imdb):
    print(f"IMDB mean score for {show_name} is {np.mean(imdb)}, with a std of {np.std(imdb)}")
    print(f"TV.com mean score for {show_name} is {np.mean(tv)}, with a std of {np.std(tv)}")

# visualize
def visualize_show(show_name, tv, imdb, graph_type="scatter"):
    plt.figure(1)
    if graph_type == "scatter":
        plt.scatter(range(len(tv)), tv, color="blue")
        plt.scatter(range(len(imdb)), imdb, color="red")
    plt.xlabel("episode")
    plt.ylabel("score")
    plt.legend(["TV.com", "IMDB"])
    plt.title(show_name)

    plt.figure(3)
    if graph_type == "scatter":
        plt.scatter(tv, imdb)
    min_val = floor(min(min(tv), min(imdb)))
    plt.xlim(min_val, 10)
    plt.ylim(min_val, 10)
    plt.ylabel("IMDB")
    plt.xlabel("TV.com")
    plt.title(show_name)

    plt.show()


def do_show(show_name, graph_type="scatter"):
    t, i = unpack_show(show_name)
    analyze_show(show_name, t, i)
    visualize_show(show_name, t, i, graph_type=graph_type)


def unpack_season(show_name):
    seasons = len(tv[show_name].keys())
    tvcom = []
    imdbcom = []
    for i in range(1, seasons + 1):
        tvcom.append(np.array(tv[show_name][i]))
        imdbcom.append(np.array(imdb[show_name][i]))
    return tvcom, imdbcom


def analyze_season(show_name, tv, imdb):
    seasons = len(tv)
    for i in range(seasons):
        tv_rating = np.mean(tv[i])
        imdb_rating = np.mean(imdb[i])
        print(f"Season {i+1} of {show_name} had a mean score of {tv_rating} on tv.com and {imdb_rating} on imdb.com")


def visualize_season(show_name, tv, imdb, graph_type="plot"):
    plt.figure(1)
    if graph_type == "plot":
        for i in range(len(tv)):
            episodes = len(tv[i])
            plt.plot(range(episodes), tv[i])
    plt.xlabel("episode")
    plt.ylabel("score")
    plt.legend([n+1 for n in range(len(tv))])
    plt.title(show_name + " on tv.com")

    plt.figure(2)
    if graph_type == "plot":
        for i in range(len(imdb)):
            episodes = len(imdb[i])
            plt.plot(range(episodes), imdb[i])
    plt.xlabel("episode")
    plt.ylabel("score")
    plt.legend([n + 1 for n in range(len(imdb))])
    plt.title(show_name + " on IMDB")

    plt.show()


def do_season(show_name, graph_type="plot"):
    t, i = unpack_season(show_name)
    analyze_season(show_name, t, i)
    visualize_season(show_name, t, i, graph_type=graph_type)

do_season("Deadwood", "plot")
