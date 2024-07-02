# from setuptools import setup, find_packages

# VERSION = '0.0.1'
# DESCRIPTION = 'A basic hello package'

# # Setting up
# setup(
#     name="hello_world_nk",
#     version=VERSION,
#     author="Nandhini",
#     author_email="<nandhini67288@gmail.com>",
#     description=DESCRIPTION,
#     long_description_content_type="text/markdown",
#     packages=find_packages(),
#     install_requires=['opencv-python'],
#     keywords=['python','hello'],
#     classifiers=[
#         "Development Status :: 1 - Planning",
#         "Intended Audience :: Developers",
#         "Programming Language :: Python :: 3",
#         "Operating System :: Unix",
#         "Operating System :: MacOS :: MacOS X",
#         "Operating System :: Microsoft :: Windows",
#     ]
# )


from setuptools import setup, find_packages

setup(
    name="hello_world_nk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    author="Nandhini",
    author_email="nandhini67288@gmail.com",
    description="A short description of your package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/nandhinikesavan20/hello_world",  # Your package's GitHub repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # python_requires='>=3.10',
)
