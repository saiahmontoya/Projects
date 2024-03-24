from pymongo import MongoClient
from pprint import pprint  # for "pretty printing"


def connect():
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    # change this string to match the name of the database you created in Mongo
    return client['Project3']



if __name__ == "__main__":
    db = connect()
    camper_names = [
        {
            "$project": {
                "name": 1
            }
        }
    ]

    # Run the pipeline.
    results = db["campers"].aggregate(camper_names)

    # Pretty-print the results.
    pprint(list(results))

    for campers in results:
        print(f"{camper['camper_names']} (ID {camper['_id']})")