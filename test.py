import pandas as pd
s=pd.Series({'渝中区':36,'江北区':80,'江津区':27,'沙坪坝区':45})
df = pd.DataFrame({'a': list("opq"), 'b': [3, 2, 1]}, index=['e', 'f', 'g'])

print(df[0:1])