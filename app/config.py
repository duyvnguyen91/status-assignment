import os
from dataclasses import dataclass
import datetime

# Logging configuration
import logging
log = logging.getLogger()
log.setLevel(logging.INFO)

class Config:
  """Configuration for the application."""

  # SSH Key
  key_path =  os.getenv('KeyPath')
  
  # Default username to access VM
  username = os.getenv('UserName')
  
  # Test Host
  test_host = [os.getenv('TestHost')]