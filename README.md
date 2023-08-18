# vmafTool function

评估视频质量的VMAF得分，支持windows和linux运行环境。

# usage
`
$ python main.py rtmp://101.146.101.192/ref/720p rtmp://x01.kkk.com/tz03/8-31

`

## test case

### case#1: 720p
>python main.py rtmp://1.1.1.12/ref/720p rtmp://2.kkk.com/t03/31
Note: video parameters shall be same except bitrate!
Reference-video:  rtmp://10.146.11.92/ref/720p
Video: h264 (Main), yuv420p(tv, bt709, progressive), 1280x720 [SAR 1:1 DAR 16:9], 2560 kb/s, 29.97 fps, 29.97 tbr, 1k tbn
Evaluation-video:  rtmp://g01.gyzgyy.cn/tz03/8-31
Video: h264 (Main), yuv420p(progressive), 1280x720 [SAR 1:1 DAR 16:9], 409 kb/s, 30.30 fps, 29.97 tbr, 1k tbn
VMAF score: 49.821081

### case#2: 1080p
>python main.py rtmp://1.16.1.92/ref/1080p rtmp://1.kkk.com/t03/32
Note: video parameters shall be same except bitrate!
Reference-video:  rtmp://10.146.11.92/ref/1080p
Video: h264 (Main), yuv420p(tv, bt709, progressive), 1920x1080 [SAR 1:1 DAR 16:9], 512 kb/s, 29.97 fps, 29.97 tbr, 1k tbn
Evaluation-video:  rtmp://g01.gyzgyy.cn/tz03/8-32
Video: h264 (Main), yuv420p(progressive), 1920x1080 [SAR 1:1 DAR 16:9], 1024 kb/s, 30.30 fps, 29.97 tbr, 1k tbn
VMAF score: 59.510553
