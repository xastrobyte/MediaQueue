from json import load
from typing import Union
from uuid import uuid4

from .person import Person
from .provider import StreamingProvider


class Media:
    """A Media object is a superclass for all types of Media
    including Movies, TV Shows, Limited Series, and Podcasts

    :param name: The name of this Media
    :param provider: The name of the StreamingProvider this Media is located on
    :param person: The Person that is watching this Media

    :keyword started: Whether or not this Media has been started (Defaults to False)
    :keyword finished: Whether or not this Media has been finished (Defaults to False)
    :keyword json: The JSON object to load a Media object from
    :keyword filename: The JSON file to load a Media object from

    :raises FileNotFoundError: When the JSON file cannot be found
    :raises KeyError: When the required parameters are missing from the JSON object
    :raises ValueError: When any of the parameters have invalid values
    """

    # # # # # # # # # # # # # # # # # # # # # # # # #

    def __init__(self, name: str = None,
                 provider: Union[StreamingProvider, str] = None,
                 person: Union[Person, str] = None,
                 *, started: bool = False, finished: bool = False,
                 json: dict = None, filename: str = None):

        media_id = None  # Give the ID some default value

        # Check if a JSON file was given
        if filename is not None:
            with open(filename, "r") as jsonfile:
                json = load(jsonfile)

        # Check if a JSON object was given
        if json is not None:
            if not {"id", "name", "provider", "person"}.issubset(set(json.keys())):
                raise KeyError("ID, Name, Provider, and Person must be specified")

            media_id = str(json["id"])
            name = json["name"]
            provider = json["provider"]
            person = json["person"]
            started = False if "started" not in json else json["started"]
            finished = False if "finished" not in json else json["finished"]

        # Validate the parameters values
        if name is None:
            raise ValueError("The name must be specified")
        if provider is None:
            raise ValueError("The Streaming Provider must be specified")
        if person is None:
            raise ValueError("The Person must be specified")
        if started is None:
            started = False
        if finished is None:
            finished = False

        if media_id is not None and len(media_id) == 0:
            raise ValueError("The ID must have a length > 0")
        if len(name) == 0:
            raise ValueError("The name must have a length > 0")
        if isinstance(provider, str):
            if len(provider) == 0:
                raise ValueError("The streaming provider must have a length > 0")
            provider = StreamingProvider(provider)
        if isinstance(person, str):
            if len(person) == 0:
                raise ValueError("The person's name must have a length > 0")
            person = Person(person)
        if started and finished:
            raise ValueError("This media cannot be started and finished at the same time")

        self.__id = str(uuid4()) if media_id is None else media_id
        self.__name = name
        self.__provider = provider
        self.__person = person
        self.__started = started
        self.__finished = finished

    # # # # # # # # # # # # # # # # # # # # # # # # #

    def set_id(self, id: str):
        """Sets the ID for this Media object"""
        self.__id = id

    def get_id(self) -> str:
        """Returns the ID of this Media object"""
        return self.__id

    def get_name(self) -> str:
        """Returns the name of this Media object"""
        return self.__name

    def get_provider(self) -> StreamingProvider:
        """Returns the StreamingProvider where this Media object is located"""
        return self.__provider

    def get_person(self) -> Person:
        """Returns the Person who is watching this Media"""
        return self.__person

    def is_started(self) -> bool:
        """Returns whether or not this Media has been started"""
        return self.__started

    def is_finished(self) -> bool:
        """Returns whether or not this Media has been finished"""
        return self.__finished

    def get_runtime(self, in_hours: bool = False) -> int:
        """Returns the runtime of this media"""
        raise NotImplementedError()

    # # # # # # # # # # # # # # # # # # # # # # # # #

    def to_json(self) -> dict:
        """Returns the JSON representation of this Media object"""
        raise NotImplementedError()

    def save(self):
        """Saves this Media object into a JSON file"""
        raise NotImplementedError()