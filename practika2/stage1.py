import argparse
import urllib.request
import json
import xml.etree.ElementTree as ET
import webbrowser
import tempfile
import os
def get_deps(package, source, depth=0, max_depth=2):
    if depth >= max_depth:
        return {}
    try:
        url = f"{source}/{package.lower()}/index.json"
        versions = json.loads(urllib.request.urlopen(url).read())['versions']
        url = f"{source}/{package.lower()}/{versions[-1]}/{package.lower()}.nuspec"
        root = ET.fromstring(urllib.request.urlopen(url).read())
        deps = {}
        for dep in root.findall('.//{*}dependency'):
            dep_id = dep.get('id')
            if dep_id:
                deps[dep_id] = get_deps(dep_id, source, depth+1, max_depth)
        return deps
    except:
        return {}
def to_mermaid(graph, parent=None):
    lines = []
    for pkg, deps in graph.items():
        if parent:
            lines.append(f"    {parent.replace('.', '_')} --> {pkg.replace('.', '_')}")
        lines.extend(to_mermaid(deps, pkg))
    return lines
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--package", required=True)
    parser.add_argument("-d", "--depth", type=int, default=2)
    args = parser.parse_args()
    source = "https://api.nuget.org/v3-flatcontainer"
    graph = {args.package: get_deps(args.package, source, max_depth=args.depth)}
    mermaid_code = "graph TD\n" + "\n".join(to_mermaid(graph))
    print("Mermaid код:")
    print(mermaid_code)
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <style>body {{ margin: 20px; }}</style>
    </head>
    <body>
        <div class="mermaid">
            {mermaid_code}
        </div>
        <script>mermaid.initialize({{startOnLoad:true}});</script>
    </body>
    </html>
    """
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html') as f:
        f.write(html)
        webbrowser.open(f'file://{f.name}')
    print(f"\nГраф открыт в браузере!")
if __name__ == "__main__":
    main()
