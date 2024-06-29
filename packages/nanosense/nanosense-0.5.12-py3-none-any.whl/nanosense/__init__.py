import logging
import os
import sys
import subprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_and_install_nvidia_packages():
    logger.info("Checking for NVIDIA GPU...")
    try:
        import pynvml
        pynvml.nvmlInit()
        gpu_count = pynvml.nvmlDeviceGetCount()
        if gpu_count > 0 and (os.name == 'nt' or sys.platform.startswith('linux')):
            logger.info(f"Found {gpu_count} NVIDIA GPU(s). Installing NVIDIA packages...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install",
                "--extra-index-url=https://pypi.nvidia.com",
                "cudf-cu12==24.6.*", "dask-cudf-cu12==24.6.*", "cuml-cu12==24.6.*"
            ])
            subprocess.check_call([
                sys.executable, "-m", "pip", "install",
                "tensorrt"
            ])
            logger.info("NVIDIA packages installed successfully.")
        else:
            logger.info("No NVIDIA GPU detected or not on Windows/Linux. Skipping NVIDIA package installation.")
    except ImportError:
        logger.warning("pynvml is not installed. Skipping NVIDIA package check and installation.")
    except Exception as e:
        logger.error(f"An error occurred while checking/installing NVIDIA packages: {e}")

# Run the check when the package is imported
check_and_install_nvidia_packages()

# Import main functionality
from .core import *
from .utils import *

__version__ = "0.5.12"  # Update this manually or use setuptools_scm for automatic versioning