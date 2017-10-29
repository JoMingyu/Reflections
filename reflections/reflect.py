import pkgutil

_resources = []


def reflect(package, extractor):
    _resources.clear()
    extractor(package)

    return _resources


def default_extractor(target):
    for loader, name, is_package in pkgutil.iter_modules(target.__path__):
        # Iterate modules
        if is_package:
            # If package, append and search deeper
            _resources.append((loader, name))
            default_extractor(loader.find_module(name).load_module(name))
        else:
            # If module, append
            _resources.append((loader, name))


def module_extractor(target):
    for loader, name, is_package in pkgutil.iter_modules(target.__path__):
        # Iterate modules
        if is_package:
            # If package, search deeper
            module_extractor(loader.find_module(name).load_module(name))
        else:
            # If module, append
            _resources.append((loader, name))


def package_extractor(target):
    for loader, name, is_package in pkgutil.iter_modules(target.__path__):
        # Iterate modules
        if is_package:
            # If package, append and search deeper
            _resources.append((loader, name))
            package_extractor(loader.find_module(name).load_module(name))
