import inspect
import os
import unittest

from src.masoniteorm.query import QueryBuilder
from src.masoniteorm.query.grammars import PostgresGrammar
from src.masoniteorm.connections import ConnectionFactory
from src.masoniteorm.relationships import belongs_to
from src.masoniteorm.models import Model
from tests.utils import MockConnectionFactory
from config.database import DATABASES

if os.getenv("RUN_POSTGRES_DATABASE") == "True":

    class User(Model):
        __connection__ = "postgres"
        __timestamps__ = False

    class BaseTestQueryRelationships(unittest.TestCase):

        maxDiff = None

        def get_builder(self, table="users"):
            connection = ConnectionFactory().make("postgres")
            return QueryBuilder(
                grammar=PostgresGrammar,
                connection=connection,
                table=table,
                # model=User,
                connection_details=DATABASES,
            ).on("postgres")

        def test_transaction(self):
            builder = self.get_builder()
            builder.begin()
            builder.create({"name": "phillip2", "email": "phillip2"})
            # builder.commit()
            user = builder.where("name", "phillip2").first()
            self.assertEqual(user["name"], "phillip2")
            builder.rollback()
            user = builder.where("name", "phillip2").first()
            self.assertEqual(user, None)