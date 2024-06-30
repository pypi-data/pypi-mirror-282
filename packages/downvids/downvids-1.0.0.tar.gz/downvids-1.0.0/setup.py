from setuptools import setup, find_packages

setup(
    name='downvids',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'downvids=downvids.downvids:main',
        ],
    },
    author='Avinion',
    author_email='shizofrin@gmail.com',
    description='A script to download videos with specified segments using yt-dlp and ffmpeg',
    url='https://x.com/Lanaev0li',
    license='Avinion Group License',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Topic :: Multimedia :: Video',
    ],
    python_requires='>=3.8',
    install_requires=[
        'yt-dlp',
    ],
)
