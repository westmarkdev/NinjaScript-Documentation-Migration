# NinjaScript Documentation Migration

This repository contains the tools and processes for migrating NinjaScript documentation to a new format. It includes the original source files, a Python script for cleaning and reformatting the documentation, and the results of the migration process.

## Repository Structure

- `source_files/`: Contains all original documentation files (2500+ files)
- `staged_files/`: A subset of files used for testing the migration process
- `input/`: Copy of staged files used as input for the migration script
- `scripts/`: Contains the Python script used for migration
- `output/`: Contains the migrated and formatted documentation files

## Branches

- `main`: Contains the full set of source files and the final migration results
- `testing`: Used for testing the migration process with a subset of files

## Usage

To run the migration script:

1. Ensure you have Python 3.x installed
2. Install required libraries: `pip install mdformat pyyaml`
3. Run the script: `python scripts/markdown_fixer.py`

The script will process files from the `scripts/input/` directory and output the results to a timestamped folder in the `scripts/output/` directory.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.  

## Contact

For any questions or concerns, please open an issue in this repository or contact <matthew@westmark.dev>
