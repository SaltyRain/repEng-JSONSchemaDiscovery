class CollectionMapping:
    """Class to store and manage mappings between collection names and files."""
    
    def __init__(self):
        """Initializes the collection mappings."""
        self.mappings = {
            "drugs": "dbpedia-drugs1.json",
            "companies": "dbpedia_companies1.json",
            "movies": "dbpedia_movies1.json"
        }
    
    def get_file_name(self, collection_name):
        """Returns the file name associated with a given collection name."""
        return self.mappings.get(collection_name, None)
