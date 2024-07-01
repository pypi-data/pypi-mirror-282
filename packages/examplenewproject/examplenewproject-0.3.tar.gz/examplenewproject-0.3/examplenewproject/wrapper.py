# isimproje/wrapper.py

import ctypes
import os

# .so dosyasının yolunu belirleyin
_so_path = os.path.join(os.path.dirname(__file__), "examplenewproject.cpython-311-darwin.so")
_so = ctypes.CDLL(_so_path)

# .so dosyasındaki fonksiyonları Python fonksiyonlarına sarın
_so.process_files.argtypes = [ctypes.c_int, ctypes.c_float, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p)]
_so.process_files.restype = ctypes.POINTER(ctypes.c_char_p)

def process_files(num_iterations, threshold, num_clusters, seed, file_list):
    file_list_ctypes = (ctypes.c_char_p * len(file_list))(*[f.encode('utf-8') for f in file_list])
    results = _so.process_files(num_iterations, threshold, num_clusters, seed, file_list_ctypes)
    return [results[i].decode('utf-8') for i in range(len(file_list))]
