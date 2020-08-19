# @Author: Christoph Giese @cgi1
# One liner to get another file from an imported module folder

import mads_utils.globals as g
init_notebook_path = os.path.join('/'.join(os.path.abspath(g.__file__).split('/')[0:-1]), 'init_notebook.py')
