from fastapi import FastAPI
import uvicorn
import time
from transformers import BertTokenizer
import torch
from SentimentClassifier import SentimentClassifier

PATH = "trump_biden_model.bin"
MAX_LEN = 160
PRE_TRAINED_MODEL_NAME = 'bert-base-cased'
device = torch.device("cpu")

app = FastAPI()

model = SentimentClassifier(2, PRE_TRAINED_MODEL_NAME)
model.load_state_dict(torch.load(PATH, map_location=device))
model.eval()

tokenizer = BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)


@app.get("/checkpoliticalview/{view}")
async def check_political_view(view: str):
    """
    Return the class of the `view` using the fine-tuned BERT model.
    :param view: str
    :return: str - `Biden` if the view is predicted to be of a Biden fan, `Trump` vice versa
    """
    encoded_comment = tokenizer.encode_plus(
        view.lower(),
        max_length=MAX_LEN,
        add_special_tokens=True,
        return_token_type_ids=False,
        pad_to_max_length=True,
        return_attention_mask=True,
        return_tensors='pt',
    )

    input_ids = encoded_comment['input_ids'].to(device)
    attention_mask = encoded_comment['attention_mask'].to(device)

    output = model(input_ids, attention_mask)
    _, prediction = torch.max(output, dim=1)

    return "Biden" if prediction.numpy().item() == 1 else "Trump"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
