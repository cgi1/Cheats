import datetime, traceback, os, sys
from traceback import format_exc as fe

"""
@author: Christoph Giese @cgi1
"""

def get_time_selector(ddf_c, start_time=None, end_time=None, v=True):
    """
    A simple converter to define a dask selector based on datetime.time inputs.
        Usage:
        selector_ddf_c_pre = get_time_selector(ddf_c=ddf_c, 
                                       start_time=datetime.time(hour=8, minute=0, second=0), 
                                       end_time=datetime.time(hour=9, minute=30, second=0))
        ddf_c.loc[selector_ddf_c_pre] # Locates based on time_selector
    """
    selector = None
    if ddf_c is None:
        print("Error>No ddf_c to get_time_selector!")
        return selector

    if start_time is not None and not isinstance(start_time, datetime.time):
        print("ERROR>start_time must be datetime.time or None!")
    if end_time is not None and not isinstance(end_time, datetime.time):
        print("ERROR>end_time must be datetime.time or None!")

    start_selector, end_selector = None, None
    if start_time is not None:
        start_selector = (ddf_c.index.dt.hour > start_time.hour) | (
                    (ddf_c.index.dt.hour == start_time.hour) & (ddf_c.index.dt.minute >= start_time.minute))

    if end_time is not None:
        end_selector = (ddf_c.index.dt.hour < end_time.hour) | (
                    (ddf_c.index.dt.hour == end_time.hour) & (ddf_c.index.dt.minute <= end_time.minute))
    if start_selector is None:
        if end_selector is None:
            pass
        else:
            selector = end_selector
    else:
        if end_selector is None:
            selector = start_selector
        else:
            selector = start_selector & end_selector

    try:
        if v:
            print("start_time=%s end_time=%s" % (start_time, end_time))
    except:
        print("Error> Failed to exec get_time_selector(%s,%s) (%s)" % (start_time, end_time, fe()))
    finally:
        return selector
