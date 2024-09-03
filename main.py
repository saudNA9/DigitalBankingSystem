from datetime import datetime, timedelta
import uuid
import csv
import logging
import sys
import tkinter as tk
from tkinter import messagebox

# Set up logging to stdout instead of stderr
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(asctime)s - %(levelname)s - %(message)s')
