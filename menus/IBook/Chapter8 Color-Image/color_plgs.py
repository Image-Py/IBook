from imagepy.core.engine import Free
from imagepy.core import myvi
from imagepy import IPy
import numpy as np
from skimage.color import hsv2rgb

class RGBCube(Free):
	title = 'Show RGB Cube'
	asyn = False

	para = {'n':3}
	view = [(int, 'n', (1,8), 0, 'slices', '')]

	def run(self, para=None):
		n = para['n'] + 1
		xs = [np.linspace(0,1,n)]*n**2
		ys = list(np.arange(n**3).reshape((-1, n))//n%n/(n-1))
		zs = list(np.arange(n**3).reshape((-1, n))//n**2/(n-1))
		cs = [np.array((x,y,z)).T for x,y,z in zip(xs,ys,zs)]
		# cs[:] = myvi.util.auto_lookup(vts[:,2], myvi.util.linear_color('jet'))/255
		vts, fs, ns, cs = myvi.build_lines(xs, ys, zs, cs)
		manager = myvi.Manager()
		surf = manager.add_surf('X', vts, fs, ns, cs)
		surf.mode, surf.width = 'grid', 2

		cs = [np.array((x,y,z)).T for x,y,z in zip(ys,xs,zs)]
		vts, fs, ns, cs = myvi.build_lines(ys, xs, zs, cs)
		surf = manager.add_surf('Y', vts, fs, ns, cs)
		surf.mode, surf.width = 'grid', 2

		cs = [np.array((x,y,z)).T for x,y,z in zip(zs,ys,xs)]
		vts, fs, ns, cs = myvi.build_lines(zs, ys, xs, cs)
		surf = manager.add_surf('Z', vts, fs, ns, cs)
		surf.mode, surf.width = 'grid', 2

		myvi.Frame3D(IPy.curapp, 'RGB Cube', manager).Show()

class HSVPyramid(Free):
	title = 'Show HSV Pyramid'
	asyn = False

	para = {'angs':6, 'rings':2}
	view = [(int, 'angs', (6,64), 0, 'angles', ''),
			(int, 'rings', (1,8), 0, 'rings', '')]

	def run(self, para=None):
		n, angs = para['rings'], para['angs']+1
		a = np.linspace(0, np.pi*2, angs)
		xs, ys, zs, cs = [], [], [], []
		for r in np.arange(1,n+1)/n:
			xs.append(np.cos(a)*r)
			ys.append(np.sin(a)*r)
			zs.append([1]*angs)
			hsv = np.array([a/np.pi/2,[r]*angs,[1]*angs]).T
			rgb = hsv2rgb(hsv.reshape((-1,1,3)))
			cs.append(list(rgb.reshape((-1,3))))

		rr = np.hstack((np.arange(0, n+1)/n,[0]))
		xs.extend(list(np.cos(a).reshape((-1,1))*rr))
		ys.extend(list(np.sin(a).reshape((-1,1))*rr))
		zs.extend([[1]*n+[1,-1]]*angs)
		hsvs = [np.array(([h/np.pi/2]*(n+2), rr, [1]*n+[1,0])).T for h in a]
		rgbs = [hsv2rgb(i.reshape((-1,1,3))).reshape(-1,3) for i in hsvs]
		cs.extend([list(i) for i in rgbs])
		# cs[:] = myvi.util.auto_lookup(vts[:,2], myvi.util.linear_color('jet'))/255
		xs.append([0,0]); ys.append([0,0]); zs.append([1,-1])
		cs.append([(1,1,1),(0,0,0)])
		vts, fs, ns, cs = myvi.build_lines(xs, ys, zs, cs)
		manager = myvi.Manager()
		surf = manager.add_surf('X', vts, fs, ns, cs)
		surf.mode, surf.width = 'grid', 2

		myvi.Frame3D(IPy.curapp, 'HSV Pyramid', manager).Show()

plgs = [RGBCube, HSVPyramid]