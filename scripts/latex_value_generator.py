class LatexValueGenerator:
    """Class for regenerating PDF values after experiment execution."""

    def __init__(self, file_path):
        """Initialize the LatexValueGenerator with the path to the LaTeX file."""
        self.file_path = file_path
        self.original_paper = {
            "drugs": "2818", 
            "companies": "21312", 
            "movies": "25140"
        }

    def generate_latex_values(self, list_of_values):
        """Generates and updates LaTeX file with new values."""
        # Initialize the rows string outside of the file operation
        rows = ''

        # Iterate over the list_of_values and build rows
        for values in list_of_values:
            row = f"{values['collectionName']} & {values['collectionCount']} & {values['uniqueUnorderedCount']} & {values['uniqueOrderedCount']} & {self.original_paper.get(values['collectionName'], 'N/A')} & {self.original_paper.get(values['collectionName'], 'N/A')} \\\\"
            rows += row + '\n'
            rows += '\hline\n'

        # Open the file to read content and then write modified content
        with open(self.file_path, 'r+') as file:
            # Read the content of the LaTeX template
            latex_template = file.read()

            # Replace %RESULT% with the generated results in the LaTeX template in 'results-table'
            latex_template = latex_template.replace('%RESULT%', rows)

            # IMPORTANT: Move the file pointer to the beginning before writing
            file.seek(0)

            # Write the modified LaTeX template back to the file
            file.write(latex_template)

            # Ensure the file is truncated if the new content is shorter than the old
            file.truncate()
        print(f"Latex file updated with new values.")
