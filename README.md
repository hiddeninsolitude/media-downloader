# Media Downloader

A simple Python script to download videos and audio from YouTube and SoundCloud.

![Screenshot](https://cdn.discordapp.com/attachments/1388116968741146677/1459236740823908465/HgCPV7E.png?ex=69628b9e&is=69613a1e&hm=9b1d0322e6b48b90e35de5e416c53eb2568ab3d44fe32f1526143cdc6e356dd3&)

## Quick Start

1. **Download:**
   ```bash
   git clone https://github.com/hiddeninsolitude/media-downloader.git
   cd media-downloader
   ```

2. **Run:**
   ```bash
   python downloader.py
   ```

That's it! The script automatically installs everything it needs.

## Features

- Download YouTube videos (MP4: 1080p, 720p, 480p)
- Download YouTube audio (MP3, OPUS, AAC, FLAC, WAV, VORBIS)
- Download SoundCloud tracks (MP3, OPUS, AAC, FLAC, WAV, VORBIS)
- Colorful interface with ASCII art
- Automatic dependency installation
- Organized downloads by format

## Requirements

- Python 3.7 or higher
- Internet connection

Everything else installs automatically!

## Usage

1. Run the script
2. Choose platform (YouTube or SoundCloud)
3. Paste the URL
4. Select format and quality
5. Wait for download to complete

Downloads are saved in the `downloads` folder, organized by format.

## Troubleshooting

**FFmpeg not found?**
- Windows: `winget install Gyan.FFmpeg`
- Mac: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

**Script won't start?**
- Check Python version: `python --version` (must be 3.7+)
- Reinstall dependencies: `pip install -r requirements.txt`

**Download fails?**
- Check your internet connection
- Update yt-dlp: `pip install --upgrade yt-dlp`
- Try a different video/track

## Building an Executable

Want a standalone .exe file? Run:

```bash
python -m PyInstaller --onefile --name="MediaDownloader" --console downloader.py
```

Your executable will be in the `dist` folder.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for personal use only. Respect copyright laws and platform terms of service. Only download content you have the right to download.

## Author

Created by **@hiddeninsolitude**

- Discord: @hiddeninsolitude
- GitHub: [hiddeninsolitude](https://github.com/hiddeninsolitude)

---

**Star this repo if you find it useful!**
