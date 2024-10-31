import pulp
import numpy as np

np.random.seed(42)

num_land = 34
num_crops = 82
num_years = 7

sales_price = np.random.rand(num_land, num_crops, num_years)
planting_cost = np.random.rand(num_land, num_crops, num_years)
yield_per_mu = np.random.rand(num_land, num_crops, num_years)
expected_sales = np.random.rand(num_land, num_crops, num_years)

problem = pulp.LpProblem("Maximize_Profit_Random", pulp.LpMaximize)

x = pulp.LpVariable.dicts("x", ((i, j, t) for i in range(num_land) for j in range(num_crops) for t in range(num_years)), 0, 1, pulp.LpContinuous)

profit = pulp.lpSum(
    sales_price[i][j][t] * yield_per_mu[i][j][t] * x[(i, j, t)] - 
    planting_cost[i][j][t] * yield_per_mu[i][j][t] * x[(i, j, t)]
    for i in range(num_land) for j in range(num_crops) for t in range(num_years)
)
problem += profit

for i in range(num_land):
    for t in range(num_years):
        problem += pulp.lpSum(x[(i, j, t)] for j in range(num_crops)) == 1

problem.solve()

for v in problem.variables():
    if v.varValue > 0:
        print(f"{v.name} = {v.varValue}")

print(f"Total Profit = {pulp.value(problem.objective)}")
