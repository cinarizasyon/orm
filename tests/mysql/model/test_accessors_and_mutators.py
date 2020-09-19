import json
import os
import unittest

import pendulum
import datetime

from app.User import User
from src.masoniteorm.orm.collection import Collection
from src.masoniteorm.orm.query.grammars import MSSQLGrammar
from src.masoniteorm.orm.models import Model


class User(Model):

    __casts__ = {"is_admin": "bool"}

    def get_name_attribute(self):
        return f"Hello, {self.get_raw_attribute('name')}"

    def set_name_attribute(self, attribute):
        return str(attribute).upper()


class SetUser(Model):

    __casts__ = {"is_admin": "bool"}

    def set_name_attribute(self, attribute):
        return str(attribute).upper()


class TestAccessor(unittest.TestCase):
    def test_can_get_accessor(self):
        user = User.hydrate(
            {"name": "joe", "email": "joe@masoniteproject.com", "is_admin": 1}
        )
        self.assertEqual(user.email, "joe@masoniteproject.com")
        self.assertEqual(user.name, "Hello, joe")
        self.assertTrue(user.is_admin is True, f"{user.is_admin} is not True")

    def test_mutator(self):
        user = SetUser.hydrate({"email": "joe@masoniteproject.com", "is_admin": 1})

        user.name = "joe"

        self.assertEqual(user.name, "JOE")
