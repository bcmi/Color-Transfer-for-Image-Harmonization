# Color-Transfer-for-Image-Harmonization
Summarize different color transfer strategies which could be used for image harmonization task.



### Traditional Color Transfer Methods

To generate synthesized composite images, traditional color transfer methods can be adopted to transfer color information from reference images to real images. We categorize previous color transfer methods into four groups based on parametric/non-parametric and correlated/decorrelated color space, and select one representative method from each group. We provide the  implementation of the following four representative methods specialized for foreground color transfer. 

- global color transfer: Parametric method in decorrelated color space. Implementation of paper "*Color transfer between images*" [[pdf]](https://www.cs.tau.ac.il/~turkel/imagepapers/ColorTransfer.pdf).

- global color transfer in RGB color space: Parametric method in correlated color space. Implementation of paper "*Color transfer in correlated color space*" [[pdf]](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.530.2757&rep=rep1&type=pdf).

- cumulative histogram mapping: Non-parametric method in decorrelated color space. Implementation of paper  ""*Histogram-based prefiltering for luminance and chrominance compensation of multiview video*" [[pdf]](https://ieeexplore.ieee.org/document/4539698).

- IDT regrain color transfer: Non-parametric method in correlated color space. Implementation of paper  "*Automated colour grading using colour distribution transfer*" [[pdf]](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.458.7694&rep=rep1&type=pdf).

### Look-up Table (LUT)

Look-up Table (LUT) is commonly used in image processing. We collect 100 LUTs from public websites and release the script to apply LUT to foreground. 
