import numpy as np

def unbalanced_assignment(cost_matrix):
    n, m = cost_matrix.shape
    max_dim = max(n, m)
    # Pad the cost matrix with zeros to make it square
    C = np.zeros((max_dim, max_dim))
    C[:n, :m] = cost_matrix

    print(C)
    
    # Initialize the state array
    M = np.full((max_dim, max_dim), np.inf)
    M[0, 0] = 0
    
    # Compute the minimum cost for each pair (i, j)
    for i in range(1, max_dim):
        for j in range(1, max_dim):
            min_case_a = C[i-1, j-1] + M[i-1, j-1]
            min_case_b = M[i, j-1]
            M[i, j] = min(M[i, j], min_case_a, min_case_b)

        print(M)
    
    # Return the optimal solution
    return M[n, m]


def dynamic_solution(n,p,k,a,s):
    
    return unbalanced_assignment(s)
