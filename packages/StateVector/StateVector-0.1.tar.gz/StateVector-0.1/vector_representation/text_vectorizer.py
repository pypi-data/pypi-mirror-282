
from gensim.models import Word2Vec
import numpy as np

class TextVectorizer:
    def __init__(self, model_path='model/word2vec_model.bin'):
        self.model = Word2Vec.load(model_path)
    
    def vectorize(self, text):
        words = text.split()
        vectors = [self.model.wv[word] for word in words if word in self.model.wv]
        if not vectors:
            return np.zeros(self.model.vector_size)
        return np.mean(vectors, axis=0)
