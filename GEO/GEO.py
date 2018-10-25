import numpy as np
import netCDF4 

def make_haste(t, i, j):
    #dont read this
    #mask of altitudes within range of bigger scale altitude step
    msk_lat = [k for k in range(len(land_data.variables['lat'][:])) if(land_data.variables['lat'][:][k] > frozen_data.variables['lat'][:][i]) & (land_data.variables['lat'][:][k] < frozen_data.variables['lat'][:][i + 1])]
    #mask of lon...
    msk_lon = [12 * j + k for k in range(12)]

    count_all = len(msk_lat) * len(msk_lon)
    count_above = 0
    for k in msk_lat:
        for z in msk_lon:
            if (sea[t][1] < land[k][z]):
                count_above += 1
    if (count_above == count_all):
        return 1, 0
    elif(count_above == 0):
        return 0, 0
    else:
        return 0, 1

sea = []
seaf = open("seal.txt", 'r')
seaf = list(seaf.read().split())
for i in range(len(seaf) // 2):
    t, h = int(seaf[2 * i]), float(seaf[2 * i + 1])
    sea.append([t, h])

# so now we have sea list, where s[i][0] - time and s[i][1] - sea level
land_data = netCDF4.Dataset('topo.nc')
land = land_data.variables['topo'][:]

#print(land.variables.keys()) //['lon', 'lat', 'topo']
frozen_data = netCDF4.Dataset('dptmask65.nc')
frozen = frozen_data.variables['dp'][:, 0, :, :] #['time', 'lon', 'lat', 'lev', 'dp']


out = open('frozen_ratio.txt', 'w')
for t in range(len(frozen_data.variables['time'][:])):
    print('\r', t, end = '     ')
    count_complete = 0
    count_incomplete = 0
    count = 0
    for i in range(frozen_data.variables['lat'].shape[0]): #be carefull to minus 1 due to 90 == -90
        for j in range(frozen_data.variables['lon'].shape[0]): 
            count += 1
            if frozen[t, i, j]:
                a, b = make_haste(t, i, j) #a mean if complete, b mean if incomplete, a = b = 0 mean sink
                count_complete += a
                count_incomplete += b
    out.write(str(sea[t][0]) + ' ' + str(count_complete / count) + ' ' + str(count_incomplete / count) + ' ')