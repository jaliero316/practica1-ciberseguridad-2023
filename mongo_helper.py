import datetime
import os

from pymongo import MongoClient


from dotenv import load_dotenv
load_dotenv()


class Mongo:

    def __init__(self):

        user = os.environ.get('MONGO_USER')
        password = os.environ.get('MONGO_PASS')
        host = os.environ.get('MONGO_URL')

        print(user, password, host)

        self.client = MongoClient(f"mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority")
        self.db = self.client.pressreader
        self.collection_name = "wallapop_search"

    def insert_publication_delivery(self, basename: str, chat_id: str, link: str):
        """
        Send batches of records to MongoDB
        """

        collection = self.db.get_collection(self.collection_name)
        collection.insert_one({
            "basename": basename,
            "chat_id": chat_id,
            "link": link,
            "datetime": datetime.datetime.now()
        })

if __name__ == "__main__":


    mongo = Mongo()



