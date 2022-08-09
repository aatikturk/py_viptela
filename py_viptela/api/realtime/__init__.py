import os
from py_viptela.api.realtime import cellular
for module in os.listdir(os.path.dirname(__file__)):
    if module != '__init__.py' and module[-3:] == '.py':
        __import__(module[:-3], locals(), globals())
del module