import os
import logging 
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO)

project_name="mlproject"

# Create the project directory
list_of_files=[
    #".github/workflows./gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion",
    f"src/{project_name}/components/data_transformatoin",
    f"src/{project_name}/components/Modal_tranier/__init__.py",
    f"src/{project_name}/components/Model_monitoring",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/train_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/utils",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception_handing.py",
    "app.py",

    

]

for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object
    filedir, filename = os.path.split(filepath)  # Get directory and filename

    if filedir != "":  # Check if the directory part is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # Check if the file doesn't exist or is empty
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")