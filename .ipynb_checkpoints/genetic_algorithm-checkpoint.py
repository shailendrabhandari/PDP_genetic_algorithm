'''Copyright [2023] [Bhandari Shailendra]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.'''

import random

# Sample data
DISASSEMBLY_TIMES = {
    'M1': {1: 2, 2: 8, 3: 1, 4: 9, 5: 1, 6: 4, 7: 9, 8: 1, 9: 4, 10: 6},
    'M2': {1: 3, 2: 7, 3: 5, 4: 9, 5: 2, 6: 1, 7: 9, 8: 8, 9: 4, 10: 6}
}
P = {
    2: [1],      # part 1 should be disassembled before part 2
    3: [1, 2],   # parts 1 and 2 should be disassembled before part 3
    5: [4],      # part 4 should be disassembled before part 5
    7: [6],      # part 6 should be disassembled before part 7
    9: [8]       # part 8 should be disassembled before part 9
}

C = {
    4: [5],      # parts 4 and 5 cannot be disassembled at the same time
    6: [7]       # parts 6 and 7 cannot be disassembled at the same time
}

# GA parameters
MaxIte = 100
PopSize = 100
pc = 0.5
pm = 0.2
elitism_factor = 0.1  # Percentage of best individuals to carry forward

def evaluate_chromosome(chromosome):
    v1, v2 = chromosome
    total_disassembly_time = 0
    CT = {}

    for i, part in enumerate(v1):
        manipulator = v2[i]

        # Calculate start time (STi)
        AND_predecessors = P.get(part, [])
        same_manipulator_predecessors = [p for idx, p in enumerate(v1) if idx < i and v2[idx] == manipulator]
        conflicting_parts = C.get(part, [])

        max_completion_time = max_completion_time = max([CT.get(p, 0) for p in AND_predecessors + same_manipulator_predecessors + conflicting_parts], default=0)


        DTi = DISASSEMBLY_TIMES[f"M{manipulator}"][part]
        CT[part] = max_completion_time + DTi
        total_disassembly_time = max(total_disassembly_time, CT[part])

    return total_disassembly_time


def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    selection_probs = [f / total_fitness for f in fitness_values]
    r = random.random()
    for i, prob in enumerate(selection_probs):
        r -= prob
        if r <= 0:
            return population[i]
def tournament_selection(population, fitness_values, tournament_size=3):
    """
    Perform tournament selection.
    
    Args:
    - population: The entire population.
    - fitness_values: List of fitness values corresponding to each individual in the population.
    - tournament_size: Number of individuals participating in each tournament.
    
    Returns:
    - selected_individual: The winner of the tournament.
    """
    
    # Randomly select 'tournament_size' individuals
    tournament_individuals = random.sample(list(zip(population, fitness_values)), tournament_size)
    
    # Sort them by their fitness. Depending on your problem, this could be a min or max sort.
    # Here, I'm assuming a minimization problem based on your fitness computation. 
    # If it's a maximization problem, reverse the sorting.
    tournament_individuals.sort(key=lambda x: x[1])
    
    # Return the best individual from the tournament
    selected_individual = tournament_individuals[0][0]
    return selected_individual


def generate_a1_a2_strings(chromosome):
    v1 = chromosome[0]
    a1 = [len(P.get(part, [])) for part in v1]  # Number of predecessors for each part
    a2 = [i - sum([1 for p in P.get(part, []) if p in v1[:i]]) for i, part in enumerate(v1)]
    return a1, a2

def precedence_preservative_crossover(parent1, parent2):
    v1_1, v2_1 = parent1
    v1_2, v2_2 = parent2
    
    a1_1, a2_1 = generate_a1_a2_strings(parent1)
    a1_2, a2_2 = generate_a1_a2_strings(parent2)
    
    point = random.randint(1, len(v1_1) - 1)  # Crossover point
    offspring1_v1 = v1_1[:point] + [part for part in v1_2 if part not in v1_1[:point]]
    offspring2_v1 = v1_2[:point] + [part for part in v1_1 if part not in v1_2[:point]]
    
    # Crossover for v2 based on the a1 and a2 values
    offspring1_v2 = []
    offspring2_v2 = []
    for i in range(len(v2_1)):
        if a1_1[i] < a1_2[i] or (a1_1[i] == a1_2[i] and a2_1[i] <= a2_2[i]):
            offspring1_v2.append(v2_1[i])
            offspring2_v2.append(v2_2[i])
        else:
            offspring1_v2.append(v2_2[i])
            offspring2_v2.append(v2_1[i])
    
    offspring1 = (offspring1_v1, offspring1_v2)
    offspring2 = (offspring2_v1, offspring2_v2)
    
    return offspring1, offspring2


def mutate_based_on_precedence(chromosome):
    v1, v2 = chromosome[:]
    valid_indices = [i for i, part in enumerate(v1) if not P.get(part)]
    
    if len(valid_indices) < 2:
        return chromosome  # No mutation possible without breaking precedence
    
    idx1, idx2 = random.sample(valid_indices, 2)
    v2[idx1], v2[idx2] = v2[idx2], v2[idx1]
    return v1, v2


def improved_GA():
    population = [(random.sample(range(1, 11), 10), [random.randint(1, 2) for _ in range(10)]) for _ in range(PopSize)]
    fitness_values = [1 / evaluate_chromosome(ch) for ch in population]
    best_chromosome = min(population, key=evaluate_chromosome)
    previous_best_fitness = 1 / evaluate_chromosome(best_chromosome)
    
    # Dynamic mutation rate
    stagnant_generations = 0
    dynamic_pm = pm

    # Elitism: select top x% of the population to carry forward
    num_elites = int(elitism_factor * PopSize)
    
    iteration = 0
    while iteration < MaxIte:
        new_population = population[:num_elites]  # Start with elites
        
        while len(new_population) < PopSize:
            parent1 = tournament_selection(population, fitness_values, tournament_size=3)

            
            if random.random() < pc:
                parent2 = tournament_selection(population, fitness_values, tournament_size=3)
                while parent2 == parent1:  # Ensure we select two different parents
                    parent2 = tournament_selection(population, fitness_values, tournament_size=3)
                offspring1, offspring2 = precedence_preservative_crossover(parent1, parent2)
                new_population.extend([offspring1, offspring2])

            if random.random() < dynamic_pm and len(new_population) < PopSize:
                mutated_chromosome = mutate_based_on_precedence(parent1)
                new_population.append(mutated_chromosome)

        population = new_population
        fitness_values = [1 / evaluate_chromosome(ch) for ch in population]
        current_best = min(population, key=evaluate_chromosome)
        current_best_fitness = 1 / evaluate_chromosome(current_best)

        # Adjust mutation rate if fitness is stagnant
        if current_best_fitness <= previous_best_fitness:
            stagnant_generations += 1
        else:
            stagnant_generations = 0
        
        if stagnant_generations >= 5:  # Threshold of 5 generations of stagnant fitness
            dynamic_pm *= 1.05  # Increase mutation rate by 5%
            if dynamic_pm > 1:
                dynamic_pm = 1
            stagnant_generations = 0

        # Print the best solution for the current iteration
        print(f"Iteration {iteration+1}: Best Solution = {current_best} with fitness = {current_best_fitness}")

        previous_best_fitness = current_best_fitness
        iteration += 1

    return min(population, key=evaluate_chromosome)

solution = improved_GA()
print("Best Solution:", solution)
