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
land = land_data.variables['topo'][:]
#print(land.variables.keys()) //['lon', 'lat', 'topo']
