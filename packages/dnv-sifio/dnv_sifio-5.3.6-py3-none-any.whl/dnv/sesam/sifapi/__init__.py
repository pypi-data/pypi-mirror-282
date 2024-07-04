import os


def dlls_path() -> str:
    parent_path = __path__[0]
    return os.path.join(parent_path, ".dlls")


def add_reference(assembly_name: str) -> None:
    from clr import AddReference
    assembly_path = os.path.join(dlls_path(), assembly_name)
    AddReference(assembly_path)
