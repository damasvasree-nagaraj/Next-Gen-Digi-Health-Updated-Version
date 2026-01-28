from pymongo import MongoClient
import certifi

client = MongoClient(
    "mongodb+srv://nextgen_admin:nextgen123@cluster0.grbxsig.mongodb.net/?appName=Cluster0",
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000
)

print(client.admin.command("ping"))
