import torch
from transformers import BertModel, BertConfig

class SentimentClassifier(torch.nn.Module):
    """
    BERT model with an additional Linear layer to be used for fine-tuning
    """
    def __init__(self, n_classes, name):
        super(SentimentClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(name)
        self.drop = torch.nn.Dropout(p=0.3)
        self.out = torch.nn.Linear(self.bert.config.hidden_size, n_classes)

    def forward(self, input_ids, attention_mask):
        _, pooled_output = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        output = self.drop(pooled_output)
        return self.out(output)