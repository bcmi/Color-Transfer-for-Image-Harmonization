import numpy as np
from PIL import Image
from pillow_lut import rgb_color_enhance,load_cube_file


def get_f_b(real_img, mask, trans_img):
    real_img=np.array(real_img)
    mask=np.array(mask)
    trans_img=np.array(trans_img)

    mask = (1 - (mask == 0))
    mask = np.expand_dims(mask, axis=2)
    mask = mask.repeat(3, axis=2)

    out_img_np = mask * trans_img + (1 - mask) * real_img
    out_img = Image.fromarray(np.uint8(out_img_np))
    return out_img

def gen_fake(real_img_path, mask_path, random_lut):

    real_img=Image.open(real_img_path)
    mask=Image.open(mask_path)
    trans_img=real_img.filter(random_lut)

    fake_img=get_f_b(real_img, mask, trans_img)
    fake_img.save('output.jpg')
    return

if __name__ == '__main__':
    real_img_path = 'data/c172513.jpg'
    mask_path = 'data/c172513_1275867.jpg'
    lut_path = 'LUTs/300 - God King.cube'
    hefe = load_cube_file(lut_path)
    lut = rgb_color_enhance(hefe, exposure=0.2, contrast=0.1, vibrance=0.5, gamma=1.3)
    gen_fake(real_img_path, mask_path, lut)




















