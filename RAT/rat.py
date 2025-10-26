import socket # For network communication
import threading # For handling multiple clients concurrently
import os # For file system operations
from colorama import Fore # For colored terminal output
import ctypes # For system-level operations

clients = {} # Dictionary to hold connected clients
