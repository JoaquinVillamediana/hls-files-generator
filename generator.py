import subprocess
import os

def main():
  dirname = os.getcwd()
  ext = ('.mp4')

  # iterating over all files
  for files in os.listdir(dirname):
    if files.endswith(ext):
        file_name = files
        file_name = file_name.replace(".mp4", "")

        print(f"Generating Segments of {file_name}...")
        
        os.mkdir(file_name)

        createSegments(file_name)
        createIndex(file_name)


def createSegments(file_name):
  print(f"360p of {file_name}...")
  call_ffmpeg(f'ffmpeg -i {file_name}.mp4 -profile:v baseline -level 3.0 -s 640x360  -start_number 0 -hls_time 15 -hls_list_size 0 -f hls ./{file_name}/360_video.m3u8')
  print(f"760p of {file_name}...")
  call_ffmpeg(f'ffmpeg -i {file_name}.mp4 -profile:v baseline -level 3.0 -s 1280x720  -start_number 0 -hls_time 15 -hls_list_size 0 -f hls ./{file_name}/720_video.m3u8')
  print(f"1080p of {file_name}...")
  call_ffmpeg(f'ffmpeg -i {file_name}.mp4 -profile:v baseline -level 3.0 -s 1920x1080  -start_number 0 -hls_time 15 -hls_list_size 0 -f hls ./{file_name}/1080_video.m3u8')

def createIndex(file_name):
  f = open(f"{file_name}/index.m3u8", "w")
  f.write("#EXTM3U\n#EXT-X-STREAM-INF:BANDWIDTH=375000,RESOLUTION=640x360\n360_video.m3u8\n#EXT-X-STREAM-INF:BANDWIDTH=2000000,RESOLUTION=1280x720\n720_video.m3u8\n#EXT-X-STREAM-INF:BANDWIDTH=3500000,RESOLUTION=1920x1080\n1080_video.m3u8")

def call_ffmpeg(cmd):
  with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
    process.communicate()
  return True


if __name__ == "__main__":
  main()
 
