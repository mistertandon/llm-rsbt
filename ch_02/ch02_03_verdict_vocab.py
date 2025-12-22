import re

class Vocabulary:
    def __init__(self, text=""):
        self.corpus_text = text
        self.tokens = []
        self.unique_tokens = set()
        self.sorted_tokens = []
        self.vocabulary = {}

    def set_corpus_text(self, text):
        self.corpus_text = text

    def tokenize(self, regEx):
        tokens = re.split(regEx, self.corpus_text)
        self.preprocessed_tokens = [token for token in tokens if token.strip()]

        return self.preprocessed_tokens

    def add_special_tokens(self, special_tokens):
        self.sorted_tokens.extend(special_tokens)

    def get_unique_tokens(self):
        self.unique_tokens = set(self.preprocessed_tokens)

    def sort_unique_tokens(self):
        self.sorted_tokens = sorted(self.unique_tokens)

    def build_vocabulary(self):
        self.vocabulary = {token: token_id for token_id, token in enumerate(self.sorted_tokens)}
    
    def get_vocabulary(self):
        return self.vocabulary
