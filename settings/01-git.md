http://localhost:8888/lab?token=755b70873b06ffc234c83ad1cc8bf429fe80e9dc14b1a85b


git commit -m 'feat: Develop code to tokenize The Verdict text'
git commit -m 'feat: Develop a SimpleTokenizerV2 class that generates tokens for a given vocabulary derived from The Verdict text. And generate tokenID for unknown token'
git commit -m 'feat: Develop a Vocabulary class to build a vocabulary from the provided corpus text.'

git push origin Feature-01-Simple-Tokenization
git push origin main

git commit -m 'feat:
1. Add keyboard shortcuts when working with JupyterLab inside Visual Studio Code.
2. Implement a tiktoken-based tokenizer as used in GPT models'

git commit -m 'feat:
1. Prepare input-target pair using torch Dataset and DataLoader.'

git commit -m 'feat:
1. Basic functionality to convert tokenID to embedding weight matrix'

ch_02_28_encoding_word_positions
ch_03_3_3_1_simple_self_attention

git commit -m 'feat:
ch02_27_creating_token_embeddings: Create Input token embedding
ch02_28_encoding_word_positions: Create Input token position embedding'

git commit -m 'feat:
ch_03_3_1_simple_self_attention: Calculate the attention weight associated with the element at index 2 in the input sequence.'

git commit -m 'feat:
ch_03_3.4.1_attention_weights: Compute the attention weights given the query, key, and value vectors. In this notebook, we specifically compute the attention weights for the element at index 2, corresponding to “journey” in the input sequence.'


Assume you're a ml researcher
Fix grammar and turn below content into ielts band 9
Input:
Compute attention weight given query, key and value
In this notebook we'll compute attention_weights particularly for element 2 i.e. journey