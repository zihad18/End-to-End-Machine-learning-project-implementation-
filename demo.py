import os

mongodburl = os.getenv("MONGODB_URL")
print(f"MongoDB URL: {mongodburl}")