# Dimensionality reduction and classification on Hyperspectral Images Using Python

## Authors

   * [**DR.T.Hitendra Sarma**](https://scholar.google.co.in/citations?user=8Frh6IQAAAAJ&hl=en)
   * **Syam Kakarla**
   
### Prerequisites

The things that you must have a decent knowledge on: 
```
    * Python
    * MatLab
    * Linear Algebra
```

### Installation

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
### Results 

   * Here we are performing the the **dimensionality reduction**  on the **hyperspectral image** called [Indian Pines](http://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes)     

1. The result of the [indian_pines_pca.py](
https://github.com/syamkakarla98/Dimensionality-reduction-and-classification-on-Hyperspectral-Images-Using-Python/blob/master/indian_pines_after_pca.csv) is shown below:

     * It initial result is a bargraph for the first **10 Pricipal Components according** to their _variance ratio's_ :

      ![indian_pines_varianve_ratio](https://user-images.githubusercontent.com/36328597/41495831-56fff622-714e-11e8-87ab-731c11d14bab.JPG)
      
   Since, the initial two principal COmponents have high variance. so, we will select the initial two PC'S.
      
      * It second result is a scatter plot for the first **10 Pricipal Components** is :

      ![indian_pines_after_pca_with_2pc](https://user-images.githubusercontent.com/36328597/41495958-603d0baa-7151-11e8-9c7c-c7452b2fb6a8.JPG)


   * The above program resullts a dimensionally reduced [csvfile](
https://github.com/syamkakarla98/Dimensionality-reduction-and-classification-on-Hyperspectral-Images-Using-Python/blob/master/indian_pines_after_pca.csv) .
 
2. The result of the [indian_pines_knnc.py](https://github.com/syamkakarla98/Dimensionality-reduction-and-classification-on-Hyperspectral-Images-Using-Python/blob/master/Indian_pines_knnc.py) is given below:

      * The above program will classify the Indian Pines dataset before **Principal Component Analysis(PCA)**. The classifier here used for classification is [K-Nearest Neighbour Classifier (KNNC)](http://scikitlearn.org/stable/auto_examples/neighbors/plot_classification.html)
      * The time taken for classification is:
      
   ![indian_pines_classification_before_pca](https://user-images.githubusercontent.com/36328597/41496231-d2ddac0e-7157-11e8-9c14-29e89685569c.JPG)

      * Then the classification accuracy of indian pines dataset before **PCA** is:
      
   ![indian_pines_accuracy_before_pca](https://user-images.githubusercontent.com/36328597/41495844-97a3e31e-714e-11e8-8d63-4d786317b239.JPG)    
   
3. The result of the [indian_pines_knnc_after_pca.py](
https://github.com/syamkakarla98/Dimensionality-reduction-and-classification-on-Hyperspectral-Images-Using-Python/blob/master/Indian_pines_knnc_after_pca.py)

   * Then the resultant classification accuracy of indian pines dataset after **PCA** is:
      
      ![indian_pines_accuracy_after_pca](https://user-images.githubusercontent.com/36328597/41495843-9753df04-714e-11e8-9540-0968bdb27a7f.JPG)

### Conclusion :

   * By performing **PCA** on the corrected indian pines dataset results **100 Principal Components(PC'S)**.
   * since, the initial two Principal Components(PC'S) has **92.01839071674918** variance ratio. we selected two only.
   * Initially the dataset contains the dimensions **21025 X 200** is drastically reduced to **21025 X 2** dimensions.
   * The time taken for classification before and after Principal Component Analysis(PCA) is:
         
         |   Dataset     |   Accuracy    | Time Taken |
         | ------------- |:-------------:| ----------:|
         |  Before PCA   |   72.748890   |  17.6010   |
         |  After PCA    |   60.098187   | 0.17700982 |
       
   * Hence, the **time** has been reduced with a lot of difference and the **classification accuracy(C.A)** also reduced but the  C.A can increased little bit by varying the 'k' value. 

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/syamkakarla98/Dimensionality-reduction-and-classification-on-Hyperspectral-Images-Using-Python/blob/master/LICENSE.md) file for details
