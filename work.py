import pygame
import time
def play_song_with_fadein(song_path, fadein_time):
    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0, fade_ms=fadein_time)
    print(f"Bài hát đang phát với hiệu ứng fade in trong {fadein_time / 1000:.1f} giây...")

def display_lyrics(lyrics, interval):
    print("\n--- Hiển thị lời bài hát ---")
    for line in lyrics:
        print(line)
        time.sleep(interval)
song_path = "py.mp3"
fadein_time = 5000 
#list:
# Hien  tai chua cho copy lơi bai hat duoc :(( 
# lyrics = [
#     "Dòng 1: Lại chìm trong đôi mắt em xoe tròn ngất ngây phút giây khi mà anh khẽ nhìn sang",
#     "Dòng 2: Lại làm đôi môi nhớ em lại muốn hôn em thêm bao lần",
#     "Dòng 3: Từng ngày cô đơn xé đôi, hạ thu đông khẽ trôi ,cạnh bên em anh sẽ thôi u sầu",
#     "Dòng 4: Lại làm cho anh càng thấy yêu em hơn ngày qua",
#     "Dòng 5:Chỉ cần thức giấc khi bên em nơi anh thấy yên bình"
#     ""
#     ""
#     ""
#     ""
#     ""
#     ""
#     ""
#     ""
# ]
interval = 3
try:
    play_song_with_fadein(song_path, fadein_time)
    
    display_lyrics(lyrics, interval)

    while pygame.mixer.music.get_busy():
        time.sleep(1)
except Exception as e:
    print(f"Lỗi khi phát bài hát : {e}")
finally:
    pygame.mixer.quit()

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v4

      # Runs a single command using the runners shell
      - name: Run a one-line script
        run: echo Hello, world!

      # Runs a set of commands using the runners shell
      - name: Run a multi-line script
        run: |
          echo Add other actions to build,
          echo test, and deploy your project.
