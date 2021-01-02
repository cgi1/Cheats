#Orig from https://stackoverflow.com/a/25574638/940592

def du(path):
    try:
        """disk usage in human readable format (e.g. '2,1GB')"""
        ret_val = subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')
        return int(ret_val)
    except:
        print(f"Error> Could du folder ({path}) {fe()}")
