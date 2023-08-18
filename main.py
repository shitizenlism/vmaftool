#!/usr/bin/python

import re
import sys
import subprocess

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <Reference Video> <Evaluation Video>")
        sys.exit(1)

    _flags = "bicubic"
    filter_param = "[1:v]format=yuv420p[main];[0:v]format=yuv420p[ref];"
    filter_param += f"[main][ref]scale2ref=flags={_flags}," \
                    f"libvmaf=n_threads=4:model_path=models/vmaf_v0.6.1.json"

    cmd = ["bin\\ffmpeg-v512.exe", "-hide_banner", "-y", "-threads", "1"]
    cmd += ["-i", sys.argv[1]]
    cmd += ["-i", sys.argv[2]]
    cmd += ["-t", "60"]
    cmd += ["-filter_complex", filter_param]
    cmd += ["-f", "null"]
    cmd += ["-"]

    # banner = "".join(["-"] * 10) + " VMAF Test " + "".join(["-"] * 30)
    # print()
    # print(banner)
    # print(" ".join(cmd))

    print("Note: video parameters shall be same except bitrate!")
    with subprocess.Popen(cmd, stderr=subprocess.PIPE, shell=False) as handle:
        _, raw = handle.communicate(timeout=120)

    info = raw.decode()
    out = re.search(r"(VMAF.*score.*)", info)
    stream_info = re.findall(r"Stream.*(Video:.*tbn)", info)
    print("Reference-video: ", sys.argv[1])
    print(stream_info[0])
    print("Evaluation-video: ", sys.argv[2])
    print(stream_info[1])
    if out:
        print(out.group(1))
    else:
        print(info)
