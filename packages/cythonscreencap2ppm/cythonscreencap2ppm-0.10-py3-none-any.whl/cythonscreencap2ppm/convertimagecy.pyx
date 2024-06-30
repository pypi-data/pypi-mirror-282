# commands to copy
# adb start-server
# adb connect 127.0.0.1:5560
# adb -s 127.0.0.1:5560 shell
# adb -s 127.0.0.1:5560 shell su -c 'rm -f -r /sdcard/cythonscreencap2ppm/'
# adb -s 127.0.0.1:5560 shell su -c 'rm -f -r /data/data/com.termux/files/usr/lib/python3.11/site-packages/cythonscreencap2ppm'
# adb -s 127.0.0.1:5560 push C:\ProgramData\anaconda3\envs\a0\cythonscreencap2ppm /sdcard/
# adb -s 127.0.0.1:5560 shell su -c 'cp -r /sdcard/cythonscreencap2ppm/ /data/data/com.termux/files/usr/lib/python3.11/site-packages/'

# adb -s 127.0.0.1:5560 shell su -c 'rm -f -r /sdcard/cythonscreencap2ppm/' & adb -s 127.0.0.1:5560 shell su -c 'rm -f -r /data/data/com.termux/files/usr/lib/python3.11/site-packages/cythonscreencap2ppm' & adb -s 127.0.0.1:5560 push C:\ProgramData\anaconda3\envs\a0\cythonscreencap2ppm /sdcard/ & adb -s 127.0.0.1:5560 shell su -c 'cp -r /sdcard/cythonscreencap2ppm/ /data/data/com.termux/files/usr/lib/python3.11/site-packages/' & adb -s 127.0.0.1:5560 shell su -c 'rm -f -r /sdcard/cythonscreencap2ppm/'
import cython
cimport cython
import numpy as np
cimport numpy as np
from libc.stdio cimport fopen, fclose, FILE,fread,fputc
from libc.stdlib cimport malloc, free
import os
import subprocess
np.import_array()

cdef int convert_screencap_c(
    char* filename,
    char* filename2,
    size_t size_of_file
) nogil:
    r"""
    Converts a raw screenshot file into another format by filtering and modifying the data. This function is not safe for Python object manipulation and runs without the GIL.

    Args:
        filename (char*): The path to the input file.
        filename2 (char*): The path to the output file.
        size_of_file (size_t): The size of the input file in bytes.

    Returns:
        int: 0 if successful, 1 if an error occurs (e.g., file not found or memory allocation failure).
    """
    cdef FILE* f = fopen(filename, "rb")
    cdef FILE* f2 = fopen(filename2, "ab")
    cdef Py_ssize_t i
    cdef cython.puchar line=NULL
    if not f:
        return 1
    if not f2:
        return 1
    try:
        line = <cython.puchar>malloc(((size_of_file )) * sizeof(cython.uchar))
        if not line:
            return 1
        fread(line, 1, ((size_of_file )), f)
        for i in range(size_of_file):
            if ((i+1) % 4 == 0) or (i<16):
                continue
            fputc((line)[i],f2)
    finally:
        fclose(f)
        fclose(f2)
        free(line)
    return 0


cdef int convert_screencap_c2np(
    cython.uchar[:] f2,
    char* filename,
    size_t size_of_file

) nogil:
    r"""
    Converts a raw screenshot file directly into a NumPy array format.

    Args:
        f2 (cython.uchar[:]): The NumPy array to fill with data.
        filename (char*): The path to the input file.
        size_of_file (size_t): The size of the input file in bytes.

    Returns:
        int: 0 if successful, 1 if an error occurs (such as file not found or memory allocation failure).
    """
    cdef Py_ssize_t counter=0
    cdef FILE* f = fopen(filename, "rb")
    cdef Py_ssize_t i
    cdef cython.puchar line=NULL
    if not f:
        return 1

    try:
        line = <cython.puchar>malloc(((size_of_file )) * sizeof(cython.uchar))
        if not line:
            return 1
        fread(line, 1, ((size_of_file )), f)
        for i in range(size_of_file):
            if ((i+1) % 4 == 0) or (i<16):
                continue
            f2[counter]=(line)[i]
            counter+=1
    finally:
        fclose(f)
        #fclose(f2)
        free(line)
    return 0

cpdef tuple[int,int] get_resolution(
    int width=0,
    int height=0):
    r"""
    Retrieves the resolution of the screen unless provided.

    Args:
        width (int): The width of the screen. If set to 0, the function will determine it automatically.
        height (int): The height of the screen. If set to 0, the function will determine it automatically.

    Returns:
        tuple[int,int]: The width and height of the screen.
    """
    cdef:
        list[str] wstri
    if width==0 or height==0:
        wstri=subprocess.run(
        'wm size',
        shell=True,
        env=os.environ,
        preexec_fn=os.setpgrp,capture_output=True
    ).stdout.decode('utf-8','ignore').strip().rsplit(maxsplit=1)[1].split('x',maxsplit=1)
        width,height=int(wstri[0]), int(wstri[1])
    return int(width),int(height)

cpdef int convert_screencap2file(
    str input_file_path,
    str output_file_path,
    int max_color_value=255,
    int width=0,
    int height=0):
    r"""
    Converts a screenshot from raw format to a PPM file.

    Args:
        input_file_path (str): The path to the raw input file (taken with screencap).
        output_file_path (str): The path where the PPM file should be saved.
        max_color_value (int): The maximum color value for the PPM format, default is 255.
        width (int): The width of the image, determined automatically if set to 0.
        height (int): The height of the image, determined automatically if set to 0.

    Returns:
        int: 0 if successful, non-zero if an error occurs.
    """
    cdef:
        cython.bytes bytefilename = input_file_path.encode()
        cython.bytes bytefilename2 = output_file_path.encode()
        cython.bytes headers
        size_t size_of_file = os.stat(input_file_path).st_size
        list[str] wstri
    width,height=get_resolution(width,height)
    headers=(f"P6\n{width} {height} {max_color_value}\n".encode())
    with open(output_file_path,mode='wb') as fi:
        fi.write(headers)
    convert_screencap_c(bytefilename,bytefilename2,size_of_file)
    return 0

cpdef np.ndarray convert_screencap2np(
    str input_file_path,
    int width=0,
    int height=0
    ):
    r"""
    Converts a screenshot from raw format (taken with screencap) directly into a NumPy array (height,width,3).

    Args:
        input_file_path (str): The path to the raw input file.
        width (int): The width of the image, determined automatically if set to 0.
        height (int): The height of the image, determined automatically if set to 0.

    Returns:
        np.ndarray: A NumPy array representing the image.
    """
    cdef:
        cython.bytes bytefilename = input_file_path.encode()
        size_t size_of_file = os.stat(input_file_path).st_size
        np.ndarray picarray
    width,height=get_resolution(width,height)
    picarray=np.zeros((width,height,3),dtype=np.uint8)
    convert_screencap_c2np(picarray.ravel(),bytefilename,size_of_file)
    return picarray

