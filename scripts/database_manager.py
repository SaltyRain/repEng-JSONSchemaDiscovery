import os
from database_connection import DatabaseConnection
import tarfile
import json
from pymongo import errors

class DatabaseManager:
    """Class for managing database operations."""

    def __init__(self, db_name):
        """Initializes the database manager with the specified database name."""
        self.db_name = db_name
        self.db_connection = DatabaseConnection().get_connection()  # Establish database connection
        self.db = self.db_connection[db_name]  # Get the specified database

    def remove_db(self):
        """Drops the specified database."""
        self.db_connection.drop_database(self.db_name)
        print(f"Database '{self.db_name}' dropped successfully.")

    # close conntection
    def close_connection(self):
        """Closes the database connection."""
        self.db_connection.close()
        print("Database connection closed successfully.")

    def clean_line(self, line):
        """Cleans a line of text."""
        return ''.join(char if 31 < ord(char) < 127 else ' ' for char in line)
    

    # extract and import data from tar file
    def extract_and_import(self, collection_name, tar_file_name, extracted_json_folder):
        """Extracts and imports data into MongoDB."""
        datasets_folder = os.path.join("/home/repro/JSONSchemaDiscovery/datasets/", collection_name)
        tar_file = os.path.join(datasets_folder, f"{tar_file_name}.tar.bz2")
        extracted_folder_path = os.path.join(extracted_json_folder, tar_file_name)

        # Extract the tar.bz2 file safely
        if tarfile.is_tarfile(tar_file):
            with tarfile.open(tar_file, "r:bz2") as tar:
                tar.extractall(path=extracted_folder_path)

        # Import into MongoDB using pymongo
        collection = self.db[collection_name]
        for file_name in os.listdir(extracted_folder_path):
            file_path = os.path.join(extracted_folder_path, file_name)
            with open(file_path, 'r') as file:
                try:
                    for line_number, line in enumerate(file, start=1):
                        cleaned_line = self.clean_line(line)
                        try:
                            data = json.loads(cleaned_line)
                            collection.insert_one(data)
                        except json.JSONDecodeError as e:
                            print(f"Error decoding JSON at line {line_number}: {e}")
                except errors.PyMongoError as e:
                    print(f"Error importing data to MongoDB: {e}")
        print(f"\n Import files for {collection_name} completed ...")