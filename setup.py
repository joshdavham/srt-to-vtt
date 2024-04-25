from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='srt-to-vtt',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    author='Joshua Hamilton',
    author_email='hamiltonjoshuadavid@gmail.com',
    description='Python package to enable easy conversion of .srt files to .vtt files.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords=['subtitle', 'subtitles', 'convert', 'srt', 'vtt', 'webvtt'],
    url='https://github.com/joshdavham/srt-to-vtt',
)
