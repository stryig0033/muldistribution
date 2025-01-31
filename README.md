# Data preprocessing for medical muldistribution analysis
preprocessed poi data using these codes.
- classification_results/20##_classified.csv
    - classification results of each years
- input_data/20##.csv
    - this is initially manually preprocessed department name data. checked if space-splitting is correct.
- modules/classify.py
    - this is classification function
- modules/dictionary.py
    - this depicts the rule of classification in dictionary format
- poi_medicine
    - original data (some of it is not tracked by git due to large volume)
- 20##_dpt_name_classification.ipynb
    - you can run this code to classify unique department names for their reliable category.