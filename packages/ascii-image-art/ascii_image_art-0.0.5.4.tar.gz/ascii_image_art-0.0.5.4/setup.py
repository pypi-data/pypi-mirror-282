from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='ascii_image_art',
    version='0.0.5.4',
    description='A simple to use Python library to convert images into ASCII characters text file and ASCII characters colored images. Option to use new AI module.',
    author='Mohammad Asad',
    url='https://github.com/txtasad/Ascii-Image-Art',
    readme ='README.md',
    classifiers = [
    'Operating System :: OS Independent',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3.0',
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Financial and Insurance Industry',
    'Intended Audience :: Science/Research',
    'Natural Language :: English'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown', 
    license='MIT',
    packages=find_packages(),
    keywords=['python','ascii','image to text','image to ascii', 'color ascii image','text image','ASAD','MOHAMMAD ASAD','ascii_art','ascii-image']
)