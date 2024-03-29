import numpy as np
import skimage.data
import skimage.transform

def unflatten(arr):
    return np.reshape(arr, (32, 32, 3))

def crop(img, x1, y1, x2, y2):
	x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
	max_h, max_w = img.shape[0], img.shape[1]
	return skimage.util.crop(img,((y1, max_h - y2),(x1,max_w - x2),(0,0)), copy=False)

def process_image(img):
    # resizes image and flattens it (32*32*3 = 3072)
    img = skimage.transform.resize(img, (32, 32), mode='constant')
    img = np.asarray([img]).flatten()
    return img 