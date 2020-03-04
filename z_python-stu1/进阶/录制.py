
'''
阅读下面的两个知识点

1.
ffmpeg可以用下面的参数来录制Windows
桌面操作的视频。

ffmpeg.exe - y - rtbufsize
100
M - f
gdigrab - framerate
10 - draw_mouse
1 - i
desktop
-c: v
libx264 - r
20 - crf
35 - pix_fmt
yuv420p - fs
100
M
"fffffffffffffffff"

其中
fffffffffffffffff
部分
是需要填入
产生的视频文件名。

录制过程中，用户按键盘
q
键，可以退出录制。


2.
ffmpeg还可以用来合并视频文件，windows下面的格式如下

ffmpeg.exe - f
concat - i
concat.txt - codec
copy
out.mp4

其中concat.txt
是要合并视频的文件列表。格式如下，每行以file
开头
后面是要合并的视频文件名：

file
20170330_110818.
mp4
file
20170330_110833.
mp4

------------------------------
下载ffmpeg程序(进入
http: // ffmpeg.zeranoe.com / builds / 点击
Download
FFmpeg按钮即可)

要求大家写一个python程序，运行后提示用户是要做什么操作，如下
'请选择您要做的操作：1：录制视频，2：合并视频：'

如果用户输入1并回车， 则调用ffmpeg录制视频文件，产生在当前目录下面。
要求录制的视频文件名
是当前时间（年月日_时分秒.mp4格式），
比如
'20170330_093612.mp4' （怎么产生这种时间格式的字符串，不知道的请自行网上搜索方法）

如果用户输入2并回车，则按字母顺序列出当前目录下所有的
mp4为扩展名
的视频文件(怎么列出，请自行网上搜索方法)，并在前面编上序号。如下所示

---------------------------------
目录中有这些视频文件：
1 - 20170329_202814.
mp4
2 - 20170330_093251.
mp4
3 - 20170330_093612.
mp4

请选择要合并视频的视频文件序号(格式
1, 2, 3, 4):
---------------------------------

用户输入视频序号（序号以逗号隔开）后， 程序合并视频文件， 输出的合并后视频文件名
固定为
out.mp4

【参考答案，往下翻】

'''





























# coding=utf8
import time, os
import glob

FFMPEG_PATH = 'd:/data/bandicam/tmp/ffmpeg.exe'
VIDEO_DIR = 'd:\\'


def recording():
    # 输出视频文件
    outputfile = VIDEO_DIR + time.strftime('%Y%m%d_%H%M%S', time.localtime()) + '.mp4'

    # 工具目录

    settings = '-y -rtbufsize 100M -f gdigrab -framerate 20 ' + \
               '-draw_mouse 1 -i desktop -c:v libx264 -r 20 ' + \
               '-crf 35 -pix_fmt yuv420p ' \
               '-fs 100M   "%s"' % outputfile

    recordingCmdLine = FFMPEG_PATH + ' ' + settings

    # 查看命令内容
    print(recordingCmdLine)

    # 执行命令录制视频
    os.system(recordingCmdLine)


def merging():
    os.chdir(VIDEO_DIR)
    fileList = glob.glob(VIDEO_DIR + '*.mp4')
    fileList = [os.path.basename(one) for one in fileList]

    if fileList:
        print('\n目录中有这些视频文件：')
    else:
        print('\n目录中没有视频文件')
        return

    idx = 1
    for one in fileList:
        print('%s - %s' % (idx, one))
        idx += 1

    print('\n请选择要合并视频的视频文件序号(格式 1,2,3,4) :', end=' ')

    mergeSequence = input('')
    videoFilesToMer = mergeSequence.split(',')
    videoFileNamesToMer = [fileList[int(one.strip()) - 1] for one in videoFilesToMer]

    print(videoFileNamesToMer)

    with open('concat.txt', 'w', encoding='utf8') as f:
        for one in videoFileNamesToMer:
            f.write('file ' + one + '\n')

    cmd = FFMPEG_PATH + ' -f concat -i concat.txt -codec copy out.mp4'
    # 执行命令录制视频
    os.system(cmd)


while True:
    print('\n请选择您要做的操作：1-录制视频，2-合并视频 :', end=' ')
    choice = input('')
    if choice == '1':
        recording()
    elif choice == '2':
        merging()