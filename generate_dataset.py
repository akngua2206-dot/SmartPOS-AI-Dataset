# ==========================================================
# SMART POS AI DATASET GENERATOR
# Version : 2.0
# Author  : SmartPOS AI
# ==========================================================

import os
import random
import zipfile
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

random.seed(42)
np.random.seed(42)

# ==========================================================
# MEMBUAT FOLDER DATASET
# ==========================================================

OUTPUT_FOLDER = "dataset"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

print("Folder dataset siap.")

# ==========================================================
# KONFIGURASI
# ==========================================================

JUMLAH_HARI = 30

TRANSAKSI_MIN = 30

TRANSAKSI_MAX = 45

print("Konfigurasi selesai.")
