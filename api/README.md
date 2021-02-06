# API

API is served via `/checkpoliticalview/{view}` endpoint on the port 5000 locally. Since the skill also runs locally, it is trivial to send request to this endpoint. `view` is taken and fed into the pretrained BERT model to retrieve a prediction e.g. Biden.

The model class is stored in [SentimentClassifier.py](SentimentClassifier.py) which is basic BERT model with having a linear layer on top. The training is carried out in the [notebook files](../notebooks/).