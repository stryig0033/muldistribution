# Data preprocessing for medical muldistribution analysis
setup
```terminal
python -m venv .venv
source .venv/bin/activate #mac
pip install -r requirements.txt
```
preprocessed poi data using these codes.
- classification_results/20##_classified.csv
    - Classification results for each year.
- input_data/20##.csv
    - Initially, manually preprocessed department name data.
    - Ensured that space-splitting is correctly applied.
- modules/classify.py
    - Contains the classification function.
- modules/dictionary.py
    - Defines the classification rules in dictionary format.
- poi_medicine
    - Original data (some files are not tracked by Git due to large volume).
- 20##_dpt_name_classification.ipynb
    - Run this notebook to classify unique department names into their respective categories.