import numpy as np
import netCDF4 

sea = []
seaf = open("seal.txt", 'r')
seaf = list(seaf.read().split())
for i in range(len(seaf) // 2):
    t, h = int(seaf[2 * i]), float(seaf[2 * i + 1])
    sea.append([t, h])

# so now we have sea list, where s[i][0] - time and s[i][1] - sea level
out = open('ratio.txt', 'w')

land_data = netCDF4.Dataset('topo.nc')
land_temp = land_data.variables['topo'][:]
#для ускорения, python быстрее работает с линейными массивами ЗНАЧИТЕЛЬНО быстрее. 
land = [item for sublist in land_temp for item in sublist] 

#print(land.variables.keys()) //['lon', 'lat', 'topo']

for t, h in sea:
    count = 0
    for i in range(len(land)):
            if (land[i] > h):
                count += 1
    out.write(str(t) + ' ' + str(count / land_data.variables["topo"].shape[0] / land_data.variables["topo"].shape[1]) 
              + ' ')
    print('\r', t // 100, end = '     ')

out.close()