import os
from json import dump

from media import TVShow


class Podcast(TVShow):
    """A Podcast consists of Season of Episodes.

    :param name: The name of this Podcast
    :param seasons: The Season in this Podcast
    :param provider: The name of the StreamingProvider this Podcast is located on
    :param person: The Person that is watching this Podcast

    :keyword started: Whether or not this Podcast has been started (Defaults to False)
    :keyword finished: Whether or not this Podcast has been finished (Defaults to False)
    :keyword json: The JSON object to load a Podcast object from
    :keyword filename: The JSON file to load a Podcast object from

    :raises FileNotFoundError: When the JSON file cannot be found
    :raises KeyError: When the required parameters are missing from the JSON object
    """

    FOLDER = "podcasts"

    # # # # # # # # # # # # # # # # # # # # # # # # #

    def save(self):
        """Saves this Podcast object into a JSON file"""
        if not os.path.exists(Podcast.FOLDER):
            os.mkdir(Podcast.FOLDER)
        with open("./{}/{}.json".format(Podcast.FOLDER, self.get_id()), "w") as jsonfile:
            dump(self.to_json(), jsonfile, indent=4)
