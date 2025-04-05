from pymongo import MongoClient
import os

# Get the MongoDB URI from environment variables or use a default local URI
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://admin:admin@wanderlens-cluster.zu2hxva.mongodb.net/")
client = MongoClient(MONGO_URI)

# Select a database and collection
db = client["userTrips"]  # Change "mydatabase" as needed
collection = db["user1"]  # Change "mycollection" as needed

document = {
    "budget": "3000",
    "destination": "Ghaziabad",
    "end_day": "2025-04-08",
    "interests": "Food",
    "name": "hackathon",
    "start_day": "2025-04-03",
    "travellers": "Friends"
}

def insert_document(document):
    """Insert a document into the collection."""
    result = collection.insert_one(document)
    return result.inserted_id

def get_documents():
    """Retrieve all documents from the collection."""
    documents = list(collection.find())
    # Convert ObjectId to string for JSON serializability
    for doc in documents:
        doc["_id"] = str(doc["_id"])
    return documents
