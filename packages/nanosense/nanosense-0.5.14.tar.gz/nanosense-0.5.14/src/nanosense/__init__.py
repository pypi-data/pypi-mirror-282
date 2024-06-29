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
from .nanosense import *

# Import other modules
# from . import Clustering_and_Data_Reduction
# from . import Combine_Datasets_and_Files
# from . import Data_Reduction
# from . import Data_Visualisation
# from . import Event_Analysis
# from . import Frequency_and_multi_plots
# from . import ML_Analysis
# from . import Nanopore_Size_Calc
# from . import Plotting_and_selecting
# from . import Reduction_Settings_Viewer
# from . import Resource_Monitor
# from . import Spectrogram_and_PSD

__version__ = "0.5.14"  # Make sure this matches the version in pyproject.toml and setup.py