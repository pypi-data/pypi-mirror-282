from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))



VERSION = '0.0.1'
DESCRIPTION = 'My all tool'
LONG_DESCRIPTION = 'This is just my personal toool'

# Setting up
setup(
    name="jiku",
    version=VERSION,
    author="NeuralNine (Florian Dedov)",
    author_email="<phinerx749@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",

    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)