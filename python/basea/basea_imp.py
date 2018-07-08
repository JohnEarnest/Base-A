# -*- coding: utf-8 -*-
"""
The implementation of Base-Ä items
"""
from decimal import Decimal

from six import string_types


class _Thing(object):

    def __init__(self):
        self.a = [
            'Atomic', 'Ballistic', 'Big', 'Boxer', 'Bracer', 'Brawler', 'Breaker', 'Challenger',
            'Champion', 'Cherno', 'Chrome', 'Cobra', 'Contender', 'Coyote', 'Crimson', 'Decider',
            'Diablo', 'Dingo', 'Disrupter', 'Echo', 'Eden', 'Falcon', 'Fearless', 'Galaxy',
            'Gallant', 'Gipsy', 'Golden', 'Grand', 'Grizzly', 'Guardian', 'Horizon', 'Hydra',
            'Intrepid', 'Keeper', 'Legend', 'Mammoth', 'Matador', 'Mighty', 'Mountain', 'Neon',
            'Nova', 'Phantom', 'Protector', 'Puma', 'Righteous', 'Romeo', 'Shaolin', 'Shining',
            'Solar', 'Spartan', 'Steady', 'Striker', 'Tacit', 'Tesla', 'Tiger', 'Titan', 'Valiant',
            'Viper', 'Vulcan', 'Warden', 'Warrior', 'Wildcat', 'Yankee', 'Zenith',
        ]
        self.b = [
            'Absolute', 'Ajax', 'Alpha', 'Apostle', 'Ares', 'Artemis', 'Assassin', 'Athena',
            'Avenger', 'Banzai', 'Blue', 'Brave', 'Bravo', 'Brutus', 'Cerberus', 'Colossus',
            'Corinthian', 'Courage', 'Cruiser', 'Danger', 'Dawn', 'Dazzle', 'Delta', 'Dreadnought',
            'Eureka', 'Finisher', 'Fist', 'Fortress', 'Fury', 'Gauntlet', 'Gladius', 'Hyperion',
            'Infinite', 'Intercept', 'Judas', 'Kilo', 'Lightning', 'Mega', 'November', 'Omega',
            'Paladin', 'Phoenix', 'Prophet', 'Real', 'Redeemer', 'Resolve', 'Rogue', 'Romeo',
            'Ronin', 'Saber', 'Sentinel', 'Sierra', 'Specter', 'Tango', 'Thunder', 'Turbo',
            'Typhoon', 'Venus', 'Victory', 'Vigor', 'Yukon', 'Zero', 'Zeus', 'Zulu',
        ]
        self.max = (len(self.a) * len(self.b)) - 1
        self.int_to_string = {}
        self.string_to_int = {}

        for x in range(0, self.max + 1):
            h = (x * 123) & self.max
            s = self.a[(h >> 6) % len(self.a)] + ' ' + self.b[h % len(self.b)]
            self.int_to_string[x] = s
            self.string_to_int[s.lower()] = x

    def valid(self, name):
        """
        Return the validity of the string given being worthy of a giant monster fighting giant robot
        :param name: The name of the giant robot
        :return: true/false as a validity of the worthiness
        """
        return name is not None and name.lower() in self.string_to_int

    def encode(self, val):
        """
        Return a name worthy of a giant monster fighting giant robot corresponding to the integer value given
        :param val: An integer value to convert to the name of a giant monster fighting giant robot
        :return: the name of a giant monster fighting giant robot
        """
        if isinstance(val, (int, float, Decimal)) and 0 <= val <= self.max:
            return self.int_to_string[int(val)]
        raise ValueError('Invalid integer value')

    def decode(self, name):
        """
        Return an integer representing the name of a giant monster fighting giant robot.
        :param name: The name of a giant monster fighting giant robot
        :return: integer representation of the name of a giant monster fighting giant robot
        """
        if isinstance(name, string_types) and self.valid(name):
            return self.string_to_int[name.lower()]
        raise ValueError('Invalid name value')


basea_instance = _Thing()
