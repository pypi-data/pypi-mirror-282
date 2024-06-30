from __future__ import annotations
import re
import numpy as np
import platform
import subprocess
import os
import sys
import time
from typing import Union

try:
    from .convertimagecy import (
        get_resolution,
        convert_screencap2file,
        convert_screencap2np,
    )
except Exception as e:
    import Cython, setuptools, flatten_any_dict_iterable_or_whatsoever, xmltodict

    iswindows = "win" in platform.platform().lower()
    if iswindows:
        addtolist = []
    else:
        addtolist = ["&"]

    olddict = os.getcwd()
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)
    compile_file = os.path.join(dirname, "convertimagecy_compile.py")
    subprocess.run(
        " ".join([sys.executable, compile_file, "build_ext", "--inplace"] + addtolist),
        shell=True,
        env=os.environ,
        preexec_fn=None if iswindows else os.setpgrp,
    )
    if not iswindows:
        time.sleep(30)
    from .convertimagecy import (
        get_resolution,
        convert_screencap2file,
        convert_screencap2np,
    )

    os.chdir(olddict)


def remount_rw(
    su: str = "su", sh: str = "sh"
) -> tuple[subprocess.CompletedProcess, bool]:
    r"""
    Attempts to remount the root filesystem as read-write by executing multiple mount commands
    using different techniques and variations depending on the environment's restrictions.

    Args:
    su (str): Command to elevate privileges, defaults to 'su'.
    sh (str): Shell type to execute the commands, defaults to 'sh'.

    Returns:
    tuple[subprocess.CompletedProcess, bool]: Result of the mount operation and a boolean indicating success.
    """
    remountcmd = R"""#!/bin/sh
    check_if_mounted() {
        mountcheckervalue=0
        mountchecker="$(mount -v | grep -v 'rw' | grep 'ro' | awk 'BEGIN{FS="[\\(]+";}{print $2}' | awk 'BEGIN{FS="[\\),]+";}{if ($1 ~ /^ro$/){ print 1;exit}}')"
        echo -e "$mountchecker"
        mountcheckervalue=$((mountcheckervalue + mountchecker))
        return "$mountcheckervalue"
    }

    modr() {

        if ! check_if_mounted; then
            mount -o remount,rw /
        else
            return 0
        fi
        if ! check_if_mounted; then
            su -c "mount -o remount,rw /"
        else
            return 0
        fi

        if ! check_if_mounted; then
            su -c "mount --all -o remount,rw -t vfat1"
        else
            return 0
        fi

        if ! check_if_mounted; then
            su -c 'mount --all -o remount,rw -t ext4'
        else
            return 0
        fi

        if ! check_if_mounted; then
            su -c 'mount -o remount,rw'
        else
            return 0
        fi

        if ! check_if_mounted; then
            su -c "mount -o remount,rw /;"
        else
            return 0
        fi

        if ! check_if_mounted; then
            mount -o remount,rw /
        else
            return 0
        fi
        if ! check_if_mounted; then
            su -c "mount -o remount,rw /"
        else
            return 0
        fi

        if ! check_if_mounted; then
            su -c 'mount -o rw&&remount /'
        else
            return 0
        fi

        if ! check_if_mounted; then
            su -c 'mount -o rw;remount /'
        else
            return 0
        fi

        if ! check_if_mounted; then
            mount --all -o remount,rw -t vfat
        else
            return 0
        fi
        if ! check_if_mounted; then
            su -c "mount --all -o remount,rw -t vfat"
        else
            return 0
        fi

        if ! check_if_mounted; then
            mount -o remount,rw /
        else
            return 0
        fi
        if ! check_if_mounted; then
            su -c "mount -o remount,rw /"
        else
            return 0
        fi
        if ! check_if_mounted; then
            mount --all -o remount,rw -t vfat
        else
            return 0
        fi
        if ! check_if_mounted; then
            su -c "mount --all -o remount,rw -t vfat"
        else
            return 0
        fi
        if ! check_if_mounted; then
            getprop --help >/dev/null;su -c 'mount -o remount,rw /;'
        else
            return 0
        fi
        if ! check_if_mounted; then
            su -c 'mount -o remount,rw /;'
        else
            return 0
        fi

        if ! check_if_mounted; then
            mount -v | grep "^/" | grep -v '\\(rw,' | grep '\\(ro' | awk '{print "mount -o rw,remount " $1 " " $3}' | tr '\n' '\0' | xargs -0 -n1 su -c
        else
            return 0
        fi

        if ! check_if_mounted; then
            mount -v | grep "^/" | grep -v '\\(rw,' | grep '\\(ro' | awk '{print "mount -o rw,remount " $1 " " $3}' | su -c sh
        else
            return 0
        fi

        if ! check_if_mounted; then
            mount -v | grep "^/" | grep -v '\\(rw,' | grep '\\(ro' | awk '{system("mount -o rw,remount " $1 " " $3)}'
        else
            return 0
        fi

        if ! check_if_mounted; then
            su -c 'mount -v | grep -E "^/" | awk '\''{print "mount -o rw,remount " $1 " " $3}'\''' | tr '\n' '\0' | xargs -0 -n1 su -c
        else
            return 0
        fi

        if ! check_if_mounted; then
            mount -Ev | grep -Ev 'nodev' | grep -Ev '/proc' | grep -v '\\(rw,' | awk 'BEGIN{FS="([[:space:]]+(on|type)[[:space:]]+)|([[:space:]]+\\()"}{print "mount -o rw,remount " $1 " " $2}' | xargs -n5 | su -c
        else
            return 0
        fi

        if ! check_if_mounted; then
            su -c 'mount -v | grep -E "^/" | awk '\''{print "mount -o rw,remount " $1 " " $3}'\''' | sh su -c
        else
            return 0
        fi

        if ! check_if_mounted; then
            getprop --help >/dev/null;su -c 'mount -v | grep -E "^/" | awk '\''{print "mount -o rw,remount " $1 " " $3}'\''' | tr '\n' '\0' | xargs -0 -n1 | su -c sh
        else
            return 0
        fi
    return 1
    }
    if ! modr 2>/dev/null; then
        echo -e "FALSEFALSEFALSE"
    else
        echo -e "TRUETRUETRUE"
    fi
}
    """
    if su != "su":
        cmd2execute = re.sub(r"\bsu\b", su, remountcmd)
    else:
        cmd2execute = remountcmd
    if sh != "sh":
        cmd2execute = re.sub(r"\bsh\b", sh, cmd2execute)
    else:
        cmd2execute = cmd2execute
    stdout_stderr = subprocess.run(
        sh,
        input=cmd2execute.encode("utf-8"),
        shell=True,
        preexec_fn=os.setpgrp,
        env=os.environ,
        capture_output=True,
    )

    return stdout_stderr, True if b"TRUETRUETRUE" in stdout_stderr.stdout else False


def get_all_path_from_exe(exefile: str, sh: str = "sh") -> list[str]:
    r"""
    Finds all paths of executable files in the system that match a given filename.

    Args:
    exefile (str): The executable name to search for.
    sh (str): Shell type to execute the search command, defaults to 'sh'.

    Returns:
    list[str]: A list of paths where the executable is found.
    """
    cmd2execute = rf"""find / -type f 2>/dev/null | grep -E "/{exefile}$" | tr '\n' '\0' | xargs -n1 -0 ls -l | grep -vE "^[^x]+[[:space:]]+" | awk '{{print $NF}}\n\nexit\n\n"""
    stdout_stderr = subprocess.run(
        sh,
        input=cmd2execute.encode("utf-8"),
        shell=True,
        preexec_fn=os.setpgrp,
        env=os.environ,
        capture_output=True,
    )
    return [
        x.strip() for x in stdout_stderr.stdout.decode("utf-8", "ignore").splitlines()
    ]


def get_all_su() -> list[str]:
    r"""
    Retrieves all paths where the 'su' executable is located across the system.

    Returns:
    list[str]: A list containing all the paths for 'su'.
    """
    return get_all_path_from_exe("su") + ["su"]


def get_all_sh() -> list[str]:
    r"""
    Retrieves all paths where the 'sh' executable is located across the system.

    Returns:
    list[str]: A list containing all the paths for 'sh'.
    """
    return get_all_path_from_exe("sh") + ["sh"]


def remount_rw_all_shell_su_combinations() -> (
    tuple[Union[subprocess.CompletedProcess, None], bool]
):
    r"""
    Tries to remount the filesystem as read-write using all combinations of 'su' and 'sh' found on the system.

    Returns:
    tuple[Union[subprocess.CompletedProcess, None], bool]: The result of the last mount attempt and a boolean indicating if any attempt was successful.
    """
    are_we_done = False
    stdout_stderr = None
    for su in get_all_su():
        if are_we_done:
            break
        for sh in get_all_sh():
            stdout_stderr, are_we_done = remount_rw(su, sh)
            if are_we_done:
                break
    return stdout_stderr, are_we_done


def mount_memory_disk(
    path: str = "/media/ramdisk",
    mb: int = 256,
    su: str = "su",
    sh: str = "sh",
    try_all_combinations: bool = False,
) -> tuple[
    Union[subprocess.CompletedProcess, None],
    Union[subprocess.CompletedProcess, None],
    bool,
]:
    memcmd = (
        f"""{su} -c 'mkdir -p {path};mount -t tmpfs -o size={mb}M tmpfs {path}'\n"""
    )
    if not try_all_combinations:
        stdout_stderr, are_we_done = remount_rw(su, sh)
    else:
        stdout_stderr, are_we_done = remount_rw_all_shell_su_combinations()
    stdout_stderr2 = subprocess.run(
        sh,
        input=memcmd.encode("utf-8"),
        shell=True,
        preexec_fn=os.setpgrp,
        env=os.environ,
        capture_output=True,
    )
    return stdout_stderr2, stdout_stderr, are_we_done


def unmount_memory_disk(
    path: str = "/media/ramdisk", su: str = "su", sh: str = "sh"
) -> Union[subprocess.CompletedProcess, None]:
    stdout_stderr2 = subprocess.run(
        sh,
        input=f"""{su} -c 'umount {path}'\n""".encode("utf-8"),
        shell=True,
        preexec_fn=os.setpgrp,
        env=os.environ,
        capture_output=True,
    )
    return stdout_stderr2


class Screencaptaker(object):
    r"""
    A class to manage taking and processing screenshots on rooted Android devices with Python installed.

    Attributes:
    path (str): Base path for storing screenshots.
    mb (int): Memory size in MB to use for the ramdisk.
    sh (str): Shell type to execute system commands.
    pure_shot (str): Filename for the raw screenshot.
    converted_shot (str): Filename for the processed screenshot.
    width (int): Width of the screenshot, defaults to system's resolution if not set.
    height (int): Height of the screenshot, defaults to system's resolution if not set.
    max_color_value (int): Maximum color value for the processed image, defaults to 255.
    """

    def __init__(
        self,
        path: str = "/media/ramdisk",
        mb: int = 256,
        sh: str = "sh",
        pure_shot: str = "pure_shot.raw",
        converted_shot: str = "converted_shot.ppm",
        width: int = 0,
        height: int = 0,
        max_color_value: int = 255,
    ):
        r"""
        Initializes a Screencaptaker instance with specified parameters or defaults.

        Args:
            path (str): Base path for storing screenshots.
            mb (int): Memory size in MB to use for the ramdisk.
            sh (str): Shell type to execute system commands.
            pure_shot (str): Filename for the raw screenshot.
            converted_shot (str): Filename for the processed screenshot.
            width (int): Width of the screenshot, initialized here or set to system's resolution.
            height (int): Height of the screenshot, initialized here or set to system's resolution.
            max_color_value (int): Maximum color value for the processed image.
        """
        if width == 0 or height == 0:
            self.width, self.height = get_resolution()
        else:
            self.width, self.height = width, height
        self.max_color_value = max_color_value
        self.path = "/" + path.strip("/ ") + "/"
        self.mb = mb
        self.sh = sh
        self.pure_shot = self.path + pure_shot
        self.converted_shot = self.path + converted_shot
        self.checkfile = self.path + "ok.txt"

    def _get_screenshot(self, timeout: int = 10) -> bool:
        r"""
        Captures a screenshot and writes it to a raw file.

        Args:
            timeout (int): Maximum time allowed for the screencap command to execute.

        Returns:
            bool: True if the screenshot was successfully captured, False otherwise.
        """
        if "LD_LIBRARY_PATH" in os.environ:
            try:
                del os.environ["LD_LIBRARY_PATH"]
            except Exception:
                pass
        fi = open(self.pure_shot, mode="wb")
        result = False
        try:
            subprocess.run(f"""screencap""", stdout=fi, timeout=timeout)
            result = True
        except subprocess.TimeoutExpired:
            result = False
        finally:
            fi.close()
        return result

    def get_screenshot_as_file(self, timeout: int = 10) -> bool:
        r"""
        Captures a screenshot and saves it as a processed file in a specified format.

        Args:
            timeout (int): Maximum time allowed for the screencap command to execute.

        Returns:
            bool: True if the screenshot was successfully captured and converted, False otherwise.
        """
        was_ok = self._get_screenshot(timeout=timeout)
        if was_ok:
            convert_screencap2file(
                self.pure_shot,
                self.converted_shot,
                max_color_value=self.max_color_value,
                width=self.width,
                height=self.height,
            )
        else:
            return False
        return was_ok

    def get_screenshot_as_np(self, timeout: int = 10) -> np.ndarray:
        r"""
        Captures a screenshot and returns it as a NumPy array.

        Args:
            timeout (int): Maximum time allowed for the screencap command to execute.

        Returns:
            np.ndarray: A NumPy array representing the screenshot, or an empty array if capture failed.
        """
        was_ok = self._get_screenshot(timeout=timeout)
        if was_ok:
            return convert_screencap2np(
                self.pure_shot,
                width=self.width,
                height=self.height,
            )
        else:
            return np.array([], dtype=np.uint16)
        return np.array([], dtype=np.uint16)
