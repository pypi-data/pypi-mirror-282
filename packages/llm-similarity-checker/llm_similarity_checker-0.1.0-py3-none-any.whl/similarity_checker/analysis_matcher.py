import joblib
import torch
from scipy.spatial.distance import cosine
from transformers import BertTokenizer, BertModel
import os

class AnalysisMatcher:
    def __init__(self, tokenizer_path=None, model_path=None):
        if tokenizer_path and model_path:
            self.tokenizer = joblib.load(tokenizer_path)
            self.model = joblib.load(model_path)
        else:
            self.load_from_pretrained()
    
    def load_from_pretrained(self, model_name='bert-base-uncased'):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name)

        # Create the directory if it doesn't exist
        if not os.path.exists("trained_models/"):
            os.makedirs("trained_models/")
            print(f"Directory created: trained_models/")
        else:
            print(f"Directory already exists: trained_models/")

        joblib.dump(self.tokenizer, 'trained_models/bert_tokenizer.joblib')
        joblib.dump(self.model, 'trained_models/bert_model.joblib')
    
    def get_sentence_embedding(self, sentence):
        inputs = self.tokenizer(sentence, return_tensors='pt', max_length=128, truncation=True, padding='max_length')
        with torch.no_grad():
            outputs = self.model(**inputs)
        # Get the embeddings for the [CLS] token (which represents the sentence)
        cls_embedding = outputs.last_hidden_state[0, 0, :]
        return cls_embedding
    
    def cosine_similarity(self, vec1, vec2):
        return 1 - cosine(vec1, vec2)
    
    def match(self, sentence1, sentence2, threshold=0.8):
        embedding1 = self.get_sentence_embedding(sentence1)
        embedding2 = self.get_sentence_embedding(sentence2)
        similarity = self.cosine_similarity(embedding1, embedding2)
        return similarity > threshold

if __name__ == "__main__":
    matcher = AnalysisMatcher(
        tokenizer_path='trained_models/bert_tokenizer.joblib',
        model_path='trained_models/bert_model.joblib'
    )

    sentence1 = "The quick brown fox jumps over the lazy dog."
    sentence2 = "A fast, brown fox leaps over a lazy dog."

    similarity_score = matcher.match(sentence1, sentence2)
    print(f"Are the sentences similar? {'Yes' if similarity_score else 'No'}")
   