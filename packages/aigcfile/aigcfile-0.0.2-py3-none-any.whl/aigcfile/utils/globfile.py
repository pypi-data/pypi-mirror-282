
def glob_paths(src_dir, wildcards=["**/*"]):
    """通过通配符, 读取目录下多种后缀名的文件, 比如["**/*.txt", "**/*.jpg"]。
    Args:
        path: path.Path()类型。文件夹路径。
        wildcards: str list类型。通配符列表, 如["**/*.txt", "**/*.jpg"]。
    Returns:
        返回文件路径list列表, 路径数据类型为pathlib.Path。
    """
    paths = []
    for w in wildcards:
        paths.extend(src_dir.glob(w))
    return paths
