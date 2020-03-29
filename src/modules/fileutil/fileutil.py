from pathlib import Path

def recursive_search(directory, wildcard="*"):
    """Recursively search a directory for files matching the given wildcard."""
    results  = []
    for path in Path(directory).rglob(wildcard):
        results.append(path) 
    return results
