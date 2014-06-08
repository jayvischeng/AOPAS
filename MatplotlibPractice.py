import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
"""x=np.arange(0, 5, 0.1)
lines=plt.plot(x, x*x, x, x)
#print type(plt.plot(x, x*x)) 

#plt.plot(x, x*x)
lines[0].set_antialiased(False)
print lines[0]
print lines[1]
print plt.getp(plt.gca())
#lines=plt.plot(x, np.sin(x), x, np.cos(x))
#plt.setp(lines, color="r", linewidth=2.0)
plt.show()
"""
#m = Basemap(llcrnrlon=72, llcrnrlat=1, urcrnrlon=138,\
#urcrnrlat=65, projection='lcc', lat_1=1, lat_2=80,\
#lon_0=-95, resolution='h', area_thresh=10000)
#m.bluemarble()
#m.drawcoastlines()
# draw country boundaries
#m.drawcountries(linewidth=2)
# draw states boundaries (America only)
#m.drawstates()
#print "AAAa"
# fill the background (the oceans)
#m.drawmapboundary(fill_color='aqua')
# fill the continental area
# we color the lakes like the oceans
#m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians
#m.drawparallels(np.arange(25,65,20),labels=[1,0,0,0])
#m.drawmeridians(np.arange(-120,-40,20),labels=[0,0,0,1])
#plt.show()
#--------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
x,y=np.mgrid[-2:2:20j,-2:2:20j]
z=x*np.exp(-x**2-y**2)
ax=plt.subplot(111,projection='3d')
#ax.plot_surface(x,y,z)
ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')
plt.show()

#--------------------------------------------------------------------------------
