Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Sahil Halarnkar/AppData/Local/Programs/Python/Python39/nptel.py
       age       JobType  ...   nativecountry                        SalStat
0       45       Private  ...   United-States   less than or equal to 50,000
1       24   Federal-gov  ...   United-States   less than or equal to 50,000
2       44       Private  ...   United-States            greater than 50,000
3       27       Private  ...          Mexico   less than or equal to 50,000
4       20       Private  ...   United-States   less than or equal to 50,000
...    ...           ...  ...             ...                            ...
31973   34     Local-gov  ...   United-States   less than or equal to 50,000
31974   34     Local-gov  ...   United-States   less than or equal to 50,000
31975   23       Private  ...   United-States   less than or equal to 50,000
31976   42     Local-gov  ...   United-States   less than or equal to 50,000
31977   29       Private  ...   United-States   less than or equal to 50,000

[31978 rows x 13 columns]
>>> A.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 31978 entries, 0 to 31977
Data columns (total 13 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   age            31978 non-null  int64 
 1   JobType        30169 non-null  object
 2   EdType         31978 non-null  object
 3   maritalstatus  31978 non-null  object
 4   occupation     30162 non-null  object
 5   relationship   31978 non-null  object
 6   race           31978 non-null  object
 7   gender         31978 non-null  object
 8   capitalgain    31978 non-null  int64 
 9   capitalloss    31978 non-null  int64 
 10  hoursperweek   31978 non-null  int64 
 11  nativecountry  31978 non-null  object
 12  SalStat        31978 non-null  object
dtypes: int64(4), object(9)
memory usage: 3.2+ MB
>>> A.describe()
                age   capitalgain   capitalloss  hoursperweek
count  31978.000000  31978.000000  31978.000000  31978.000000
mean      38.579023   1064.360623     86.739352     40.417850
std       13.662085   7298.596271    401.594301     12.345285
min       17.000000      0.000000      0.000000      1.000000
25%       28.000000      0.000000      0.000000     40.000000
50%       37.000000      0.000000      0.000000     40.000000
75%       48.000000      0.000000      0.000000     45.000000
max       90.000000  99999.000000   4356.000000     99.000000
>>> A.isnull().sum()
age                 0
JobType          1809
EdType              0
maritalstatus       0
occupation       1816
relationship        0
race                0
gender              0
capitalgain         0
capitalloss         0
hoursperweek        0
nativecountry       0
SalStat             0
dtype: int64
>>> A['occupation'].value_counts()
 Prof-specialty       4038
 Craft-repair         4030
 Exec-managerial      3992
 Adm-clerical         3721
 Sales                3584
 Other-service        3212
 Machine-op-inspct    1966
 Transport-moving     1572
 Handlers-cleaners    1350
 Farming-fishing       989
 Tech-support          912
 Protective-serv       644
 Priv-house-serv       143
 Armed-Forces            9
Name: occupation, dtype: int64
>>> B=A.dropna(axis=0)
>>> B.isnull().sum()
age              0
JobType          0
EdType           0
maritalstatus    0
occupation       0
relationship     0
race             0
gender           0
capitalgain      0
capitalloss      0
hoursperweek     0
nativecountry    0
SalStat          0
dtype: int64
>>> pd.crosstab(index=B['gender'],column=B['SalStat'],margins=True,normalize=index)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    pd.crosstab(index=B['gender'],column=B['SalStat'],margins=True,normalize=index)
NameError: name 'index' is not defined
>>> pd.crosstab(index=B['gender'],columns=B['SalStat'],margins=True,normalize='index')
SalStat   greater than 50,000   less than or equal to 50,000
gender                                                      
 Female              0.113678                       0.886322
 Male                0.313837                       0.686163
All                  0.248922                       0.751078
>>> B['SalStat']=B['SalStat'].map({' less than or equal to 50,000':0,'greater than 50,000':1})

Warning (from warnings module):
  File "<pyshell#8>", line 1
SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
>>> B['SalStat']
0        0.0
1        0.0
2        NaN
3        0.0
4        0.0
        ... 
31973    0.0
31974    0.0
31975    0.0
31976    0.0
31977    0.0
Name: SalStat, Length: 30162, dtype: float64
>>> B['SalStat']=B['SalStat'].map({0.0:0,None:1})
>>> B['SalStat']
0        0.0
1        0.0
2        NaN
3        0.0
4        0.0
        ... 
31973    0.0
31974    0.0
31975    0.0
31976    0.0
31977    0.0
Name: SalStat, Length: 30162, dtype: float64
>>> B=A.dropna(axis=0)
>>> B['SalStat']=B['SalStat'].map({' less than or equal to 50,000':0, ' greater than 50,000':1})

Warning (from warnings module):
  File "<pyshell#13>", line 1
SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
>>> B['SalStat']
0        0
1        0
2        1
3        0
4        0
        ..
31973    0
31974    0
31975    0
31976    0
31977    0
Name: SalStat, Length: 30162, dtype: int64
>>> B1=B['SalStat'].values()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    B1=B['SalStat'].values()
TypeError: 'numpy.ndarray' object is not callable
>>> B1=B['SalStat'].values
>>> B1
array([0, 0, 1, ..., 0, 0, 0], dtype=int64)
>>> B.drop(columns=['SalStat'],axis=1)
       age       JobType  ... hoursperweek   nativecountry
0       45       Private  ...           28   United-States
1       24   Federal-gov  ...           40   United-States
2       44       Private  ...           40   United-States
3       27       Private  ...           40          Mexico
4       20       Private  ...           35   United-States
...    ...           ...  ...          ...             ...
31973   34     Local-gov  ...           60   United-States
31974   34     Local-gov  ...           40   United-States
31975   23       Private  ...           40   United-States
31976   42     Local-gov  ...           40   United-States
31977   29       Private  ...           40   United-States

[30162 rows x 12 columns]
>>> B.columsn
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    B.columsn
  File "C:\Users\Sahil Halarnkar\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\generic.py", line 5141, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'columsn'
>>> B.columns
Index(['age', 'JobType', 'EdType', 'maritalstatus', 'occupation',
       'relationship', 'race', 'gender', 'capitalgain', 'capitalloss',
       'hoursperweek', 'nativecountry', 'SalStat'],
      dtype='object')
>>> B=B.drop(columns=['SalStat'],axis=1)
>>> B.columns
Index(['age', 'JobType', 'EdType', 'maritalstatus', 'occupation',
       'relationship', 'race', 'gender', 'capitalgain', 'capitalloss',
       'hoursperweek', 'nativecountry'],
      dtype='object')
>>> C=pd.get_dummies(B,drop_first=True)
>>> C
       age  capitalgain  ...  nativecountry_ Vietnam  nativecountry_ Yugoslavia
0       45            0  ...                       0                          0
1       24            0  ...                       0                          0
2       44            0  ...                       0                          0
3       27            0  ...                       0                          0
4       20            0  ...                       0                          0
...    ...          ...  ...                     ...                        ...
31973   34          594  ...                       0                          0
31974   34            0  ...                       0                          0
31975   23            0  ...                       0                          0
31976   42            0  ...                       0                          0
31977   29            0  ...                       0                          0

[30162 rows x 94 columns]
>>> C=C.values
>>> C
array([[45,  0,  0, ...,  1,  0,  0],
       [24,  0,  0, ...,  1,  0,  0],
       [44,  0,  0, ...,  1,  0,  0],
       ...,
       [23,  0,  0, ...,  1,  0,  0],
       [42,  0,  0, ...,  1,  0,  0],
       [29,  0,  0, ...,  1,  0,  0]], dtype=int64)
>>> t1x,t2x,t1y,t2y=train_test_split(C,B1)
>>> t1x
array([[25,  0,  0, ...,  1,  0,  0],
       [64,  0,  0, ...,  1,  0,  0],
       [41,  0,  0, ...,  0,  0,  0],
       ...,
       [47,  0,  0, ...,  1,  0,  0],
       [22,  0,  0, ...,  1,  0,  0],
       [63,  0,  0, ...,  1,  0,  0]], dtype=int64)
>>> t1x.shape
(22621, 94)
>>> t2x.shape
(7541, 94)
>>> l=LogisticRegression)(
	
SyntaxError: unmatched ')'
>>> l=LogisticRegression()
>>> k=l.fit(t1x,t1y)

Warning (from warnings module):
  File "C:\Users\Sahil Halarnkar\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\linear_model\_logistic.py", line 763
    n_iter_i = _check_optimize_result(
ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Increase the number of iterations (max_iter) or scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
>>> #dont use logistic regression try using knn
>>> from sklearn.neigbors import KNeighborClassifier
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    from sklearn.neigbors import KNeighborClassifier
ModuleNotFoundError: No module named 'sklearn.neigbors'
>>> from sklearn.neighbors import KNeighborClassifier
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    from sklearn.neighbors import KNeighborClassifier
ImportError: cannot import name 'KNeighborClassifier' from 'sklearn.neighbors' (C:\Users\Sahil Halarnkar\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\neighbors\__init__.py)
>>> from sklearn.neighbors import KNeighborsClassifier
>>> K=KNeighborsClassifier(n_neighbors=18)
>>> K.fit(t1x,t1y)
KNeighborsClassifier(n_neighbors=18)
>>> p=K.predict(t2x)
>>> a=accuracy_score(t2y,p)
>>> a
0.8449807717809309
>>> B
       age       JobType  ... hoursperweek   nativecountry
0       45       Private  ...           28   United-States
1       24   Federal-gov  ...           40   United-States
2       44       Private  ...           40   United-States
3       27       Private  ...           40          Mexico
4       20       Private  ...           35   United-States
...    ...           ...  ...          ...             ...
31973   34     Local-gov  ...           60   United-States
31974   34     Local-gov  ...           40   United-States
31975   23       Private  ...           40   United-States
31976   42     Local-gov  ...           40   United-States
31977   29       Private  ...           40   United-States

[30162 rows x 12 columns]
>>> C
array([[45,  0,  0, ...,  1,  0,  0],
       [24,  0,  0, ...,  1,  0,  0],
       [44,  0,  0, ...,  1,  0,  0],
       ...,
       [23,  0,  0, ...,  1,  0,  0],
       [42,  0,  0, ...,  1,  0,  0],
       [29,  0,  0, ...,  1,  0,  0]], dtype=int64)
>>> B1
array([0, 0, 1, ..., 0, 0, 0], dtype=int64)
>>> B.columns
Index(['age', 'JobType', 'EdType', 'maritalstatus', 'occupation',
       'relationship', 'race', 'gender', 'capitalgain', 'capitalloss',
       'hoursperweek', 'nativecountry'],
      dtype='object')
>>> 5

