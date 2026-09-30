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

def build_full_tree():
    """Build full tree of ALL active folders (nested)"""
    all_folders = list(Folder.objects.filter(is_active=True).order_by('order', 'name'))
    
    def _build(parent_id):
        nodes = []
        for f in all_folders:
            if f.parent_id == parent_id:
                nodes.append({
                    'folder': f,
                    'children': _build(f.id),
                })
        return nodes
    
    return _build(None)


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