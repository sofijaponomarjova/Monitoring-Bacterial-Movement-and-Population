import numpy as np
import math

file_name = "/Users/admin/Desktop/lab_project/DataFiles/output-Set1.txt"   # change this
ids = ["211", "-211", "321", "-321", "2212", "-2212",
       "3122", "-3122", "3312", "-3312", "3334", "-3334"]

# collect momentum per strain from one file
momenta = {i: [] for i in ids}
with open(file_name) as f:
    for line in f:
        v = line.split()
        if len(v) == 4 and v[3] in momenta:
            px, py, pz = float(v[0]), float(v[1]), float(v[2])
            momenta[v[3]].append(math.sqrt(px**2 + py**2 + pz**2))

# overall range
all_p = np.concatenate([np.array(m) for m in momenta.values()])
print(f"min:  {all_p.min():.3f}")
print(f"95%:  {np.percentile(all_p, 95):.3f}")
print(f"99%:  {np.percentile(all_p, 99):.3f}")
print(f"max:  {all_p.max():.3f}\n")

# per-strain 99th percentile (check that the ranges are similar)
for i in ids:
    print(f"{i:>6}: n={len(momenta[i]):>8}, 99% = {np.percentile(momenta[i], 99):.3f}")

# try bins
top = np.percentile(all_p, 99)   # round this up to a clean number after looking
n_bins = 8
edges = np.linspace(0, top, n_bins + 1)
print("\nedges:", np.round(edges, 3))

# rarest strains: are the bins filled enough?
for i in ["3334", "-3334", "3312", "-3312"]:
    counts, _ = np.histogram(momenta[i], bins=edges)
    print(f"{i:>6}: {counts}")