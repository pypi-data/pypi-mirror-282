from setuptools import setup, find_packages

setup(
    name='mykmeansproject',
    version='0.2',  # Versiyon numarasını güncelledik
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Gereken diğer paketler
    ],
    package_data={
        'mykmeansproject': ['yeni44-mac.out', 'yeni44-linux.out'],
    },
    entry_points={
        'console_scripts': [
            # Komut satırı araçları eklemek isterseniz buraya ekleyebilirsiniz
        ],
    },
    author="Vasfi Tataroglu",
    author_email="your-email@example.com",
    description="A package for running KMeans and GeoKMeans algorithms.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/mykmeansproject",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
