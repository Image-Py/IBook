from imagepy.core.engine import Filter
from imagepy.ipyalg import find_maximum, ridge, stair, isoline
from skimage.morphology import watershed
import scipy.ndimage as ndimg
import numpy as np
from imagepy import IPy

class Ridge(Filter):
    title = 'Riedge Sub'
    note = ['8-bit', 'not_slice', 'auto_snap', 'not_channel', 'preview']
    
    para = {'sigma':1.0, 'thr':0, 'ud':True}
    view = [(float, (0,5), 1, 'sigma', 'sigma', 'pix'),
            ('slide', (0,255), 'Low', 'thr', ''),
            (bool, 'ascend', 'ud'),]

    def load(self, ips):
        self.buflut = ips.lut
        ips.lut = ips.lut.copy()
        return True
    
    def preview(self, ips, para):
        ips.lut[:] = self.buflut
        if para['ud']:
            ips.lut[:para['thr']] = [0,255,0]
        else:
            ips.lut[para['thr']:] = [255,0,0]
        ips.update = 'pix'

    #process
    def run(self, ips, snap, img, para = None):
        self.ips.lut[:] = self.buflut
        img2 = ndimg.gaussian_filter(snap, para['sigma'])
        mark = img2<para['thr'] if para['ud'] else img2>para['thr']
        mark = mark.astype(np.uint8)
        ridge(img2, mark, para['ud'])
        imgs = []

        for i in range(0,255,10)[::1 if para['ud'] else -1]:
            msk = i>img if para['ud'] else i<img
            sl = img.copy()
            sl[msk] = mark[msk]
            imgs.append(sl)
        IPy.show_img(imgs, ips.title+'-ridgesub')

class Watershed(Filter):
    title = 'Watershed Sub'
    note = ['8-bit', 'not_slice', 'auto_snap', 'not_channel', 'preview']
    
    para = {'sigma':1.0, 'thr':0, 'ud':True}
    view = [(float, (0,5), 1, 'sigma', 'sigma', 'pix'),
            ('slide', (0,255), 'Low', 'thr', ''),
            (bool, 'ascend', 'ud'),]

    def load(self, ips):
        self.buflut = ips.lut
        ips.lut = ips.lut.copy()
        return True
    
    def preview(self, ips, para):
        ips.lut[:] = self.buflut
        if para['ud']:
            ips.lut[:para['thr']] = [0,255,0]
        else:
            ips.lut[para['thr']:] = [255,0,0]
        ips.update = 'pix'

    #process
    def run(self, ips, snap, img, para = None):
        self.ips.lut[:] = self.buflut
        ndimg.gaussian_filter(snap, para['sigma'], output=img)
        mark = img<para['thr'] if para['ud'] else img>para['thr']

        markers, n = ndimg.label(mark, np.ones((3,3)), output=np.uint16)
        buf = img if para['ud'] else 255-img
        mark = watershed(buf, markers, watershed_line=True)
        mark = np.multiply((mark==0), 255, dtype=np.uint8)
        imgs = []
        for i in range(0,255,10)[::1 if para['ud'] else -1]:
            msk = i>img if para['ud'] else i<img
            sl = img.copy()
            sl[msk] = mark[msk]
            imgs.append(sl)
        IPy.show_img(imgs, ips.title+'-ridgesub')

plgs = [Ridge, Watershed]