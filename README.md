# Asynchronous Parallel Disassembly Planning with Genetic Algorithm

This repository contains a sample implementation inspired by the paper "An asynchronous parallel disassembly planning based on genetic algorithm".

## Problem Statement
- Utilizing an asynchronous parallel approach for disassembly planning.
- Employing Genetic Algorithm for optimization.

## Initialization
- The initialization phase sets up the problem's constraints and parameters.

- DISASSEMBLY_TIMES: This dictionary provides the time taken by each manipulator to disassemble each part. There are two manipulators: M1 and M2. The nested dictionary provides the time taken by that manipulator to disassemble each part, where the key represents the part number and the value is the time taken.

For instance:

- DISASSEMBLY_TIMES['M1'][1] is 2, meaning it takes 2 units of time for manipulator M1 to disassemble part 1. DISASSEMBLY_TIMES['M2'][2] is 7, meaning it takes 7 units of time for manipulator M2 to disassemble part 2.

- P (Precedence Constraints): This dictionary defines the precedence relationship between parts. The key represents a part and the associated value (list) represents the parts that need to be disassembled before the key part.

For instance:

- P[2] is [1], meaning part 1 should be disassembled before part 2. P[3] is [1, 2], meaning parts 1 and 2 should be disassembled before part 3. In simple words, you can't start disassembling part X until all the parts listed in P[X] are completely disassembled.

- C (Concurrency Constraints): This dictionary defines the concurrency constraints between parts. The key represents a part, and the associated value (list) represents the parts that cannot be disassembled concurrently (at the same time) with the key part.

For instance:

- C[4] is [5], meaning parts 4 and 5 cannot be disassembled at the same time by the same or different manipulators. C[6] is [7], meaning parts 6 and 7 cannot be disassembled at the same time by the same or different manipulators. So if you start disassembling part 4, you cannot start disassembling part 5 until part 4 is completely disassembled and vice versa.



## Code Structure
- `evaluate_chromosome`: Evaluates a chromosome to calculate the total disassembly time.
- `roulette_wheel_selection`: Performs roulette wheel selection.
- `tournament_selection`: Performs tournament selection.
- `generate_a1_a2_strings`: Generates A1 and A2 strings for crossover.
- `precedence_preservative_crossover`: Performs precedence-preservative crossover.
- `mutate_based_on_precedence`: Performs mutation while preserving precedence relationships.
- `improved_GA`: Main function to run the Genetic Algorithm.

## Output
- The code will output the best solution found over the iterations of the GA.

## Regerence
@article{REN2018647,
title = {An asynchronous parallel disassembly planning based on genetic algorithm},
journal = {European Journal of Operational Research},
volume = {269},
number = {2},
pages = {647-660},
year = {2018},
issn = {0377-2217},
doi = {https://doi.org/10.1016/j.ejor.2018.01.055},
url = {https://www.sciencedirect.com/science/article/pii/S0377221718300912},
author = {Yaping Ren and Chaoyong Zhang and Fu Zhao and Huajun Xiao and Guangdong Tian},
keywords = {Combinatorial optimization, Disassembly sequence planning, Asynchronous parallel disassembly, Operation time-dependent, Metaheuristics},
abstract = {Disassembly is one of the most crucial remanufacturing activities. Disassembly sequence planning (DSP) is a combinatorial optimization problem and has been studied by many researchers. Conventional DSP techniques focus on sequential disassembly planning (SDP) in which only one manipulator is used to remove a single part or subassembly at a time such that it is inefficient when disassembling large or complex products. Recently, parallel disassembly has attracted some interest as it employs several manipulators to remove multiple components simultaneously. However, most of the work to date focuses on parallel disassembly techniques which require synchronization between manipulators, i.e., they must start their tasks simultaneously. This simplifies the modeling and analysis efforts but fails to fully realize the benefits of parallel disassembly. In this work, we propose asynchronous parallel disassembly planning (aPDP) which eliminates the synchronization requirement. In addition to precedence constraints, aPDP becomes highly operation time-dependent. To deal with this, we design an efficient encoding and decoding strategy for the disassembly process. In this paper, a metaheuristic approach, based on a genetic algorithm, is developed to solve the aPDP problem. The proposed algorithm is applied to four products which require disassembly processes of varying complexity, and the results are compared with two methods reported in literature. It is suggested that the proposed approach can identify faster disassembly processes, especially when solving large-scale problems.}
}

## Example Code 
- Details about the code can be found in [Jupyter Notebook](https://github.com/shailendrabhandari/PDP_genetic_algorithm/blob/main/PDP_geneticAlgorithm.ipynb).

  ## Author
[Shailendra Bhandari](https://github.com/shailendrabhandari)

- 👨‍💻 Data Science Enthusiast (Quantum AI, Evolutionary Algorithms, and Natural Language Processing)
- 📖 Open Source Enthusiast
- 🐦 [@bh_shailendra](https://twitter.com/bh_shailendra)
- 📧 Email: shailendra.vandari@gmail.com


