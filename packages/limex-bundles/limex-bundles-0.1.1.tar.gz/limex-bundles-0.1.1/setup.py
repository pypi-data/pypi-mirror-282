from setuptools import setup, find_packages

setup(
    name='limex-bundles',
    version='0.1.1',
    description='A library to install Limex bundles for Zipline',
    author='LimexDataHub',
    author_email='datahub@limex.com',
    url='https://github.com/Limex-com/limexhub-python',  # замените на ваш URL
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'shutil', 
        'limexhub', 
        'zipline-reloaded'
    ],
    entry_points={
        'console_scripts': [
            'install_bundle=limex_bundles.installer:install_bundle',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

