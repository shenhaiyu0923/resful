import time,os

#输出视频文件
outputfile='e:/ccc/'+time.strftime('%Y%m%d_%H%M%S',time.localtime())+'.mp4'#输出文件路径

ffmpegDir='d:/ffmpeg/ffmpeg/bin/ffmpeg.exe'

settings = '-y -rtbufsize 100M -f gdigrab -framerate 20 ' + \
           '-draw_mouse 1 -i desktop -c:v libx264 -r 20 ' + \
           '-crf 35 -pix_fmt yuv420p ' \
           '-fs 100M   "%s"' % outputfile

#将参数组合起来
recordingCmdLine = ffmpegDir + ' ' + settings
#查看参数命令
print(recordingCmdLine)
#执行
os.system(recordingCmdLine)
















