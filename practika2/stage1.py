import argparse
import urllib.request
import json
import xml.etree.ElementTree as ET
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--package", required=True)
    parser.add_argument("-s", "--source", default="https://api.nuget.org/v3-flatcontainer")
    args = parser.parse_args()
    print(f"Анализ пакета: {args.package}")
    try:
        url = f"{args.source.rstrip('/')}/{args.package.lower()}/index.json"
        with urllib.request.urlopen(url) as response:
            versions = json.loads(response.read().decode())['versions']
        version = versions[-1]
        print(f"Версия: {version}")
        url = f"{args.source.rstrip('/')}/{args.package.lower()}/{version}/{args.package.lower()}.nuspec"
        with urllib.request.urlopen(url) as response:
            root = ET.fromstring(response.read().decode())
        dependencies = []
        for dep in root.findall('.//{*}dependency'):
            dep_id = dep.get('id')
            if dep_id:
                dependencies.append(dep_id)
        print("Прямые зависимости:")
        for dep in dependencies:
            print(f"  - {dep}")  
    except Exception as e:
        print(f"Ошибка: {e}")
if __name__ == "__main__":
    main()
