import matplotlib.pyplot as plt
from hw6_b06901090 import svd_compress
from PIL import Image
import numpy as np
import matplotlib
matplotlib.use('agg')


def load_image(img_path):
    """Load image into a 3D numpy array
    Arg:
        img_path: string, file path of the image file.
    Return:
        imArr: numpy array with shape (height, width, 3).
    """
    with Image.open(img_path) as im:
        imArr = np.fromstring(im.tobytes(), dtype=np.uint8)
        imArr = imArr.reshape((im.size[1], im.size[0], 3))
    return imArr


def save_image(imArr, fpath='output.jpg'):
    """Save numpy array as a jpeg file
    Arg:
        imArr: 2d or 3d numpy array, *** it must be np.uint8 and range from [0, 255]. ***
        fpath: string, the path to save imgArr.
    """
    im = Image.fromarray(imArr)
    im.save(fpath)


def plot_curve(k, err, fpath='curve.png', show=False):
    """Save the relation curve of k and approx. error to fpath
    Arg:
        k: a list of k, in this homework, it should be [1, 5, 50, 150, 400, 1050, 1289]
        err: a list of aprroximation error corresponding to k = 1, 5, 50, 150, 400, 1050, 1289
        fpath: string, the path to save curve
        show: boolean, if True: display the plot else save the plot to fpath
    """
    plt.gcf().clear()
    plt.plot(k, err, marker='.')
    plt.title('SVD compression')
    plt.xlabel('k')
    plt.ylabel('Approx. error')
    if show:
        plt.show()
    else:
        plt.savefig(fpath, dpi=300)


def approx_error(imArr, imArr_compressed):
    """Calculate approximation error 
    Arg:
        Two numpy arrays
    Return:
        A float number, approximation error
    """
    v = imArr.ravel().astype(float)
    u = imArr_compressed.ravel().astype(float)
    return np.linalg.norm(v - u) / len(v)


img_path = 'img/vegetable_english.jpg'
imArr = load_image(img_path)

ks = [1, 5, 50, 150, 400, 1050, 1289]
err = []
for k in ks:
    print("Perform SVD for k=%d ..." % k, end='\r')
    imArr_compressed = svd_compress(imArr, K=k)
    err += [approx_error(imArr, imArr_compressed)]
    save_image(imArr_compressed, 'result_{}.jpg'.format(k))

plot_curve(ks, err, show=False)
