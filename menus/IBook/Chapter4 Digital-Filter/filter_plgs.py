from imagepy.core.engine import Free
import scipy.ndimage as ndimg
import numpy as np, wx
# from imagepy import IPy
#matplotlib.use('WXAgg')
import matplotlib.pyplot as plt

def block(arr):
	img = np.zeros((len(arr),30,30), dtype=np.uint8)
	img.T[:] = arr
	return np.hstack(img)

class Temperature(Free):
	title = 'Temperature Difference'
	asyn = False

	def run(self, para = None):
		xs = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
		ys = np.array([1,2,1,2,2,3,8,9,8,10,9,10], dtype=np.float32)
		ds = ndimg.convolve1d(ys, [0,1,-1])
		lbs = ['Jan','Feb','Mar','Apr','May','June',
		       'Jul','Aug','Sep','Oct','Nov','Dec']
		plt.xticks(xs, lbs)

		plt.plot(xs, ys, '-o', label='Temperature')
		plt.plot(xs, ds, '-o', label='Difference')
		plt.grid()
		plt.gca().legend()

		plt.title('Temperature in XX')
		plt.xlabel('Month')
		plt.ylabel('Temperature (C)')

		plt.show()
		self.app.show_img([block((ys-ys.min())*(180/ys.max()-ys.min()))], 'Temperature')
		self.app.show_img([block((ds-ds.min())*(180/ds.max()-ds.min()))], 'Difference')

class Shake(Free):
	title = 'Shake Damping'
	asyn = False

	def run(self, para = None):
		xs = np.array([1,2,3,4,5,6,7,8,9,10])
		ys = np.array([10,-9,8,-7,6,-5,4,-3,2,-1], dtype=np.float32)
		ds = ndimg.convolve1d(ys, [1/3,1/3,1/3])
		print(ds)
		plt.plot(xs, ys, '-o', label='Shake')
		plt.plot(xs, ds, '-o', label='Damping')
		plt.grid()
		plt.gca().legend()

		plt.title('Shake Damping')
		plt.xlabel('Time')
		plt.ylabel('Amplitude')
		plt.show()
		self.app.show_img([block(ys*10+128)], 'Shake')
		self.app.show_img([block(ds*10+128)], 'Damping')

class Inertia(Free):
	title = 'Psychological Inertia'
	asyn = False

	def run(self, para = None):
		xs = np.array([1,2,3,4,5,6,7,8,9,10])
		ys = np.array([90,88,93,95,91,70,89,92,94,89], dtype=np.float32)
		ds = ndimg.convolve1d(ys, [1/3,1/3,1/3])
		print(ds)
		plt.plot(xs, ys, '-o', label='Psychological')
		plt.plot(xs, ds, '-o', label='Inertia')
		plt.grid()
		plt.gca().legend()

		plt.title('Psychological Inertia')
		plt.xlabel('Time')
		plt.ylabel('Score')
		plt.show()
		self.app.show_img([block((ys-80)*3+80)], 'Psychological')
		self.app.show_img([block((ds-80)*3+80)], 'Inertia')

class GaussCore(Free):
	title = 'Gaussian Core'
	asyn = False

	def run(self, para = None):
		x, y = np.ogrid[-3:3:10j, -3:3:10j]
		z = np.exp(-(x ** 2 + y ** 2)/1)
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.plot_wireframe(x, y, z)
		z = np.exp(-(x ** 2 + y ** 2)/4)
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.plot_wireframe(x, y, z)
		plt.show()

class LoGCore(Free):
	title = 'Laplace of Gaussian Core'
	asyn = False

	def run(self, para = None):
		plt.figure()
		x = np.linspace(-3,3,50)
		y = np.exp(-x**2)
		dy = np.exp(-x**2)*(4*x**2-2)
		plt.plot(x, y, label='Gauss')
		plt.plot(x, -dy, label="Gauss''")
		plt.grid()
		plt.legend()
		x, y = np.ogrid[-3:3:20j, -3:3:20j]
		z = (4*x**2-2)*np.exp(-y**2-x**2)+(4*y**2-2)*np.exp(-x**2-y**2)
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.plot_wireframe(x, y, -z)
		plt.show()


class DogCore(Free):
	title = 'Difference of Gaussian Core'
	asyn = False

	def run(self, para = None):
		plt.figure()
		x = np.linspace(-3,3,50)
		y = np.exp(-x**2)
		yy = np.exp(-x**2/4)/2
		plt.plot(x, y, label='sigma = 1')
		plt.plot(x, yy, label='sigma = 2')

		plt.plot(x, y-yy, 'r', lw=3, label="Difference")
		plt.grid()
		plt.legend()
		x, y = np.ogrid[-3:3:20j, -3:3:20j]
		z = np.exp(-(x ** 2 + y ** 2)/1)-np.exp(-(x ** 2 + y ** 2)/4)/2
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.plot_wireframe(x, y, z)
		plt.show()

class LaplaceSharp(Free):
	title = 'Show how to Laplace Sharp'
	asyn = False

	def run(self, para = None):
		x = np.linspace(-10,10,300)
		y = np.arctan(x)

		fig, axes = plt.subplots(nrows=2, ncols=2)
		ax0, ax1, ax2, ax3 = axes.flatten()
		ax0.set_title('y = arctan(x)')
		ax0.plot(x, y)
		ax0.grid()
		ax1.set_title("y = arctan(x)'")
		ax1.plot(x, y)
		ax1.plot(x, 1/(x**2+1))
		ax1.grid()
		ax2.set_title("y = arctan(x)''")
		ax2.plot(x, y)
		ax2.plot(x, (2*x)/(x**4+2*x**2+1))
		ax2.grid()
		ax3.set_title("y = arctan(x) + arctan(x)''")
		ax3.plot(x, y)
		ax3.plot(x, y+(2*x)/(x**4+2*x**2+1))
		ax3.grid()
		fig.tight_layout()
		plt.show()
		self.app.show_img([(((y*70)+128)*np.ones((30,1))).astype(np.uint8)], 'tan(x)')
		self.app.show_img([((100/(x**2+1))*np.ones((30,1))).astype(np.uint8)], "tan(x)'")
		self.app.show_img([((((2*x)/(x**4+2*x**2+1)*70)+128)*
			np.ones((30,1))).astype(np.uint8)], "tan(x))''")
		self.app.show_img([((((y+(2*x)/(x**4+2*x**2+1))*70)+128)*
			np.ones((30,1))).astype(np.uint8)], "tan(x)+tan(x)''")

class UnSharp(Free):
	title = 'Show how to Unsharp Mask'
	asyn = False

	def run(self, para = None):
		x = np.linspace(-10,10,300)
		y = np.arctan(x)
		fig, axes = plt.subplots(nrows=2, ncols=2)
		ax0, ax1, ax2, ax3 = axes.flatten()
		gy = ndimg.gaussian_filter1d(y, 30)
		ax0, ax1, ax2, ax3 = axes.flatten()
		ax0.set_title('y = arctan(x)')
		ax0.plot(x, y)
		ax0.grid()
		ax1.set_title("gaussian")
		ax1.plot(x, y)
		ax1.plot(x, gy)
		ax1.grid()
		ax2.set_title("y = arctan(x) - gaussian")
		ax2.plot(x, y)
		ax2.plot(x, y-gy)
		ax2.grid()
		ax3.set_title("y = arctan(x) + diff")
		ax3.plot(x, y)
		ax3.plot(x, y+2*(y-gy))
		ax3.grid()
		fig.tight_layout()
		plt.show()
		self.app.show_img([((y*70+128)*np.ones((30,1))).astype(np.uint8)], 'tan(x)')
		self.app.show_img([((gy*70+128)*np.ones((30,1))).astype(np.uint8)], 'gaussian')
		self.app.show_img([(((y-gy)*100+128)*np.ones((30,1))).astype(np.uint8)], 'arctan(x) - gaussian')
		self.app.show_img([(((y+2*(y-gy))*70+128)*np.ones((30,1))).astype(np.uint8)], "arctan(x) + diff")

plgs = [Temperature, Shake, Inertia, GaussCore, LoGCore, DogCore, LaplaceSharp, UnSharp]