# from imagepy import IPy
from sciapp.action import Free
from scipy.misc import imread
import os.path as osp

class Data(Free):
	def __init__(self, name):
		self.name = name
		self.title = name.split('.')[0]

	def run(self, para = None):
		root_dir = osp.abspath(osp.dirname(__file__))
		img = imread(osp.join(root_dir, self.name))
		if img.ndim==3 and img.shape[2]==4:
			img = img[:,:,:3].copy()
		self.app.show_img([img], self.title)

	def __call__(self):
		return self

datas = ['Angkor.jpg','qrcode.png','street.jpg','road.jpg','house.jpg',
'neubauer.jpg','windmill.jpg','sunglow.jpg','ailurus.jpg','Yuan.jpg',
'saltpepper.jpg','dem.jpg', 'honeycomb.jpg', 'necklace.jpg','universe.jpg',
'towel-far.jpg','towel-near.jpg','trafficsign.jpg','bee.png','insect.png',
'game.jpg','gear.png','block.png','distance.png','points.png', 'qin.png', 
'img.png','pointline.png','marble.png','cell.jpg','rust.jpg', 'rose.jpg',
'roses.jpg','rgb.PNG','cmyk.png']

plgs = [Data(i) for i in datas]
