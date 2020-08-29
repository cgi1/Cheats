import dask.dataframe as dd
import pandas as pd
from numba import jit, njit
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
ddf = dd.from_pandas(df, npartitions=2)
print (ddf.compute())
