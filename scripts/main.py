from collection_mapping import CollectionMapping
from database_manager import DatabaseManager
from json_schema_extractor import JSONSchemaExtractor
from latex_value_generator import LatexValueGenerator
from schema_comparer import SchemaComparer
from user_auth import UserAuthentication

def main():
    print(f"Step 1. Connect to the database and remove it if it already exists")
    db_name = "jsonschemadiscovery"
    db_manager = DatabaseManager(db_name)
    db_manager.remove_db()

    print(f"\nStep 2. Create user and login")

    # Create user
    # NOTE: this function can be called without parameters to use the default values. In this case, they are equal to the parameters passed.
    response = UserAuthentication.create_user()
    if response == 'ok':
        print(f"\n User created successfully.")
    else:
        print(f"\n User creation failed.")

    collection_mapping = CollectionMapping()
    extracted_json_folder = "/home/repro/JSONSchemaDiscovery/extracted_json"

    print(f"\nStep 3. Import data into the database")
    print(f"\n Extracting archives and importing data into the database ...")

    # Iterate over the collection mappings and perform the import for each
    for collection_name, file_name in collection_mapping.mappings.items():
        print(f"\n Extracting and importing data for {collection_name} ...")
        db_manager.extract_and_import(collection_name, file_name, extracted_json_folder)

    print(f"\n Data import completed.")

    print(f"\nStep 4. Extract raw schema from the database")
    extractor = JSONSchemaExtractor('http://localhost:4200')    

    for collection in collection_mapping.mappings.keys():
        response = extractor.send_request_to_server(collection)
        if response == 'ok':
            print(f"\n Raw schema extraction for {collection} completed.")
        else:
            print(f"\n Raw schema extraction for {collection} failed.")


    analyzedResult = extractor.get_analysis()
    print(f"\n Analysis Result:\n{analyzedResult}\n")

    # Save analysis results to a CSV file
    extractor.save_analysis_to_csv(analyzedResult)
    print(f"\n Analysis results saved to CSV file.")


    print(f"\nStep 5. Insert result into Latex file")
    file_path = '/home/repro/JSONSchemaDiscovery/rep-eng-paper/paper.tex'
    generator = LatexValueGenerator(file_path)
    generator.generate_latex_values(analyzedResult)

    print(f"\nStep 6. Result comparison from the original paper and from the current experiment")

    original_file = "/home/repro/JSONSchemaDiscovery/csv/original_data.csv"
    generated_file = "/home/repro/JSONSchemaDiscovery/csv/experiment_results.csv"

    comparer = SchemaComparer(original_file, generated_file)
    comparer.compare_schemas()

    print(f"\n Comparison completed.")


# Call main function
if __name__ == "__main__":
    main()