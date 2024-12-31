import random
import math

def simulated_annealing(initial_state, objective_function, initial_temperature, cooling_rate, max_iterations, error_threshold):
    current_state = initial_state
    current_energy = objective_function(current_state)
    best_state = current_state
    best_energy = current_energy
    
    for iteration in range(max_iterations):
        new_state = [
            current_state[0] + random.uniform(-1, 1),
            current_state[1] + random.uniform(-1, 1) 
        ]
        
        new_state[0] = max(-10, min(10, new_state[0]))
        new_state[1] = max(-10, min(10, new_state[1]))
        
        
        new_energy = objective_function(new_state)
        delta_energy = new_energy - current_energy
        
        
        if delta_energy < 0:
            current_state = new_state
            current_energy = new_energy
            
            
            if current_energy < best_energy:
                best_state = current_state
                best_energy = current_energy
        else:
            
            acceptance_probability = math.exp(-delta_energy / initial_temperature)
            if random.uniform(0, 1) < acceptance_probability:
                current_state = new_state
                current_energy = new_energy
        
        
        initial_temperature *= (1 - cooling_rate)
        
        
        print(f"Iteration: {iteration + 1}, Current State: {current_state}, Energy: {current_energy}")
        
        
        if abs(best_energy) < error_threshold:
            break
    
    return best_state, best_energy


def objective_function(state):
    x, y = state
    return x**2 + y**2


initial_state = [4, 4]  
initial_temperature = 200  
cooling_rate = 0.01  
max_iterations = 1000 
error_threshold = 0.001  
best_state, best_energy = simulated_annealing(initial_state, objective_function, initial_temperature, cooling_rate, max_iterations, error_threshold)

print("Best state:", best_state)
print("Best energy:", best_energy)