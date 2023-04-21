# Quispe Soliz Matias Fernando

# SIS420 - Inteligencia Artificial

import random

key_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def fitness(password):
    total_distance = 0
    for i in range(len(password) - 1):
        current_key = password[i]
        next_key = password[i+1]
        current_pos = get_key_position(current_key)
        next_pos = get_key_position(next_key)
        distance = abs(current_pos[0] - next_pos[0]) + abs(current_pos[1] - next_pos[1])
        total_distance += distance
    return total_distance

def get_key_position(key):
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix[i])):
            if key_matrix[i][j] == key:
                return (i, j)

def select_parents(population):
    parent1 = tournament_selection(population)
    parent2 = tournament_selection(population)
    return parent1, parent2

def tournament_selection(population, tournament_size=3):
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda x: x[1])
    return tournament[0]

def crossover(parent1, parent2):
    split_index = random.randint(1, len(parent1) - 1)
    child1 = parent1[:split_index] + parent2[split_index:]
    child2 = parent2[:split_index] + parent1[split_index:]
    return child1, child2

def mutation(individual, mutation_rate=0.01):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(key_matrix) - 1)
            k = random.randint(0, len(key_matrix[j]) - 1)
            individual[i] = key_matrix[j][k]
    return individual

population_size = 100
num_generations = 1000
mutation_rate = 0.01
population = []
for i in range(population_size):
    password = [random.randint(1, 9) for _ in range(9)]
    fitness_value = fitness(password)
    population.append((password, fitness_value))

for generation in range(num_generations):
    parent1, parent2 = select_parents(population)
    child1, child2 = crossover(parent1[0], parent2[0])
    child1 = mutation(child1, mutation_rate)
    child2 = mutation(child2, mutation_rate)
    child1_fitness = fitness(child1)
    child2_fitness = fitness(child2)
    population.sort(key=lambda x: x[1], reverse=True)
    population[-2] = (child1, child1_fitness)
    population[-1] = (child2, child2_fitness)
    
    # Muestra el progreso del algoritmo cada 100 generaciones
    if (generation+1) % 100 == 0:
        print("Generación", generation+1, "| Mejor valor de aptitud:", population[0][1])
    
    # Si se encontró una solución óptima, finaliza el algoritmo
    if population[0][1] == 0:
        print("Se encontró una solución óptima en la generación", generation+1)
        break

best_password = population[0][0]
print("Contraseña generada por el algoritmo:", ''.join(map(str, best_password)))