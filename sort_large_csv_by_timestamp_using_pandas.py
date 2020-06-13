"""
A script to do a validation check on the timestamp 
to only set_index/sort_index/save_to_csv if a valid timestamp is in the row.

@author: Christoph Giese cgi1; https://github.com/cgi1/
"""
import pandas as pd
import os, datetime, traceback

L1_DIR = '/mnt/ssd/ASCII/'
suffix = '.l1'
for fname in sorted(os.listdir(L1_DIR)):
    if not fname.endswith(suffix):
        continue
    print("Start processing %s" % fname)
    s = datetime.datetime.now()
    fin_path = os.path.join(L1_DIR, fname)
    fname_out = fname.split('.')[0] + '.l1sorted'
    fpath_out = os.path.join(L1_DIR, fname_out)

    df = pd.read_csv(fin_path)
    e = datetime.datetime.now()
    print("Read %s rows from %s. Took (%s)" % (len(df.index), fname, (e-s)))
    df['ts_parsed'] = pd.to_datetime(df['ts'], format='%Y-%m-%d %H:%M:%S.%f', errors='coerce')

    is_na_row = df.index.isin(df['ts_parsed'].isna())
    df_dt_not_parsable = df.loc[df.index.isin(is_na_row)]
    print("%.2f %% (abs: %s) are not parsable datetimes. Removed it."
          % ((100 / len(df.index) * len(df_dt_not_parsable.index)), len(df_dt_not_parsable.index)))
    df = df.loc[~df.index.isin(is_na_row)]
    print("Now having %s rows to set_index." % len(df.index))
    s = datetime.datetime.now()
    df.set_index('ts', inplace=True)
    e = datetime.datetime.now()
    print("set_index %s rows from %s. Took (%s)" % (len(df.index), fname, (e-s)))

    s = datetime.datetime.now()
    df.sort_index(inplace=True)
    e = datetime.datetime.now()
    print("sort_index %s rows from [%s] to [%s]. Took (%s)" % (len(df.index), fname, fname_out, (e-s)))

    s = datetime.datetime.now()
    df.reset_index(inplace=True)
    # This one saves at ~10MB per second to disk.. One day is 7.5GB --> 750 seconds or 12.5 minutes
    df.to_csv(fpath_out, index=False)
    e = datetime.datetime.now()
    print("to_csv %s rows from [%s] to [%s]. Took (%s)" % (len(df.index), fname, fname_out, (e - s)))


