import cvxpy as cp
import numpy as np
import pandas as pd

# Parameters
num_land = 54
num_crops = 82
t = 1  # Fixed for now

# Create model
model = cp.Problem(cp.Maximize)

# Decision variables
x = cp.Variable((num_land, num_crops), nonneg=True)
z = cp.Variable((num_land, num_crops), boolean=True)

# Load data
Pjt = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='销售价格Pj').to_numpy()[0][1:].astype(float)
qjt = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='销售量qj').to_numpy()[0][1:].astype(float)
Si = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='地块面积Si').iloc[:, 2].to_numpy().astype(float)
Dijt = np.delete(pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='亩产Dij').to_numpy(), 0, axis=1).astype(float)
Cijt = np.delete(pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='成本Cij').to_numpy(), 0, axis=1).astype(float)

# Robust parameters
def robust_parameters():
    sales_volume_change = np.array([np.random.uniform(0.95, 1.05) for _ in range(num_crops)])
    yield_change = np.array([np.random.uniform(0.9, 1.1) for _ in range(num_crops)])
    cost_increase = np.array([np.random.uniform(1.05, 1.05) for _ in range(num_crops)])
    price_change = np.array([np.random.uniform(0.95, 1.05) if i >= 41 else 1.0 for i in range(num_crops)])
    return sales_volume_change, yield_change, cost_increase, price_change

sales_volume_change, yield_change, cost_increase, price_change = robust_parameters()

# Objective: Maximize profit
revenue = cp.sum([Pjt[j] * cp.sum(Si[i] * Dijt[i, j] * x[i, j] for i in range(num_land)) for j in range(num_crops)])
cost = cp.sum([Si[i] * Dijt[i, j] * x[i, j] * Cijt[i, j] * cost_increase[j] for i in range(num_land) for j in range(num_crops)])
profit = revenue - cost

# Set objective
model = cp.Problem(cp.Maximize(profit))

# Constraints
constraints = []

# Each land's crop ratio sum to 1
for i in range(num_land):
    constraints.append(cp.sum(x[i, :]) == 1)

# x[i][j] <= z[i][j]
for i in range(num_land):
    for j in range(num_crops):
        constraints.append(x[i, j] <= z[i, j])

# Restrict specific crops on certain lands
for i in range(27, 35):
    for j in list(range(1, 16)) + list(range(35, 57)) + list(range(58, 76)) + list(range(79, 82)):
        constraints.append(x[i, j] == 0)

for i in range(51, 54):
    for j in list(range(1, 17)) + list(range(35, 58)) + list(range(76, 82)):
        constraints.append(x[i, j] == 0)

for i in range(35, 51):
    for j in list(range(1, 17)) + list(range(35, 79)):
        constraints.append(x[i, j] == 0)

# Add constraints to model
model.constraints = constraints

# Solve model
model.solve()

# Print results
print("Optimal value:", model.value)
for i in range(num_land):
    for j in range(num_crops):
        if x[i, j].value > 0:
            print(f"Land {i + 1}, Crop {j}: {x[i, j].value}")

# Save results
result_df = pd.DataFrame(x.value, columns=[f'Crop_{i}' for i in range(num_crops)])
result_df.to_excel('robust_optimization_results.xlsx', index=False)
