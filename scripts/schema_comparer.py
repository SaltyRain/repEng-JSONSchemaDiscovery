import subprocess

class SchemaComparer:
    """Class to compare schemas through MD5 checksums and file differences."""

    def __init__(self, original_file, generated_file):
        self.original_file = original_file
        self.generated_file = generated_file

    def calculate_md5(self, file_path):
        """Calculate the MD5 checksum of a file."""
        result = subprocess.run(['md5sum', file_path], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.split()[0]
        else:
            raise ValueError(f"Failed to calculate MD5 for {file_path}")
    
    def calculate_diff(self, file1, file2):
        """Calculate the differences between two files."""
        result = subprocess.run(['diff', file1, file2], capture_output=True, text=True)
        if result.returncode in [0, 1]:  # 0 means no differences, 1 means differences
            return result.stdout
        else:
            raise ValueError("Failed to compare files")


    def compare_schemas(self):
        """Compare two schema files by their MD5 checksums and content differences."""
        original_file_hash = self.calculate_md5(self.original_file)
        generated_file_hash = self.calculate_md5(self.generated_file)

        print(f"Hash value (Original File): {original_file_hash}")
        print(f"Hash value (Generated File): {generated_file_hash}")

        if original_file_hash == generated_file_hash:
            print("\nThe hash values of both files are identical, indicating a match.")
            print("\nReproduction is confirmed.")
        else:
            file_diff = self.calculate_diff(self.original_file, self.generated_file)
            if file_diff:
                print("\nDifferences in files found:")
                print(file_diff)
                print("Reproduction cannot be confirmed due to differences.")
            else:
                print("\nThe content of both files are functionally identical.")
                print("Reproduction is confirmed.")
