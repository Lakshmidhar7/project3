import os
from distutils import sysconfig

directory = os.getcwd()
site_packages_path = sysconfig.get_python_lib()
file_path = os.path.join(site_packages_path, "MyseleniumPath.pth")

if os.path.isfile(file_path):
    os.remove(file_path)
with open(file_path, 'w+')as as_path:
    as_path.write(directory+'\n')
    as_path.write(directory+os.sep+"Pageactions"+os.sep+"\n")
    as_path.write(directory+os.sep+"Pageobjects"+os.sep+'\n')
    as_path.write(directory+os.sep+"Keywords"+os.sep+"\n")

print("\tIntalling Requirement for selenium project\n")
