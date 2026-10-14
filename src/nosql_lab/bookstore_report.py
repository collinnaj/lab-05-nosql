
#!/usr/bin/env python3

import os
import logging

from pymongo import MongoClient


MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    
    client = None

    try:
        
        client = MongoClient(
            MONGODB_ATLAS_URL,
            username=MONGODB_ATLAS_USER,
            password=MONGODB_ATLAS_PWD,
            serverSelectionTimeoutMS=5000
        )

        
        client.admin.command("ping")
        logger.info("Connected to MongoDB Atlas successfully.")

        
        db = client["bookstore"]
        authors = db["authors"]
        books = db["books"]

        
        author_ids = ["author_002", "author_003", "author_004"]

        
        total_authors = authors.count_documents(
            {"_id": {"$in": author_ids}}
        )
        print(f"Authors: {total_authors}\n")

        
        for author_id in author_ids:
            author = authors.find_one({"_id": author_id})

            if author is not None:
                print(author["name"])

                
                for book in books.find({"author_ids": author_id}):
                    print(
                        f"  {book['title']} "
                        f"({book['published_year']})"
                    )

                print()

    except Exception:
        
        logger.exception("Could not generate the bookstore report.")

    finally:
        
        if client is not None:
            client.close()
            logger.info("MongoDB connection closed.")


if __name__ == "__main__":
    main()
