# Color-Transfer-for-Image-Harmonization
Training deep image harmonization network requires abundant pairs of composite images and harmonized images, which are very hard to acquire in practice. **An achievable approach is adjusting the foreground of real images to produce synthetic composite images, leading to pairs of synthetic composite images and real images.** Here, we summarize different color transfer strategies which could be used to adjust the foregrounds of real images.


### Traditional Color Transfer Methods

To generate synthesized composite images, traditional color transfer methods can be adopted to transfer color information from reference images to real images. We categorize previous color transfer methods into four groups based on parametric/non-parametric and correlated/decorrelated color space, and select one representative method from each group. We provide the  implementation of the following four representative methods specialized for foreground color transfer in this repository. 

- global color transfer: Parametric method in decorrelated color space. Implementation of paper "*Color transfer between images*" [[pdf]](https://www.cs.tau.ac.il/~turkel/imagepapers/ColorTransfer.pdf).

- global color transfer in RGB color space: Parametric method in correlated color space. Implementation of paper "*Color transfer in correlated color space*" [[pdf]](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.530.2757&rep=rep1&type=pdf).

- cumulative histogram mapping: Non-parametric method in decorrelated color space. Implementation of paper  "*Histogram-based prefiltering for luminance and chrominance compensation of multiview video*" [[pdf]](https://ieeexplore.ieee.org/document/4539698).

- IDT regrain color transfer: Non-parametric method in correlated color space. Implementation of paper  "*Automated colour grading using colour distribution transfer*" [[pdf]](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.458.7694&rep=rep1&type=pdf).

### Look-Up Table (LUT) based Methods

Look-Up Table (LUT) is commonly used in image processing. We collect 100 LUTs from public websites and release the script of applying LUT to foreground in this repository. 


### Color Checker based Methods

For the images with illumination information recorded by color checker, we can first convert its foreground to the standard illumination condition, and then convert it to another illumination condition, arriving at a synthetic composite image. The related codes can be found [here](https://github.com/bcmi/Image-Harmonization-Dataset-ccHarmony).

### Learnable Color Transfer Methods

Based on input real image and foreground mask, we can train a model to predict plausible color transfer for the foreground region to produce synthetic composite images.  The related codes can be found [here](https://github.com/bcmi/SycoNet-Adaptive-Image-Harmonization). 
