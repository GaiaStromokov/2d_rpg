from config.gen_import import *
os.system('cls' if os.name == 'nt' else 'clear')


stats = np.zeros((4, 4), dtype=float)
stats[:3, :3] = 10.0

for i in range(3):
    for j in range(1, 3):
        stats[j, i] += stats[j - 1, i] * 0.1
    stats[3, i] = stats[:3, i].sum() * 0.33 
    stats[i, 3] = stats[i, :3].sum() * 0.33 
stats[3, 3] = stats.sum()
stats = stats.round(2)

print(stats)