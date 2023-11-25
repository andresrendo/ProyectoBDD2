
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
ssl=True
uri = "mongodb+srv://andresrendo:28186020@aaaolaaa.jrfwm6q.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'),ssl_cert_reqs=ssl.CERT_NONE)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)