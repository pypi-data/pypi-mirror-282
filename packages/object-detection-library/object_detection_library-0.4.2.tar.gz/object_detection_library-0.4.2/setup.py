from setuptools import setup, find_packages

setup(
    name='object_detection_library',
    version='0.4.2',
    description='A library for YOLOv8 object detection and other utilities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Karthik180304/object-detection',
    author='Karthik',
    author_email='karthik.shivakkumar@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'torch',
        'ultralytics',
        'opencv-python',
        'paho-mqtt',
        'numpy',
        'expecttest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'object_detection=object_detection_library.main:main',  # This line allows the main function to be callable from the command line
        ],
    },
)
