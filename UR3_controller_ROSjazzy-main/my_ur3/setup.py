from setuptools import setup
import os
from glob import glob

package_name = 'my_ur3'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), ['resource/' + package_name]),

        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.xml')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
        
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf') + glob('urdf/*.urdf.xacro')),  

        (os.path.join('share', package_name, 'meshes', 'ur3', 'visual'), glob('meshes/ur3/visual/*')),
        (os.path.join('share', package_name, 'meshes', 'ur3', 'collision'), glob('meshes/ur3/collision/*')),

        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sigurd Gresberg',
    maintainer_email='sigurd.gresberg@gmail.com',
    description='UR3 Robot Package',
    license='Apache License 2.0',
)
