
# StateVector

StateVector is a highly efficient vector database leveraging classical and quantum algorithms to optimize cosine similarity calculations. It supports various data types such as text, images, and audio, providing fast and accurate similarity searches.

## Features
- **Vector Representation**: Converts text, images, and audio into vector representations using algorithms like Word2Vec.
- **Similarity Calculation**: Computes cosine similarity using both classical and quantum-optimized algorithms.
- **Indexing**: Builds efficient indexes using KD Trees for quick retrieval of similar vectors.
- **Search**: Performs nearest neighbor search for similarity queries.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/StateVector.git
    cd StateVector
    ```
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
### Text Vectorization
```python
from vector_representation.text_vectorizer import TextVectorizer

vectorizer = TextVectorizer('model/word2vec_model.bin')
vector = vectorizer.vectorize("example text")
```

### Cosine Similarity
```python
from similarity.cosine_similarity import CosineSimilarity

similarity = CosineSimilarity.compute(vector1, vector2)
```

### Quantum Cosine Similarity
```python
from similarity.quantum_cosine_similarity import QuantumCosineSimilarity

quantum_similarity = QuantumCosineSimilarity()
similarity = quantum_similarity.compute(vector1, vector2)
```

### KD Tree Indexing
```python
from index.kd_tree import KDTreeIndex

index = KDTreeIndex(data)
distance, index = index.query(vector, k=5)
```

### Nearest Neighbor Search
```python
from search.nearest_neighbor import NearestNeighborSearch

search = NearestNeighborSearch(index)
results = search.search(vector, k=5)
```

## Documentation
See the `docs` directory for detailed documentation on each module.

---

# StateVector

StateVector 是一个高效的向量数据库，利用经典和量子算法优化余弦相似性计算。它支持文本、图像和音频等多种数据类型，提供快速准确的相似性搜索。

## 特性
- **向量表示**：使用 Word2Vec 等算法将文本、图像和音频转换为向量表示。
- **相似度计算**：使用经典和量子优化算法计算余弦相似度。
- **索引**：使用 KD 树构建高效索引，快速检索相似向量。
- **搜索**：执行最近邻搜索以进行相似性查询。

## 安装
1. 克隆仓库：
    ```sh
    git clone https://github.com/yourusername/StateVector.git
    cd StateVector
    ```
2. 安装所需依赖：
    ```sh
    pip install -r requirements.txt
    ```

## 使用方法
### 文本向量化
```python
from vector_representation.text_vectorizer import TextVectorizer

vectorizer = TextVectorizer('model/word2vec_model.bin')
vector = vectorizer.vectorize("example text")
```

### 余弦相似度
```python
from similarity.cosine_similarity import CosineSimilarity

similarity = CosineSimilarity.compute(vector1, vector2)
```

### 量子余弦相似度
```python
from similarity.quantum_cosine_similarity import QuantumCosineSimilarity

quantum_similarity = QuantumCosineSimilarity()
similarity = quantum_similarity.compute(vector1, vector2)
```

### KD 树索引
```python
from index.kd_tree import KDTreeIndex

index = KDTreeIndex(data)
distance, index = index.query(vector, k=5)
```

### 最近邻搜索
```python
from search.nearest_neighbor import NearestNeighborSearch

search = NearestNeighborSearch(index)
results = search.search(vector, k=5)
```

## 文档
详见 `docs` 目录下各模块的详细文档。


