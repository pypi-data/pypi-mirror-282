# screencap to ppm 

### Tested against Windows 10 / Python 3.11 / Anaconda / BlueStacks (Android 11 - rooted with Python installed) 

### pip install cythonscreencap2ppm


```py
from cythonscreencap2ppm import (
    Screencaptaker,
    mount_memory_disk,
    remount_rw,
    convert_screencap2file,
    convert_screencap2np,
    get_all_sh,
    get_all_su,
    get_resolution,
    remount_rw,
    remount_rw_all_shell_su_combinations,
    unmount_memory_disk,
)
import os

os.environ["OMP_THREAD_LIMIT"] = "1"
mount_memory_disk(
    path="/media/ramdisk", mb=256, su="su", sh="sh", try_all_combinations=False
)

# class to take screenshots with screencap (raw RGB data - NOT PNG! ) and convert to PPM
self = Screencaptaker(
    path="/media/ramdisk",
    mb=256,
    sh="sh",
    pure_shot="pure_shot.raw",
    converted_shot="converted_shot.ppm",
    width=0,
    height=0,
    max_color_value=255,
)

counter = 0
while True:
    nparraybuf = self.get_screenshot_as_np()
    print(nparraybuf.shape, counter, end="\r")
    counter += 1

# Example of using remount_rw to attempt remounting the root filesystem as read-write
result, success = remount_rw("su", "sh")
# Convert a raw screenshot file to a PPM format and save it
convert_screencap2file(
    "/path/to/input.raw",
    "/path/to/output.ppm",
    max_color_value=255,
    width=0,
    height=0,
)
# Convert a raw screenshot file directly into a NumPy array
image_array = convert_screencap2np("/path/to/input.raw", width=0, height=0)
print("Image array shape:", image_array.shape)
# Retrieve all paths where the 'sh' shell executable is found
sh_paths = get_all_sh()
print("SH paths found:", sh_paths)
# Retrieve all paths where the 'su' executable is found
su_paths = get_all_su()
print("SU paths found:", su_paths)
# Get the screen resolution of the device
width, height = get_resolution()
print("Screen resolution:", width, "x", height)
# Try to remount the root filesystem as read-write using all combinations of 'su' and 'sh' paths
stdout_stderr, success = remount_rw_all_shell_su_combinations()
print("Remount attempt successful:", success)
# Unmount a previously mounted memory disk
result = unmount_memory_disk("/media/ramdisk", "su", "sh")
print("Unmount operation completed")
# Example of mounting a memory disk to a specified path with a defined size
mount_memory_disk(
    path="/media/ramdisk", mb=256, su="su", sh="sh", try_all_combinations=False
)
print("Memory disk mounted at /media/ramdisk with size 256MB")
```