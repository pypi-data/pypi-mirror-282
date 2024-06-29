import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install as _install

class CustomInstallCommand(_install):
    def run(self):
        _install.run(self)
        if not sys.platform.startswith('darwin'):  # Skip on macOS
            self.execute_nvidia_install()

    def execute_nvidia_install(self):
        # This method will be called on the target system during installation
        check_and_install_nvidia_packages()

def check_and_install_nvidia_packages():
    try:
        import pynvml
        pynvml.nvmlInit()
        gpu_count = pynvml.nvmlDeviceGetCount()
        if gpu_count > 0:
            if os.name == 'nt' or sys.platform.startswith('linux'):
                print("NVIDIA GPUs detected. Installing NVIDIA packages...")
                # Use subprocess.check_call here if you want to install during setup
                print("To install NVIDIA packages, run the following commands:")
                print("pip install --extra-index-url=https://pypi.nvidia.com cudf-cu12==24.6.* dask-cudf-cu12==24.6.* cuml-cu12==24.6.*")
                print("pip install tensorrt")
    except ImportError:
        print("pynvml is not installed. NVIDIA GPU check skipped.")
    except Exception as e:
        print(f"An error occurred while checking for NVIDIA GPUs: {e}")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='nanosense',
    version='0.5.11',
    description='A comprehensive package for solid state nanopore data analysis and visualization.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Shankar Dutt',
    author_email='shankar.dutt@anu.edu.au',
    url='https://github.com/shankardutt/nanosense',
    packages=find_packages(include=['nanosense', 'nanosense.*']),
    include_package_data=True,
    package_data={
        'nanosense': ['icons.icns', 'image_1.jpg'],
    },
    install_requires=[
        'PySide6',
        'cryptography',
        'matplotlib',
        'neo',
        'numpy',
        'pyabf',
        'scipy',
        'joblib',
        'bottleneck',
        'ruptures',
        'pywavelets',
        'detecta',
        'hmmlearn',
        'scikit-learn',
        'h5py',
        'seaborn',
        'pandas',
        'tabulate',
        'sktime',
        'lightgbm',
        'torch',
        'torchvision',
        'tensorflow',
        'numexpr',
        'uncertainties',
        'pyqtgraph',
        'lightgbm',
        'pynvml',
        'psutil'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'nanosense=nanosense.nanosense:main',
        ],
    },
    cmdclass={
        'install': CustomInstallCommand,
    },
)