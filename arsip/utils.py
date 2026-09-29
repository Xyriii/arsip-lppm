from .models import Folder


def build_breadcrumb(folder):
    """Bikin list breadcrumb dari root sampai folder ini"""
    if not folder:
        return []

    breadcrumb = []
    current = folder
    while current:
        breadcrumb.insert(0, current)
        current = current.parent
    return breadcrumb


def build_tree(folders, parent=None):
    """Bikin struktur pohon dari list folder"""
    tree = []
    for folder in folders:
        if folder.parent_id == (parent.id if parent else None):
            children = build_tree(folders, folder)
            tree.append({
                'folder': folder,
                'children': children,
            })
    return tree