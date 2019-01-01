from PIL import Image
import numpy as np
import matplotlib


def load_image(img_path):
    """Load image into a 3D numpy array
    Arg:
        img_path: string, file path of the image file.
    Return:
        imArr: numpy array with shape (height, width, 3).
    """
    with Image.open(img_path) as im:
        imArr = np.fromstring(im.tobytes(), dtype=np.uint8)
        # imArr = imArr.reshape((im.size[1], im.size[0]))
        imArr = imArr.reshape((im.size[1], im.size[0], 3))
    return imArr


def load_image2(img_path):
    """Load image into a 3D numpy array
    Arg:
        img_path: string, file path of the image file.
    Return:
        imArr: numpy array with shape (height, width, 3).
    """
    with Image.open(img_path) as im:
        imArr = np.fromstring(im.tobytes(), dtype=np.uint8)
        imArr = imArr.reshape((im.size[1], im.size[0]))
        # imArr = imArr.reshape((im.size[1], im.size[0], 3))
    return imArr


def save_image(imArr, fpath='output.jpg'):
    """Save numpy array as a jpeg file
    Arg:
        imArr: 2d or 3d numpy array, *** it must be np.uint8 and range from [0, 255]. ***
        fpath: string, the path to save imgArr.
    """
    im = Image.fromarray(imArr)
    im.save(fpath)


def svd_compress(imArr, K=50):
    """Compress image array using SVD decomposition.
    Arg:
        imArr: numpy array with shape (height, width, 3).
    Return:
        Compressed imArr: numpy array.
    """
    imArr_compressed = np.zeros(imArr.shape)
    # For each channel
    for ch in range(3):
        # --------------------
        # TODO:
        #     Compress the image array using SVD decomposition
        # hint:
        #     1. numpy.linalg.svd
        #     2. numpy.diag
        #     3. numpy.dot
        #
        # Your code here
        # imArr_compressed = ??
        #
        # --------------------
        U, sigma, VT = np.linalg.svd(imArr[:, :, ch], full_matrices=False)
        sigma[K:] = 0.
        imArr_compressed[:, :, ch] = np.dot(U*sigma, VT)
        # Make imArr_compressed range from 0 to 255
        imArr_compressed[:, :, ch] -= imArr_compressed[:, :, ch].min()
        imArr_compressed[:, :, ch] /= imArr_compressed[:, :, ch].max()
        imArr_compressed[:, :, ch] *= 255
        # Return uint8 because save_image needs input of type uint8
    return imArr_compressed.astype(np.uint8)


if __name__ == "__main__":
    img_path = 'img/vegetable_english.jpg'
    imArr = load_image(img_path)
    save_image(svd_compress(imArr, 1)[:, :, 1], 'test/test0.jpg')
    """
    a = []
    for i in range(0, 5):
        imArr_compressed = np.zeros(imArr.shape)
        print(i)
        ch = 1
        U, sigma, VT = np.linalg.svd(imArr[:, :, ch], full_matrices=False)
        sigma[0:i] = 0.
        sigma[i+1:] = 0.
        # sigma[i] /=
        imArr_compressed[:, :, ch] = np.dot(U*sigma, VT)
        # Make imArr_compressed range from 0 to 255
        imArr_compressed[:, :, ch] -= imArr_compressed[:, :, ch].min()
        imArr_compressed[:, :, ch] /= imArr_compressed[:, :, ch].max()
        # imArr_compressed[:, :, ch] *= 255
        # imArr_compressed[..., 0] = 0.
        # imArr_compressed[..., 2] = 0.
        imArr_compressed = imArr_compressed[:, :, 1]
        print(imArr_compressed.shape)
        a.append(imArr_compressed)
        imArr_compressed = imArr_compressed.astype(np.uint8)
        print(imArr_compressed.shape)
        save_image(imArr_compressed, 'test/test'+str(i)+'.jpg')
    b = (sum(a)/len(a)*255)
    b = b.astype(np.uint8)
    save_image(b, 'img3.jpg')
    # """
    """
    img = load_image2('test/test0.jpg')
    for i in range(1, 5):
        print(i)
        try:
            img += load_image2('test/test'+str(i)+'.jpg')
        except:
            pass
    # print(max(img[0]))
    save_image(img, 'img.jpg')
    """
