Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Sahil Halarnkar\AppData\Local\Programs\Python\Python39\nptel.py
            dateCrawled  ...          lastSeen
0      30/03/2016 13:51  ...     7/4/2016 4:44
1         7/3/2016 9:54  ...  26/03/2016 13:17
2         1/4/2016 0:57  ...     1/4/2016 8:40
3      19/03/2016 17:50  ...     7/4/2016 4:44
4      16/03/2016 14:51  ...    1/4/2016 23:18
...                 ...  ...               ...
49996    3/4/2016 15:48  ...    5/4/2016 15:16
49997  27/03/2016 14:55  ...    7/4/2016 11:45
49998  14/03/2016 18:51  ...   25/03/2016 6:17
49999  15/03/2016 18:06  ...    6/4/2016 17:15
50000   22/03/2016 9:54  ...    5/4/2016 21:15

[50001 rows x 19 columns]
>>> pd.set_option('display.float_format',lambda x: '%.3f' % x)
>>> pd.set_option('display.max_columns',500)
>>> A.describe()
             price  yearOfRegistration   powerPS  kilometer  \
count    50001.000           50001.000 50001.000  50001.000   
mean      6559.865            2005.544   116.496 125613.688   
std      85818.470             122.992   230.568  40205.234   
min          0.000            1000.000     0.000   5000.000   
25%       1150.000            1999.000    69.000 125000.000   
50%       2950.000            2003.000   105.000 150000.000   
75%       7190.000            2008.000   150.000 150000.000   
max   12345678.000            9999.000 19312.000 150000.000   

       monthOfRegistration  postalCode  
count            50001.000   50001.000  
mean                 5.744   50775.217  
std                  3.711   25743.702  
min                  0.000    1067.000  
25%                  3.000   30559.000  
50%                  6.000   49504.000  
75%                  9.000   71404.000  
max                 12.000   99998.000  
>>> A.columns
Index(['dateCrawled', 'name', 'seller', 'offerType', 'price', 'abtest',
       'vehicleType', 'yearOfRegistration', 'gearbox', 'powerPS', 'model',
       'kilometer', 'monthOfRegistration', 'fuelType', 'brand',
       'notRepairedDamage', 'dateCreated', 'postalCode', 'lastSeen'],
      dtype='object')
>>> A=A.drop(columns=['dateCrawled','name','abtest','dateCreated','lastSeen','postalCode'],axis=1)
>>> A.columns
Index(['seller', 'offerType', 'price', 'vehicleType', 'yearOfRegistration',
       'gearbox', 'powerPS', 'model', 'kilometer', 'monthOfRegistration',
       'fuelType', 'brand', 'notRepairedDamage'],
      dtype='object')
>>> A['monthOfRegistration']/=12
>>> A
           seller offerType  price    vehicleType  yearOfRegistration  \
0         private     offer   4450      limousine                2003   
1         private     offer  13299            suv                2005   
2         private     offer   3200            bus                2003   
3         private     offer   4500      small car                2006   
4         private     offer  18750            suv                2008   
...           ...       ...    ...            ...                 ...   
49996     private   request      0            bus                2005   
49997     private   request  19999            NaN                1990   
49998     private   request      0          coupe                2004   
49999  commercial     offer    100  station wagon                2000   
50000  commercial     offer   1100      small car                2006   

         gearbox  powerPS        model  kilometer  monthOfRegistration  \
0         manual      150          3er     150000                0.250   
1         manual      163     xc_reihe     150000                0.500   
2         manual      101       touran     150000                0.917   
3         manual       86        ibiza      60000                1.000   
4      automatic      185     xc_reihe     150000                0.917   
...          ...      ...          ...        ...                  ...   
49996        NaN        0  transporter     150000                0.000   
49997        NaN        0         golf       5000                0.000   
49998     manual        0          3er     150000                0.083   
49999     manual        0       megane     150000                0.667   
50000     manual       38        matiz     150000                0.833   

      fuelType       brand notRepairedDamage  
0       diesel         bmw               NaN  
1       diesel       volvo                no  
2       diesel  volkswagen               NaN  
3       petrol        seat                no  
4       diesel       volvo                no  
...        ...         ...               ...  
49996      NaN  volkswagen               NaN  
49997      NaN  volkswagen               NaN  
49998   petrol         bmw                no  
49999   petrol     renault               NaN  
50000   petrol   chevrolet                no  

[50001 rows x 13 columns]
>>> A=A.apply(lambda x:x.fillna(x.mean()) if x.dtype=='float' else x.fillna(x.value_counts().index[0]))
>>> A.isnull().sum()
seller                 0
offerType              0
price                  0
vehicleType            0
yearOfRegistration     0
gearbox                0
powerPS                0
model                  0
kilometer              0
monthOfRegistration    0
fuelType               0
brand                  0
notRepairedDamage      0
dtype: int64
>>> B=A['price'].value
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    B=A['price'].value
  File "C:\Users\Sahil Halarnkar\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\generic.py", line 5141, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'value'
>>> B=A['price'].values
>>> B
array([ 4450, 13299,  3200, ...,     0,   100,  1100], dtype=int64)
>>> A=A[(A.yearOfRegistration<=2021) & (A.yearOfRegistration>=1950) & (A.price>=100) & (A.price<=150000) & (A.powerPS>=10) & (A.powerPS<=500)]
>>> A['monthOfRegistration']
0       0.250
1       0.500
2       0.917
3       1.000
4       0.917
         ... 
49991   0.667
49992   0.750
49993   0.667
49995   0.250
50000   0.833
Name: monthOfRegistration, Length: 43155, dtype: float64
>>> A['age']=(2021-A['yearOfRegistration'])+A['monthOfRegistration']
>>> A
           seller offerType  price    vehicleType  yearOfRegistration  \
0         private     offer   4450      limousine                2003   
1         private     offer  13299            suv                2005   
2         private     offer   3200            bus                2003   
3         private     offer   4500      small car                2006   
4         private     offer  18750            suv                2008   
...           ...       ...    ...            ...                 ...   
49991     private     offer  10900      limousine                2004   
49992     private     offer    790      limousine                1998   
49993     private     offer    830      small car                1999   
49995     private     offer   2290  station wagon                2001   
50000  commercial     offer   1100      small car                2006   

         gearbox  powerPS     model  kilometer  monthOfRegistration fuelType  \
0         manual      150       3er     150000                0.250   diesel   
1         manual      163  xc_reihe     150000                0.500   diesel   
2         manual      101    touran     150000                0.917   diesel   
3         manual       86     ibiza      60000                1.000   petrol   
4      automatic      185  xc_reihe     150000                0.917   diesel   
...          ...      ...       ...        ...                  ...      ...   
49991     manual      231   x_reihe     150000                0.667   petrol   
49992     manual       82     astra     150000                0.750   diesel   
49993     manual       60      clio     125000                0.667   petrol   
49995     manual      101     astra     150000                0.250   petrol   
50000     manual       38     matiz     150000                0.833   petrol   

            brand notRepairedDamage    age  
0             bmw                no 18.250  
1           volvo                no 16.500  
2      volkswagen                no 18.917  
3            seat                no 16.000  
4           volvo                no 13.917  
...           ...               ...    ...  
49991         bmw                no 17.667  
49992        opel                no 23.750  
49993     renault                no 22.667  
49995        opel                no 20.250  
50000   chevrolet                no 15.833  

[43155 rows x 14 columns]
>>> A=A.drop(columns=['yearOfRegistration','monthOfRegistration'],axis=1)
>>> B=A['price'].values
>>> A=A.drop(columns=['price'],axis=1)
>>> C=A.values
>>> C
array([['private', 'offer', 'limousine', ..., 'bmw', 'no', 18.25],
       ['private', 'offer', 'suv', ..., 'volvo', 'no', 16.5],
       ['private', 'offer', 'bus', ..., 'volkswagen', 'no',
        18.916666666666668],
       ...,
       ['private', 'offer', 'small car', ..., 'renault', 'no',
        22.666666666666668],
       ['private', 'offer', 'station wagon', ..., 'opel', 'no', 20.25],
       ['commercial', 'offer', 'small car', ..., 'chevrolet', 'no',
        15.833333333333334]], dtype=object)
>>> C=pd.get_dummies(A)
>>> C

>>> C=A.values
>>> C=pd.get_dummies(A)
>>> C=C.values
>>> C
array([[1.50000000e+02, 1.50000000e+05, 1.82500000e+01, ...,
        0.00000000e+00, 1.00000000e+00, 0.00000000e+00],
       [1.63000000e+02, 1.50000000e+05, 1.65000000e+01, ...,
        1.00000000e+00, 1.00000000e+00, 0.00000000e+00],
       [1.01000000e+02, 1.50000000e+05, 1.89166667e+01, ...,
        0.00000000e+00, 1.00000000e+00, 0.00000000e+00],
       ...,
       [6.00000000e+01, 1.25000000e+05, 2.26666667e+01, ...,
        0.00000000e+00, 1.00000000e+00, 0.00000000e+00],
       [1.01000000e+02, 1.50000000e+05, 2.02500000e+01, ...,
        0.00000000e+00, 1.00000000e+00, 0.00000000e+00],
       [3.80000000e+01, 1.50000000e+05, 1.58333333e+01, ...,
        0.00000000e+00, 1.00000000e+00, 0.00000000e+00]])
>>> b=np.log(B)
>>> b
array([8.40065938, 9.49544412, 8.07090609, ..., 6.7214257 , 7.7363071 ,
       7.00306546])
>>> t1x,t2x,t1y,t2y=train_test_split(C,b)
>>> from sklearn.linear_model import LinearRegression
>>> l=LinearRegression()
>>> m=l.fit(t1x,t1y)
>>> p=m.predict(t2x)
>>> accuracy_score(t2y,p)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    accuracy_score(t2y,p)
  File "C:\Users\Sahil Halarnkar\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\utils\validation.py", line 63, in inner_f
    return f(*args, **kwargs)
  File "C:\Users\Sahil Halarnkar\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\metrics\_classification.py", line 202, in accuracy_score
    y_type, y_true, y_pred = _check_targets(y_true, y_pred)
  File "C:\Users\Sahil Halarnkar\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\metrics\_classification.py", line 100, in _check_targets
    raise ValueError("{0} is not supported".format(y_type))
ValueError: continuous is not supported
>>> 