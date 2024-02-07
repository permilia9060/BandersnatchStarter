from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    def __init__(self, db_name, collection_name):
        self.client = MongoClient("mongodb+srv://permilia9060:Dillon9060!@cluster0.v88hr8e.mongodb.net/?retryWrites="
                                  "true&w=majority")
        self.db = self.client["BandersnatchStarter"]
        self.collection = self.db["Collection"]

    def seed(self):
        sample_data = [{"name": f"Monster {i}", "type": "Unknown"} for i in range(1, 1000 + 1)]
        result = self.collection.insert_many(sample_data)
        return len(result.inserted_ids)

    def reset(self):
        result = self.collection.delete_many({})
        return result.deleted_count

    def count(self) -> int:
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        cursor = self.collection.find()
        data = list(cursor)
        df = DataFrame(data)
        return df

    def html_table(self) -> str:
        cursor = self.collection.find()
        df = DataFrame(list(cursor))
        html_table = df.to_html(index=False)
        return html_table




