
from scipy.spatial import KDTree

class KDTreeIndex:
    def __init__(self, data):
        self.tree = KDTree(data)
    
    def query(self, vector, k=1):
        distance, index = self.tree.query(vector, k=k)
        return distance, index
