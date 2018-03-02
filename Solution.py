# Create array to hold iterations required each test
all_iterations = []

# Perform number of trials to compute average runs needed
for i in range(0,50):
    # Perform same initial search to find local max
    s = Problem()
    sn = s.get_node()
    local_max = hill_climb(s)
    hits = local_max.compute_value()
    iterations = 0
    
    # Loop a random restart until solution found
    while hits > 0:
        rand = np.random.randint(8,size=8)
        sn.set_state(rand)
        local_max = hill_climb(s)
        hits = local_max.compute_value()
        iterations += 1
    
    # Add print solution and save num of iterations taken
    #print("Solution %d is:" % (i+1), local_max.get_state(), "\t Iterations required:", iterations)
    all_iterations.append(iterations)

# Print result
print("Mean iterations:", np.mean(all_iterations))
print("Final solution found:", local_max.get_state())