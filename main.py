import os
import sys

from media import Movie, TVShow, Podcast, LimitedSeries
from ui import MediaQueue


if __name__ == "__main__":

    # Create the directories for the media, if necessary
    if not os.path.exists("./data"):
        os.mkdir("./data")
    if not os.path.exists(f"./data/{Movie.FOLDER}"):
        os.mkdir(f"./data/{Movie.FOLDER}")
    if not os.path.exists(f"./data/{TVShow.FOLDER}"):
        os.mkdir(f"./data/{TVShow.FOLDER}")
    if not os.path.exists(f"./data/{Podcast.FOLDER}"):
        os.mkdir(f"./data/{Podcast.FOLDER}")
    if not os.path.exists(f"./data/{LimitedSeries.FOLDER}"):
        os.mkdir(f"./data/{LimitedSeries.FOLDER}")

    app = MediaQueue(sys.argv)
