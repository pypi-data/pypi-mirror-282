
from qiskit import Aer, QuantumCircuit, transpile, assemble, execute
import numpy as np

class QuantumCosineSimilarity:
    def __init__(self):
        self.backend = Aer.get_backend('qasm_simulator')
    
    def compute(self, vec1, vec2):
        vec1, vec2 = np.array(vec1), np.array(vec2)
        n = len(vec1)
        
        qc = QuantumCircuit(n)
        qc.initialize(vec1, range(n))
        qc.initialize(vec2, range(n))
        
        qc.measure_all()
        
        t_qc = transpile(qc, self.backend)
        qobj = assemble(t_qc)
        result = execute(qc, self.backend).result()
        
        counts = result.get_counts(qc)
        overlap = counts.get('0' * n, 0) / sum(counts.values())
        return 2 * overlap - 1
