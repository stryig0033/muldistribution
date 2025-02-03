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

# Preprocessing Overview

In this preprocessing, the general character classification rules are defined in `modules/dictionary.py`.  
Additionally, if individual classifications are required for specific files, those classification rules are defined in the variable `override_map_20##` within `20##_dpt_name_classification.ipynb`.

## About `modules/dictionary.py`
All general classification rules are defined here.  

For each medical department, three topics are set:
- **`"must"`**: Words that **must** be included in the string.
- **`"any"`**: Words that should be included **at least once**.
- **`"not"`**: Words that **must not** be included.

Each word also has a `"partial"` or `"exact"` setting:
- **`"partial"`**: The word only needs to appear as **part of a string**.
- **`"exact"`**: The **entire word** must appear exactly as it is.

Using this reference table, classification is executed in `modules/classify.py`.

## About `override_map_20##`
This is dictionary data used to perform individual classifications for each Excel file.  
Cases where there is no distinction between internal medicine and surgery, or where a special expression refers to two or more medical departments, are also handled here.
- The **left column** contains the **target words for classification**.
- The **right column** specifies the **medical department** to which each word should be assigned.

These dictionary data are also processed together in `modules/classify.py`.  
Additionally, whether the classification uses `"partial"` or `"exact"` matching can be configured in `modules/classify.py`.
