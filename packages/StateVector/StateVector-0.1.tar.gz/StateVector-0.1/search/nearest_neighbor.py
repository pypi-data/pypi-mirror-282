
class NearestNeighborSearch:
    def __init__(self, index):
        self.index = index
    
    def search(self, vector, k=1):
        return self.index.query(vector, k=k)
