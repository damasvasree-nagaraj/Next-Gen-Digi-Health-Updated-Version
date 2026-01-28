from pymongo import MongoClient
import certifi

client = MongoClient(
    "mongodb+srv://YOUR_USERNAME:PASSWORD@cluster0.grbxsig.mongodb.net/?appName=Cluster0",
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000
)

print(client.admin.command("ping"))

