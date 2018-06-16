# Dimensionality reduction and classification on Hyperspectral Images Using Python

### Prerequisites

The things that you must have a decent knowledge on: 
```
    * Python
    * MatLab
```

### Installing

* This project is fully based on python. So, the necessary modules needed for computaion are:
```
    * Numpy
    * Sklearm
    * Matplotlib
    * Pandas
```
* The commands needed for installing the above modules on windows platfom are:
```python

    pip install numpy
    pip install sklearn
    pip install matplotlib
    pip install pandas
```
* we can verify the installation of modules by  importing the modules. For example:
```python

    import numpy
    from sklearn.decomposition import PCA 
    import matplotlib.pyplot as plt
    import pandas as pd
```
### Results :

   * Here we are performing the the **dimensionality reduction**  on the **hyperspectral image** called [Indian Pines](http://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes).


1. The resultof the [indian_pines_pca.py](https://github.com/syamkakarla98/Dimensionality-reduction-and-classification-on-Hyperspectral-Images-Using-Python/blob/master/indian_pines_pca.py) is shown below:

     * It initial result is a bargraph for the first **10 Pricipal Components according** to their _variance ratio's_ :

      ![indian_pines_varianve_ratio](https://user-images.githubusercontent.com/36328597/41495831-56fff622-714e-11e8-87ab-731c11d14bab.JPG)
      
   Since, the initial two principal COmponents have high variance. so, we will select the initial two PC'S.
      
      * It second result is a scatter plot for the first **10 Pricipal Components according** :

      ![indian_pines_after_pca_with_2pc](https://user-images.githubusercontent.com/36328597/41495958-603d0baa-7151-11e8-9c7c-c7452b2fb6a8.JPG)


      * The above program resullts a dimensionally reduced [csvfile](https://github.com/syamkakarla98/Dimensionality-reduction-and- classification-on-Hyperspectral-Images-Using-Python/blob/master/indian_pines_after_pca.csv).

