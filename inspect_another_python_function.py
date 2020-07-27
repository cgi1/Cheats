"""
@author: Christoph Giese @cgi1
"""

def get_filter():
    # Example function
    if filter_name == 'A':
        return True
    elif filter_name == 'B':
        return False

def get_filter_list(v=False):
    import inspect
    source_get_filter = inspect.getsource(get_filter)
    search_str = "filter_name == "
    extracted_filter_list = []
    for row in source_get_filter.split('\n'):
        splt = row.split("filter_name == \'")
        if len(splt) > 1:
            cleaned = splt[1].split('\'')[0]
            # print(cleaned)
            extracted_filter_list.append(cleaned)

    if v: print("Extracted %s filters from get_filter(filter_name) function." % (len(extracted_filter_list)))
    return extracted_filter_list
    
extracted_filters = get_filter_list(v=True)
