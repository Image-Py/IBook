cell>None
Duplicate>{'name': 'cell-gray', 'stack': True}
8-bit>None
Duplicate>{'name': 'cell-msk', 'stack': True}
Threshold>{'thr1': 193, 'thr2': 255}
Fill Holes>None
Geometry Filter>{'con': '4-connect', 'inv': False, 'area': 1100.0, 'l': 0.0, 'holes': 0, 'solid': 0.0, 'e': 0.0, 'front': 255, 'back': 0}
Binary Opening>{'w': 3, 'h': 3}
Binary Watershed>{'tor': 1, 'con': False}
Intensity Filter>{'con': '4-connect', 'inten': 'cell-gray', 'max': 0.0, 'min': 0.0, 'mean': -140.0, 'std': 0.0, 'sum': 0.0, 'front': 255, 'back': 50}
Duplicate>{'name': 'cell-filter', 'stack': True}
Threshold>{'thr1': 0, 'thr2': 255}
Image Calculator>{'img1': 'cell', 'op': 'min', 'img2': 'cell-filter'}