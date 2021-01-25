import os
import tensorflow as tf
import json
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle

TOKENIZER_PATH = 'saved_tokenizer'

def tokenize(dataset_dir = 'VQA_Dataset'):
    questions = []
    with open(os.path.join(dataset_dir, 'train_questions_annotations.json')) as f:
        annotations = json.load(f)
        for a_id, a in annotations.items():
            questions.append(a['question'])

    with open(os.path.join(dataset_dir, 'test_questions.json')) as f:
        annotations = json.load(f)
        for a_id, a in annotations.items():
            questions.append(a['question'])

    MAX_NUM_WORDS = 5000
    tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
    tokenizer.fit_on_texts(questions)

    ''' uncomment to calculate num_word and max_length    
    tokenized = tokenizer.texts_to_sequences(questions)
    word_index = tokenizer.word_index
    max_length = max(len(q) for q in tokenized)
    
    print(f"num_words: {len(word_index)} - max_seq_length: {max_length}")
    assert(False)
    '''
    
    with open(TOKENIZER_PATH, 'wb') as f:
        pickle.dump(tokenizer, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    return tokenizer

def get_tokenizer():
    if not os.path.exists(TOKENIZER_PATH):
        tokenize()

    with open(TOKENIZER_PATH, 'rb') as f:
        tokenizer = pickle.load(f)
    return tokenizer
    
if __name__ == "__main__":
    tokenize()
