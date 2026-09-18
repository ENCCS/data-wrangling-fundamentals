import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# create text data
text_data = np.array([
    "I love France. France!",
    "Argentina is best",
    "Spain beats both"
])

count_single = CountVectorizer(
    token_pattern=r"(?u)\b\w+\b"
)

bag_of_words_single = count_single.fit_transform(text_data)
count_single.get_feature_names_out()
