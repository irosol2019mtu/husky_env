from collections import deque
import numpy as np
import matplotlib.pyplot as plt
             
# parameters
Zeta= 38
Eta = 120	
q_star = 10	
OSCILLATIONS_DETECTION_LENGTH = 3

# Main Function
def path(est_pos,X_map,Y_map):
	res=0.1	
	n=10/res
	ox = np.divide(X_map,res)
	oy = np.divide(Y_map,res)
	oy = np.add(oy,100)
	sx = int(round((est_pos[0])/res))	#@TODO 
	sy = int(round((est_pos[1])/res+100))	#@TODO 
	gx = 90				#@TODO 
	gy = 50					#@TODO 
	xw = 100				#@TODO 
	yw = 100			#@TODO 
	obs_radius =[5 for i in range(len(ox))]#@TODO set radius

	ix,iy = potential_field_planning(sx, sy, gx, gy, ox, oy, obs_radius, xw, yw)
#	plt.scatter(ox[2:-1],oy[2:-1])
#	plt.scatter(ix[2:-1],iy[2:-1])
	plt.scatter(ox,oy)
	plt.scatter(ix,iy)

	plt.show()
	return ix,iy

def potential_field_planning(sx, sy, gx, gy, ox, oy, obs_radius, xw, yw):
	#caculate potiential field
	pmap = cal_potential_field(gx, gy, ox, oy, obs_radius, sx, sy, xw, yw)
	d = np.hypot(sx - gx, sy - gy)
	ix, iy = sx, sy
	rx, ry = [sx], [sy]
	motion = get_motion_model()
	previous_ids = deque()
    
	while d >= 1:
		minp = float("inf")
		minix, miniy = -1, -1
		for i, _ in enumerate(motion):
			inx = int(ix + motion[i][0])
			iny = int(iy + motion[i][1])
			if inx >= len(pmap) or iny >= len(pmap[0]) or inx < 0 or iny < 0:
				p = float("inf")
				print("outside potential")
			else:
				p = pmap[inx][iny]
			if minp > p:
				minp = p
				minix = inx
				miniy = iny
		ix = minix
		iy = miniy
		d = np.hypot(gx - ix, gy - iy)
		rx.append(ix)
		ry.append(iy)

		if (oscillations_detection(previous_ids, ix, iy)):
			print("Osicillation detected at ({}, {})".format(ix, iy))
			break


	return rx, ry
                    

def cal_attractive_potential(x, y, gx, gy):
	d=np.hypot(x - gx, y - gy)
	return 0.5 * Zeta * d**2

def cal_repulsive_potential(x, y, ox, oy, obs_radius):
	#search nearest obstacle
	minid = -1
	dmin = float("inf")
	for i, _ in enumerate(ox):
		d = np.hypot(x - ox[i], y - oy[i]) - obs_radius[i]
		if dmin >= d:
			dmin = d
			minid = i

	#calculate repulsive potential 
	dq = np.hypot(x - ox[minid ], y - oy[minid]) - obs_radius[minid]
	if dq <= q_star:
		if dq <= 0.1:
			dq = 0.1
		return 0.5 * Eta * ((1.0 / dq) - (1.0 / q_star)) ** 2
	else: 
		return 0.0

def cal_potential_field(gx, gy, ox, oy, obs_radius, sx, sy, xw, yw):

	#calculate final potential 
	pmap = [[0.0 for i in range(yw)] for i in range(xw)]

	for x in range(xw):
		for y in range(yw):
			ug = cal_attractive_potential(x, y, gx, gy)
			uo = cal_repulsive_potential(x, y, ox, oy, obs_radius)
			pmap[x][y] = ug + uo

	return pmap

def get_motion_model():
	#dx, dy 
	motion = [[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]

	return motion

def oscillations_detection(previous_ids, ix, iy):
	previous_ids.append((ix, iy))

	if (len(previous_ids) > OSCILLATIONS_DETECTION_LENGTH):
		previous_ids.popleft()

	#check if contains any duplicates by copying into a set
	previous_ids_set = set()
	for index in previous_ids:
		if index in previous_ids_set:
			return True
		else:
			previous_ids_set.add(index)
	return False

if __name__ == '__main__':
	print("start!!")
	path()
	print("Done!!")


