

import numpy as np
import pandas as pd
isolates = []
in_file = '/projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/distances_input.csv'
out_file = '/projects/VirtualHost/predictb/tools/Comparative_Genomics/comp_gen_data/distance_matrix.csv'
with open(in_file, 'r') as f:
    for line in f:
        isolates.append(line.rstrip().split(',')[0].split('_')[0])
        isolates.append(line.rstrip().split(',')[1].split('_')[0])
        
isolates = list(set(isolates))
mat = np.zeros(shape=(len(isolates), len(isolates)))

with open(in_file, 'r') as f:
    for line in f:
        mat[isolates.index(line.rstrip().split(',')[0].split('_')[0])][isolates.index(line.rstrip().split(',')[1].split('_')[0])] = float(line.rstrip().split(',')[2])
        mat[isolates.index(line.rstrip().split(',')[1].split('_')[0])][isolates.index(line.rstrip().split(',')[0].split('_')[0])] = float(line.rstrip().split(',')[2])
        
dist_mat = [isolates]
dist_mat.extend(mat.tolist())
df = pd.DataFrame(dist_mat)
df.to_csv(out_file, header=None)
