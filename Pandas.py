print ("Pandas")

import pandas as pd


pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

pd.DataFrame({'Igen': [20, 30], 'Nem': [131, 121]})



pd.DataFrame({'Jhon': [121,121], 'jedd':[2121,12121]})

pd.DataFrame({'jhon': [121, 1212],
    'jeff': [22, 211]},
    index= ['a', 'b'])

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

pd.Series([1,2,3,4,5])


pd.Series([1,2,3], index=['car1', 'car2', 'car3'], name='cars')


