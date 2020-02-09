# NumPy入门

- 一个强大的N维数据对象Array
- 比较成熟的函数库
- 用于整个C/C++和Fortra代码的工具包
- 实用的线性代数、傅里叶变换和随机数生成函数

1. 安装方法

   ```
   pip install --user numpy
   ```

2. 常用函数

   ```python
   In [1]: import numpy as np
   
   In [2]: a = np.array([1, 2, 3, 4])
   
   In [3]: b = np.arry([4, 5, 6, 7])
   ---------------------------------------------------------------------------
   AttributeError                            Traceback (most recent call last)
   <ipython-input-3-ce0131fb7ffb> in <module>()
   ----> 1 b = np.arry([4, 5, 6, 7])
   
   AttributeError: module 'numpy' has no attribute 'arry'
   
   In [4]: b = np.array([4, 5, 6, 7])
   
   In [5]: c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
   
   In [6]: b
   Out[6]: array([4, 5, 6, 7])
   
   In [7]: c
   Out[7]: 
   array([[ 1,  2,  3,  4],
          [ 4,  5,  6,  7],
          [ 7,  8,  9, 10]])
   
   In [8]: a.shape
   Out[8]: (4,)
   
   In [9]: c.shape
   Out[9]: (3, 4)
   
   In [10]: a = np.arange(10)
   
   In [11]: a
   Out[11]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
   
   In [12]: a[3:5]
   Out[12]: array([3, 4])
   
   In [13]: b = a[3:7]
   # 通过下标获取的新数组是原始数据的一个视图 和原始
   In [14]: b
   Out[14]: array([3, 4, 5, 6])
   
   In [15]: b[2] = -10
   
   In [16]: b
   Out[16]: array([  3,   4, -10,   6])
   
   In [17]: a
   Out[17]: array([  0,   1,   2,   3,   4, -10,   6,   7,   8,   9])
   
   In [18]: a = np.matrix([[1, 2, 3],[5, 5, 6],[7, 9, 9]])
   
   In [19]: a*a**-1
   Out[19]: 
   matrix([[ 1.0000000e+00,  0.0000000e+00,  0.0000000e+00],
           [ 4.4408921e-16,  1.0000000e+00,  4.4408921e-16],
           [ 0.0000000e+00, -4.4408921e-16,  1.0000000e+00]])
   In [20]: a = ([1, 2, 3])
   
   In [21]: a = np.array([1, 2, 3])
   # 一位数组转换为二维数组
   In [22]: a.reshape((-1,1))
   Out[22]: 
   array([[1],
          [2],
          [3]])
   
   In [23]: a.reshape((1,-1))
   Out[23]: array([[1, 2, 3]])
   
   In [23]: a.reshape((1,-1))
   Out[23]: array([[1, 2, 3]])
   
   In [24]: help(np.dot)
   
   
   ```

   

