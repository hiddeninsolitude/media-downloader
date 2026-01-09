import yt_dlp
import sys
import os
import subprocess
import shutil
import site
from colorama import Fore, Back, Style, init

init(autoreset=True)

def check_dependencies():
    needs_restart = False
    
    try:
        import colorama
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'], 
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        needs_restart = True
    
    try:
        import yt_dlp
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yt-dlp'],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        needs_restart = True
    
    if shutil.which('ffmpeg') is None:
        try:
            result = subprocess.run(
                ['winget', 'install', 'Gyan.FFmpeg', '--silent'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                needs_restart = True
        except:
            pass
    
    if needs_restart:
        os.execv(sys.executable, [sys.executable] + sys.argv)

def download_video(url, format_type='mp4', quality='1080', platform='youtube', audio_format='mp3'):
    if format_type.lower() == 'mp4':
        output_dir = os.path.join('downloads', 'mp4')
    else:
        output_dir = os.path.join('downloads', audio_format)
    
    os.makedirs(output_dir, exist_ok=True)
    
    if format_type.lower() != 'mp4':
        quality_settings = {
            'mp3': '192',
            'opus': '128',
            'aac': '192',
            'flac': '0',
            'wav': '0',
            'vorbis': '5'
        }
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': audio_format,
                'preferredquality': quality_settings.get(audio_format, '192'),
            }],
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        }
    else:
        ydl_opts = {
            'format': f'bestvideo[height<={quality}][vcodec^=avc]+bestaudio/bestvideo[height<={quality}]+bestaudio/best[height<={quality}]/best',
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'postprocessor_args': {
                'ffmpeg': ['-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k']
            },
        }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            format_display = audio_format.upper() if format_type != 'mp4' else format_type.upper()
            print(f"{Fore.CYAN}Downloading from {Fore.YELLOW}{platform.title()}{Fore.CYAN} as {Fore.YELLOW}{format_display}{Fore.CYAN} to {Fore.MAGENTA}{output_dir}{Fore.CYAN}...")
            ydl.download([url])
            print(f"{Fore.GREEN}✓ Download completed successfully! {Fore.CYAN}Saved to: {Fore.MAGENTA}{output_dir}")
    except Exception as e:
        print(f"{Fore.RED}✗ Error: {e}")
        sys.exit(1)

def main():
    if os.name == 'nt':
        try:
            os.system('mode con: cols=130 lines=40')
        except:
            pass
    
    ascii_art = f"""
{Fore.MAGENTA}
 ███╗   ███╗███████╗██████╗ ██╗ █████╗     ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
 ████╗ ████║██╔════╝██╔══██╗██║██╔══██╗    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 ██╔████╔██║█████╗  ██║  ██║██║███████║    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
 ██║╚██╔╝██║██╔══╝  ██║  ██║██║██╔══██║    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
 ██║ ╚═╝ ██║███████╗██████╔╝██║██║  ██║    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
 ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}
{Fore.YELLOW}                              YouTube & SoundCloud Downloader - v1.0
{Fore.GREEN}                              Download videos and audio in multiple formats!
{Fore.LIGHTBLACK_EX}                              Created by @hiddeninsolitude - Discord
"""
    print(ascii_art)
    print(f"{Fore.MAGENTA}{'═' * 120}")
    print()
    
    check_dependencies()
    
    while True:
        print(f"{Fore.YELLOW}Select platform:")
        print(f"{Fore.RED}1. YouTube")
        print(f"{Fore.LIGHTYELLOW_EX}2. SoundCloud")
        print(f"{Fore.LIGHTBLACK_EX}3. Spotify (Currently Unavailable)")
        platform_choice = input(f"{Fore.CYAN}Enter choice (1-2): {Style.RESET_ALL}").strip()
        
        if platform_choice == '3':
            print(f"\n{Fore.RED}✗ Spotify downloading is currently unavailable.")
            print(f"{Fore.YELLOW}Please use YouTube or SoundCloud instead.\n")
            continue
        
        platform_map = {'1': 'youtube', '2': 'soundcloud'}
        platform = platform_map.get(platform_choice, 'youtube')
        
        url = input(f"{Fore.CYAN}Enter {platform.title()} URL: {Style.RESET_ALL}").strip()
        
        audio_format = 'mp3'
        
        if platform == 'soundcloud':
            print(f"\n{Fore.YELLOW}Select audio format:")
            print(f"{Fore.GREEN}1. MP3 (192kbps) - Most compatible")
            print(f"{Fore.CYAN}2. OPUS (128kbps) - Better quality at lower bitrate")
            print(f"{Fore.BLUE}3. AAC (192kbps) - Apple devices")
            print(f"{Fore.MAGENTA}4. FLAC - Lossless (large file)")
            print(f"{Fore.YELLOW}5. WAV - Uncompressed (very large)")
            print(f"{Fore.LIGHTGREEN_EX}6. VORBIS (OGG) - Open source")
            audio_choice = input(f"{Fore.CYAN}Enter choice (1-6): {Style.RESET_ALL}").strip()
            
            audio_format_map = {
                '1': 'mp3',
                '2': 'opus',
                '3': 'aac',
                '4': 'flac',
                '5': 'wav',
                '6': 'vorbis'
            }
            audio_format = audio_format_map.get(audio_choice, 'mp3')
            format_type = 'audio'
            quality = None
        else:
            print(f"\n{Fore.YELLOW}Select format:")
            print(f"{Fore.GREEN}1. MP4 (Video)")
            print(f"{Fore.BLUE}2. Audio only")
            choice = input(f"{Fore.CYAN}Enter choice (1 or 2): {Style.RESET_ALL}").strip()
            
            format_type = 'mp4' if choice == '1' else 'audio'
            
            if format_type == 'mp4':
                print(f"\n{Fore.YELLOW}Select quality:")
                print(f"{Fore.GREEN}1. 1080p")
                print(f"{Fore.CYAN}2. 720p")
                print(f"{Fore.BLUE}3. 480p")
                quality_choice = input(f"{Fore.CYAN}Enter choice (1-3): {Style.RESET_ALL}").strip()
                quality_map = {'1': '1080', '2': '720', '3': '480'}
                quality = quality_map.get(quality_choice, '1080')
            else:
                print(f"\n{Fore.YELLOW}Select audio format:")
                print(f"{Fore.GREEN}1. MP3 (192kbps) - Most compatible")
                print(f"{Fore.CYAN}2. OPUS (128kbps) - Better quality at lower bitrate")
                print(f"{Fore.BLUE}3. AAC (192kbps) - Apple devices")
                print(f"{Fore.MAGENTA}4. FLAC - Lossless (large file)")
                print(f"{Fore.YELLOW}5. WAV - Uncompressed (very large)")
                print(f"{Fore.LIGHTGREEN_EX}6. VORBIS (OGG) - Open source")
                audio_choice = input(f"{Fore.CYAN}Enter choice (1-6): {Style.RESET_ALL}").strip()
                
                audio_format_map = {
                    '1': 'mp3',
                    '2': 'opus',
                    '3': 'aac',
                    '4': 'flac',
                    '5': 'wav',
                    '6': 'vorbis'
                }
                audio_format = audio_format_map.get(audio_choice, 'mp3')
                quality = None
        
        download_video(url, format_type, quality, platform, audio_format)
        
        print(f"\n{Fore.CYAN}Download another? (y/n): {Style.RESET_ALL}", end='')
        another = input().strip().lower()
        if another != 'y':
            print(f"\n{Fore.GREEN}Thanks for using Media Downloader! Goodbye! 👋")
            break
        print()

if __name__ == "__main__":
    main()
