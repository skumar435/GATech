## get the coordiates for clusters

import ast
data[:, 1]
coordinates = []
for row in data[:]:
    coordinates.append([row[1], ast.literal_eval(row[7])['latitude'], ast.literal_eval(row[7])['longitude']])
coordinates = pd.DataFrame(coordinates)
coordinates