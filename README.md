# Asynchronous Parallel Disassembly Planning with Genetic Algorithm

This repository contains a sample implementation inspired by the paper "An asynchronous parallel disassembly planning based on genetic algorithm".

## Problem Statement
- Utilizing an asynchronous parallel approach for disassembly planning.
- Employing Genetic Algorithm for optimization.

## Dataset
- The data for disassembly times and precedence/concurrent relationships among parts are included in the code.

## Code Structure
- `evaluate_chromosome`: Evaluates a chromosome to calculate the total disassembly time.
- `roulette_wheel_selection`: Performs roulette wheel selection.
- `tournament_selection`: Performs tournament selection.
- `generate_a1_a2_strings`: Generates A1 and A2 strings for crossover.
- `precedence_preservative_crossover`: Performs precedence-preservative crossover.
- `mutate_based_on_precedence`: Performs mutation while preserving precedence relationships.
- `improved_GA`: Main function to run the Genetic Algorithm.

## Usage
```bash
python disassembly_planning.py

## Output
- The code will output the best solution found over the iterations of the GA.
## References
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
