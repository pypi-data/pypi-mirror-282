from dataclasses import dataclass

from falgopy.algorithm.algorithm_output import AlgorithmOutput


@dataclass
class SearchingAlgorithmOutput(AlgorithmOutput):
    total_iterations: int = 0
    target_index: int = None
