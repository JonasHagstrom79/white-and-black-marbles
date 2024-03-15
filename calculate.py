import random

def simulate_balls():
    # Initialize the bowl with 25 white and 25 black balls
    bowl = ['white']*25 + ['black']*25
    
    while len(bowl) > 1:
        # Randomly pick two balls from the bowl
        ball1 = bowl.pop(random.randint(0, len(bowl)-1))
        ball2 = bowl.pop(random.randint(0, len(bowl)-1))
        
        if ball1 == ball2:
            # If both balls are of the same color, add one white ball to the bowl
            bowl.append('white')
        else:
            # If balls are of different colors, do not add the white one back (it simulates removing it)
            # No need to explicitly add a black ball back to the bowl since one is already removed
            pass  # This line is just a placeholder; no action is needed
    
    # Check if the bowl is empty before returning the last ball
    if bowl:
        return bowl[0]
    else:
        # Return a message or handle the case where the bowl is unexpectedly empty
        return "Bowl is empty"

# Simulate the process a large number of times to estimate the probability
num_simulations = 10000
results = [simulate_balls() for _ in range(num_simulations)]
probability_white = results.count('white') / num_simulations

print(f"Probability of the last ball being white: {probability_white}")