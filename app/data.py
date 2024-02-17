from os import getenv   # retrieve environment variables
from certifi import where   # imports the where constant from the certifi module
from dotenv import load_dotenv  # imports the load_dotenv function from the dotenv module
from MonsterLab import Monster  # imports the Monster class from the MonsterLab module
from pandas import DataFrame  # imports the DataFrame class from the pandas library
from pymongo import MongoClient  # imports the MongoClient class from the pymongo library

# purpose of project: provide a way to interact with a MongoDB database to create an HTML table


class Database:  # like a template for making objects and refers an instance of class

    """
    functions:

 attributes:
    db_name: the name of the MongoDB database
    collection_name: the name of the collection

 methods:
    __init__(self, db_name="BandersnatchStarter", collection_name="Collection"):
        makes sure the env variables are loaded and the Database is initialized and connected to the database

    seed(self, sample_data_function):
        puts sample data into the collection

    reset(self):
        deletes the documents from the collection

    count(self) -> int
        returns the number of documents

    dataframe(self) -> DataFrame
        gets documents from the collection and changes them into a Pandas DataFrame

    html_table(self) -> str
        gets documents from the collection and makes an HTML table

    try/except
        catches errors
    """

    def __init__(self, db_name="BandersnatchStarter", collection_name="Collection"):  # gets Database object ready so
        # you can use it

        try:
            load_dotenv()  # loads the env variables
            self.db_name = db_name  # stores the name of the MongoDB database
            self.collection_name = collection_name  # stores the name of the collection
            db_url = getenv('DB_URL')  # gets the value of the environmental variables
            if db_url is None:  # Looks for errors in the .env file
                raise EnvironmentError("DB_URL environment variable is not set.")
            self.database = MongoClient(getenv('DB_URL'))[self.db_name]  # makes a connection to the MongoDB database
            self.collection = self.database[self.collection_name]  # Sets up the database name and collection name
        except Exception as e:  # error message
            print(f"An error occurred while initializing the database: {str(e)}")

    def seed(self, sample_data_function):
        try:
            sample_data = [sample_data_function().to_dict() for i in range(1, 1001)]
            result = self.collection.insert_many(sample_data)

        except Exception as e:
            print(f"An error occurred while seeding the collection: {str(e)}")

    def reset(self):
        try:
            result = self.collection.delete_many({})  # this line deletes multiple documents from the MongoDB collection
            return result.deleted_count  # returns the number of documents deleted
        except Exception as e:
            print(f"An error occurred while resetting the collection: {str(e)}")

    def count(self) -> int:
        try:
            return self.collection.count_documents({})  # returns the number of documents in the MongoDB collection
        except Exception as e:
            print(f"An error occurred while counting documents in the collection: {str(e)}")

    def dataframe(self) -> DataFrame:  # retrieves documents and converts them into a Pandas Dataframe
        try:
            cursor = self.collection.find({}, {"_id": False})  # retrieves all the documents
            data = list(cursor)  # converts the cursor into a list of dictionaries
            df = DataFrame(data)  # creates a Pandas Dataframe from the list
            return df
        except Exception as e:
            print(f"An error occurred while converting documents to DataFrame: {str(e)}")

    def html_table(self) -> str:  # generates an HTML table
        try:
            cursor = self.collection.find()  # retrieves all the documents
            df = DataFrame(list(cursor))  # changes the documents stored in the cursor into a Pandas DataFrame
            html_table = df.to_html(index=False)  # this will create an HTML string containing a table
            return html_table
        except Exception as e:
            print(f"An error occurred while generating HTML table: {str(e)}")












