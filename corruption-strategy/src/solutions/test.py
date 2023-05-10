import pulp


def build_conections(n,m,a,w):

    conections = []
    mark = [[False for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(m):
                if i != j and not mark[i][j]:
                    mark[i][j] = True
                    mark[j][i]= True
                    
                    conections.append((i,j,))




# Crear el problema
prob = pulp.LpProblem("Proyecto de construccion de carreteras", pulp.LpMaximize)

# Crear las variables de decision
n = 3  # numero de ciudades
m = 4  # numero de carreteras
x = [pulp.LpVariable("x{}".format(i), cat=pulp.LpBinary) for i in range(m)]
z = [pulp.LpVariable("z{}".format(i), cat=pulp.LpBinary) for i in range(n)]

# Agregar la funcion objetivo
a = [5,15,4,7]  # aportes de cada ciudad
w = [10,20,3]  # costos de cada carretera
prob += pulp.lpSum([w[i] * x[i] for i in range(m)]) - pulp.lpSum([a[j] * z[j] for j in range(n)])

# Agregar las restricciones
for j in range(n):
    # Cada ciudad debe estar conectada por al menos una carretera
    prob += pulp.lpSum([x[i] for i in range(m) if i in conexiones[j]]) >= z[j]
for i in range(m):
    # Cada carretera solo se puede construir una vez
    prob += x[i] <= 1

# Resolver el problema
prob.solve()

# Imprimir la solucion
print("Status:", pulp.LpStatus[prob.status])
print("Objetivo:", pulp.value(prob.objective))
for v in prob.variables():
    print(v.name, "=", v.varValue)
