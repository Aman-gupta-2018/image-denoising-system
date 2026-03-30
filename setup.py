from setuptools import setup, find_packages

setup(
    name='image-denoising-system',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torch',
        'fastapi',
        'uvicorn',
        'pillow',
        'numpy',
        'opencv-python',
        'scikit-image',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'denoise=src.cli:main',
        ],
    },
)