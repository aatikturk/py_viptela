import os
for module in os.listdir(os.path.dirname(__file__)):
    if module != '__init__.py' and module[:-3] == ".py":
        module = module[:-3]
        from py_viptela.api.tshoot import module
    elif module != '__init__.py' and module[:-3] != ".py":
        from py_viptela.api.tshoot import module
del module