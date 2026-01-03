import xml.etree.ElementTree as ET
import os

path = r'C:\Users\stefa\AppData\Local\Packages\Microsoft.FlightSimulator_8wekyb3d8bbwe\SystemAppData\wgs\000901F27997511D_00000000000000000000000069F80140'
dirs = os.listdir(path)
print(dirs)

with os.scandir(path) as d:
    for e in d:
        if e.is_dir():
            with os.scandir(fr'{path}\{e.name}') as dd:
                for f in dd:
                    print(f.path)
                    if not f.name.endswith('.1'):
                        tree = ET.parse(f.path)
                        root = tree.getroot()
                        print(root.tag)
"""                         for child in root:
                            print(child.tag, child.attrib)  """
                        





#tree = ET.parse('books.xml')