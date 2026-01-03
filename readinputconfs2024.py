from bs4 import BeautifulSoup
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
                    """
                    if not f.name[:4]=='cont':
                        with open(f.path, 'r', errors = 'ignore') as fh:
                            data = fh.read()
                            #print(data)
                        try:
                            Bs_data = BeautifulSoup(data, 'xml')
                            b_unique = Bs_data.find_all('FriendlyName')
                            print(b_unique)
                        except:
                            print('Skit')
                    """
                    import xml.etree.ElementTree as ET
                    tree = ET.parse(f.path)

























                        





#tree = ET.parse('books.xml')