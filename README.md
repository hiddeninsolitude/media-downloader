# ðŸŽ¬ Media Downloader - YouTube & SoundCloud

<div align="center">

![Version](https://img.shields.io/badge/version-1.0-purple)
![Python](https://img.shields.io/badge/python-3.7+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

**A powerful, colorful, and user-friendly command-line tool for downloading videos and audio from YouTube and SoundCloud**

[Features](#-features) â€¢ [Installation](#-installation) â€¢ [Usage](#-usage) â€¢ [Documentation](#-documentation) â€¢ [Contributing](#-contributing)

</div>

---

## ðŸ“– Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Requirements](#-requirements)
- [Installation](#-installation)
  - [Quick Start](#quick-start-recommended)
  - [From Source](#from-source)
  - [Pre-built Executable](#pre-built-executable-windows)
  - [Build Your Own](#build-your-own-executable)
- [Usage](#-usage)
  - [Basic Usage](#basic-usage)
  - [Step-by-Step Guide](#step-by-step-guide)
  - [Advanced Options](#advanced-options)
- [Audio Formats](#-audio-formats)
- [Video Quality Options](#-video-quality-options)
- [Download Organization](#-download-organization)
- [Supported Platforms](#-supported-platforms)
- [Technical Details](#-technical-details)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-frequently-asked-questions)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Disclaimer](#%EF%B8%8F-disclaimer)

---

## ðŸŒŸ Overview

Media Downloader is a feature-rich Python application that simplifies downloading content from YouTube and SoundCloud. With its beautiful ASCII art interface, automatic dependency management, and support for multiple formats, it provides a seamless downloading experience for users of all skill levels.

### Why Choose Media Downloader?

- **ðŸŽ¨ Beautiful Interface**: Colorful ASCII art and intuitive menus make downloading enjoyable
- **ðŸ”„ Zero Configuration**: Automatically installs and configures all dependencies
- **ðŸ“ Smart Organization**: Downloads are automatically sorted into format-specific folders
- **ðŸŽµ Format Flexibility**: Choose from 6 different audio formats to suit your needs
- **ðŸŽ¥ Quality Control**: Select video quality from 480p to 1080p
- **âš¡ Fast & Reliable**: Built on yt-dlp, the most powerful download engine available
- **ðŸ”’ Safe & Open Source**: Fully transparent code you can review and modify

---

## âœ¨ Features

### Core Features

- **Multi-Platform Support**
  - YouTube video downloads (MP4 format)
  - YouTube audio extraction
  - SoundCloud track downloads
  - More platforms coming soon!

- **Multiple Format Support**
  - 6 audio formats: MP3, OPUS, AAC, FLAC, WAV, VORBIS
  - Video formats: MP4 (480p, 720p, 1080p)
  - Automatic format conversion using FFmpeg

- **User Experience**
  - Colorful, rainbow-themed interface
  - Beautiful ASCII art banner
  - Interactive menu system
  - Real-time download progress
  - Automatic window resizing for optimal display

- **Smart Features**
  - Automatic dependency detection and installation
  - Auto-restart after dependency installation
  - Organized folder structure by format
  - Automatic filename generation from video/track titles
  - Error handling with helpful messages

- **Developer Friendly**
  - Clean, well-documented code
  - Easy to extend and modify
  - Built with modern Python practices
  - Includes build scripts for creating executables

---

## ðŸ“¸ Screenshots

```
 â–ˆâ–ˆâ–ˆâ•—   â–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ•—    â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ•—   â–ˆâ–ˆâ•—â–ˆâ–ˆâ•—      â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— 
 â–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—    â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘    â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•”â•â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—
 â–ˆâ–ˆâ•”â–ˆâ–ˆâ–ˆâ–ˆâ•”â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘    â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘ â–ˆâ•— â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â–ˆâ–ˆâ•— â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•
 â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â•  â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘    â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•‘   â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â•  â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—
 â–ˆâ–ˆâ•‘ â•šâ•â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘    â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â•šâ–ˆâ–ˆâ–ˆâ•”â–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘ â•šâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘
 â•šâ•â•     â•šâ•â•â•šâ•â•â•â•â•â•â•â•šâ•â•â•â•â•â• â•šâ•â•â•šâ•â•  â•šâ•â•    â•šâ•â•â•â•â•â•  â•šâ•â•â•â•â•â•  â•šâ•â•â•â•šâ•â•â• â•šâ•â•  â•šâ•â•â•â•â•šâ•â•â•â•â•â•â• â•šâ•â•â•â•â•â• â•šâ•â•  â•šâ•â•â•šâ•â•â•â•â•â• â•šâ•â•â•â•â•â•â•â•šâ•â•  â•šâ•â•

                              YouTube & SoundCloud Downloader - v1.0
                              Download videos and audio in multiple formats!
                              Created by @hiddeninsolitude - Discord
```

---

## ðŸ“‹ Requirements

### System Requirements

- **Operating System**: Windows 10/11, macOS 10.14+, or Linux
- **Python**: Version 3.7 or higher
- **RAM**: 512 MB minimum (1 GB recommended)
- **Storage**: 100 MB for application + space for downloads
- **Internet**: Stable connection required for downloading

### Software Dependencies

All dependencies are automatically installed by the script:

- **yt-dlp** (2024.0+) - Download engine
- **colorama** (0.4.0+) - Terminal colors
- **FFmpeg** - Audio/video processing (auto-installed on Windows)

---

## ðŸš€ Installation

### Quick Start (Recommended)

1. **Download the script:**
   ```bash
   git clone https://github.com/hiddeninsolitude/media-downloader.git
   cd media-downloader
   ```

2. **Run it:**
   ```bash
   python downloader.py
   ```

That's it! The script will automatically install all required dependencies on first run.

### From Source

**Step 1: Clone the Repository**
```bash
git clone https://github.com/hiddeninsolitude/media-downloader.git
cd media-downloader
```

**Step 2: Install Dependencies (Optional)**
```bash
pip install -r requirements.txt
```
*Note: The script will auto-install these if you skip this step*

**Step 3: Run the Script**
```bash
python downloader.py
```

### Pre-built Executable (Windows)

**For users who don't have Python installed:**

1. Go to the [Releases](https://github.com/hiddeninsolitude/media-downloader/releases) page
2. Download `MediaDownloader.exe`
3. Double-click to run
4. No installation needed!

**Note**: Windows may show a security warning for unsigned executables. Click "More info" â†’ "Run anyway"

### Build Your Own Executable

**Windows:**
```bash
# Double-click build_exe.bat
# OR run manually:
python -m PyInstaller --onefile --name="MediaDownloader" --console downloader.py
```

**macOS/Linux:**
```bash
pip install pyinstaller
pyinstaller --onefile --name="MediaDownloader" --console downloader.py
```

Your executable will be in the `dist` folder.

For detailed build instructions, see [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md)

---

## ðŸ“– Usage

### Basic Usage

```bash
python downloader.py
```

### Step-by-Step Guide

**1. Launch the Application**
   - Run the script or executable
   - The colorful ASCII banner will appear
   - Dependencies are checked automatically

**2. Select Platform**
   ```
   Select platform:
   1. YouTube
   2. SoundCloud
   3. Spotify (Currently Unavailable)
   Enter choice (1-2):
   ```

**3. Enter URL**
   - Paste the full URL of the video or track
   - Example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

**4. Choose Format**
   
   **For YouTube:**
   ```
   Select format:
   1. MP4 (Video)
   2. Audio only
   ```

   **For Video (MP4):**
   ```
   Select quality:
   1. 1080p
   2. 720p
   3. 480p
   ```

   **For Audio:**
   ```
   Select audio format:
   1. MP3 (192kbps) - Most compatible
   2. OPUS (128kbps) - Better quality at lower bitrate
   3. AAC (192kbps) - Apple devices
   4. FLAC - Lossless (large file)
   5. WAV - Uncompressed (very large)
   6. VORBIS (OGG) - Open source
   ```

**5. Wait for Download**
   - Progress will be displayed in real-time
   - Files are saved to the appropriate folder

**6. Download More (Optional)**
   ```
   Download another? (y/n):
   ```

### Advanced Options

**Batch Downloads:**
Run the script and keep selecting 'y' to download multiple files in one session.

**Custom Output Directory:**
Modify the `output_dir` variable in `downloader.py` to change the download location.

**Silent Mode:**
Dependencies are checked silently. The script only shows output during downloads.

---

## ðŸŽµ Audio Formats

### Detailed Format Comparison

| Format | Bitrate | Quality | File Size | Compatibility | Best For |
|--------|---------|---------|-----------|---------------|----------|
| **MP3** | 192 kbps | Good | Medium | â­â­â­â­â­ | General use, all devices |
| **OPUS** | 128 kbps | Excellent | Small | â­â­â­â­ | Modern devices, streaming |
| **AAC** | 192 kbps | Very Good | Medium | â­â­â­â­â­ | Apple devices, iTunes |
| **FLAC** | Lossless | Perfect | Large | â­â­â­ | Audiophiles, archiving |
| **WAV** | Lossless | Perfect | Very Large | â­â­â­â­ | Professional audio work |
| **VORBIS** | Variable | Very Good | Medium | â­â­â­ | Open-source enthusiasts |

### Format Recommendations

- **For everyday listening**: MP3 or AAC
- **For best quality/size ratio**: OPUS
- **For Apple devices**: AAC
- **For archiving**: FLAC
- **For audio editing**: WAV
- **For open-source preference**: VORBIS

---

## ðŸŽ¥ Video Quality Options

| Quality | Resolution | Typical File Size (10 min) | Best For |
|---------|------------|----------------------------|----------|
| **1080p** | 1920x1080 | 200-500 MB | HD displays, archiving |
| **720p** | 1280x720 | 100-250 MB | Most devices, balanced |
| **480p** | 854x480 | 50-100 MB | Mobile devices, saving space |

**Note**: Not all videos have 1080p available. The script will automatically download the best available quality.

---

## ðŸ“ Download Organization

All downloads are automatically organized into format-specific folders:

```
downloads/
â”œâ”€â”€ mp3/          # MP3 audio files
â”œâ”€â”€ opus/         # OPUS audio files
â”œâ”€â”€ aac/          # AAC audio files
â”œâ”€â”€ flac/         # FLAC audio files
â”œâ”€â”€ wav/          # WAV audio files
â”œâ”€â”€ vorbis/       # VORBIS (OGG) audio files
â””â”€â”€ mp4/          # MP4 video files
```

**File Naming:**
Files are automatically named using the video/track title from the platform, with special characters removed for compatibility.

Example: `Rick Astley - Never Gonna Give You Up.mp3`

---

## ðŸŒ Supported Platforms

| Platform | Video | Audio | Status | Notes |
|----------|-------|-------|--------|-------|
| **YouTube** | âœ… | âœ… | Active | Full support, all formats |
| **SoundCloud** | âŒ | âœ… | Active | Audio only |
| **Spotify** | âŒ | âŒ | Unavailable | API rate limits |

### Coming Soon
- Bandcamp support
- Vimeo support
- Direct URL downloads
- Playlist support

---

## ðŸ”§ Technical Details

### Architecture

```
Media Downloader
â”œâ”€â”€ Dependency Manager (Auto-install)
â”œâ”€â”€ Platform Selector (YouTube/SoundCloud)
â”œâ”€â”€ Format Selector (Video/Audio)
â”œâ”€â”€ Download Engine (yt-dlp)
â”œâ”€â”€ Format Converter (FFmpeg)
â””â”€â”€ File Organizer (Auto-sort)
```

### Technologies Used

- **Python 3.7+**: Core language
- **yt-dlp**: Download engine (fork of youtube-dl)
- **FFmpeg**: Audio/video processing
- **colorama**: Cross-platform colored terminal output
- **PyInstaller**: Executable creation

### Performance

- **Download Speed**: Limited by your internet connection
- **Conversion Speed**: Depends on file size and CPU
- **Memory Usage**: ~50-100 MB during operation
- **Disk Usage**: Minimal (downloads excluded)

---

## ðŸ› ï¸ Troubleshooting

### Common Issues and Solutions

#### Issue: "FFmpeg not found"

**Solution:**
- **Windows**: The script auto-installs via winget. If it fails:
  ```bash
  winget install Gyan.FFmpeg
  ```
  Or download from https://ffmpeg.org/download.html

- **macOS**:
  ```bash
  brew install ffmpeg
  ```

- **Linux**:
  ```bash
  sudo apt install ffmpeg  # Debian/Ubuntu
  sudo yum install ffmpeg  # CentOS/RHEL
  ```

#### Issue: "Some formats are missing"

**Cause**: YouTube is forcing SABR streaming or the video doesn't have that format.

**Solution**:
- Try a different quality setting
- Update yt-dlp: `pip install --upgrade yt-dlp`
- Some videos may not have 1080p available

#### Issue: "Download fails with error"

**Solutions**:
1. Check your internet connection
2. Verify the URL is correct and accessible
3. Update yt-dlp: `pip install --upgrade yt-dlp`
4. Try a different video/track
5. Check if the video is region-locked

#### Issue: "Script won't start"

**Solutions**:
1. Verify Python version: `python --version` (must be 3.7+)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Run with admin/sudo if permission errors occur
4. Check antivirus isn't blocking the script

#### Issue: "Executable shows security warning"

**Cause**: Windows SmartScreen for unsigned executables.

**Solution**:
1. Click "More info"
2. Click "Run anyway"
3. Or build from source yourself

#### Issue: "Colors not showing correctly"

**Solution**:
- Windows: Use Windows Terminal or PowerShell (not CMD)
- Update colorama: `pip install --upgrade colorama`
- Some terminals don't support ANSI colors

### Getting Help

If you encounter issues not listed here:

1. Check the [Issues](https://github.com/hiddeninsolitude/media-downloader/issues) page
2. Search for similar problems
3. Create a new issue with:
   - Your OS and Python version
   - Full error message
   - Steps to reproduce
   - What you've already tried

---

## â“ Frequently Asked Questions

**Q: Is this legal?**
A: The tool itself is legal. However, downloading copyrighted content without permission may violate terms of service or copyright laws. Only download content you have the right to download.

**Q: Do I need a YouTube/SoundCloud account?**
A: No, the tool works with public content without requiring login.

**Q: Can I download playlists?**
A: Not in the current version. This feature is planned for a future release.

**Q: Why is Spotify unavailable?**
A: Spotify has strict API rate limits that make reliable downloading difficult without personal API credentials.

**Q: Can I download age-restricted videos?**
A: Not currently. This may be added in a future version.

**Q: How do I update the tool?**
A: Pull the latest changes from GitHub:
```bash
git pull origin main
```

**Q: Can I use this on a server?**
A: Yes, but you'll need to modify the script to remove interactive prompts for automated use.

**Q: Is my data collected?**
A: No. The tool runs entirely locally and doesn't send any data anywhere except to the platforms you're downloading from.

---

## ðŸ¤ Contributing

Contributions are welcome and appreciated! Here's how you can help:

### Ways to Contribute

- ðŸ› **Report Bugs**: Open an issue with details
- ðŸ’¡ **Suggest Features**: Share your ideas in issues
- ðŸ“ **Improve Documentation**: Fix typos, add examples
- ðŸ”§ **Submit Code**: Create pull requests
- â­ **Star the Project**: Show your support!

### Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/media-downloader.git
   ```
3. Create a branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Make your changes
5. Test thoroughly
6. Commit with clear messages:
   ```bash
   git commit -m "Add: feature description"
   ```
7. Push and create a pull request

### Code Style

- Follow PEP 8 guidelines
- Add comments for complex logic
- Update documentation for new features
- Test on multiple platforms if possible

### Pull Request Guidelines

- Describe what your PR does
- Reference related issues
- Include screenshots for UI changes
- Ensure all tests pass
- Keep PRs focused on a single feature/fix

---

## ðŸ“„ License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for full details.

### What This Means

âœ… **You CAN**:
- Use commercially
- Modify the code
- Distribute
- Use privately
- Sublicense

âŒ **You CANNOT**:
- Hold the author liable
- Use the author's name for promotion without permission

ðŸ“‹ **You MUST**:
- Include the original license
- Include copyright notice

---

## ðŸ‘¤ Author

**Created by @hiddeninsolitude**

- Discord: @hiddeninsolitude
- GitHub: [Your GitHub Profile]

### Support the Project

If you find this project useful:
- â­ Star the repository
- ðŸ› Report bugs
- ðŸ’¡ Suggest features
- ðŸ“¢ Share with others
- â˜• [Buy me a coffee](your-link) (optional)

---

## ðŸ™ Acknowledgments

This project wouldn't be possible without these amazing open-source projects:

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - The powerful download engine that makes everything possible
- **[FFmpeg](https://ffmpeg.org/)** - The Swiss Army knife of audio/video processing
- **[colorama](https://github.com/tartley/colorama)** - Making terminals colorful across platforms
- **[PyInstaller](https://www.pyinstaller.org/)** - Creating standalone executables

Special thanks to:
- The Python community for excellent documentation
- All contributors and users who provide feedback
- Open-source developers who make tools like this possible

---

## âš ï¸ Disclaimer

### Important Legal Notice

This tool is provided for **educational and personal use only**. Users are responsible for complying with:

- Copyright laws in their jurisdiction
- Terms of Service of platforms (YouTube, SoundCloud, etc.)
- Fair use guidelines
- Local regulations regarding content downloading

### Responsibility

- **The author is not responsible** for how you use this tool
- **You are solely responsible** for ensuring your use is legal
- **Respect content creators** - consider supporting them through official channels
- **Don't distribute copyrighted content** without permission

### Ethical Use

Please use this tool responsibly:
- âœ… Download your own content
- âœ… Download content you have permission to download
- âœ… Download public domain or Creative Commons content
- âœ… Use for personal backup purposes
- âŒ Don't download copyrighted content without permission
- âŒ Don't redistribute downloaded content
- âŒ Don't use for commercial purposes without proper licensing

### Platform Terms

Be aware that downloading content may violate platform terms of service:
- YouTube: [Terms of Service](https://www.youtube.com/t/terms)
- SoundCloud: [Terms of Use](https://soundcloud.com/terms-of-use)

**Use at your own risk and discretion.**

---

## ðŸ“Š Project Stats

![GitHub stars](https://img.shields.io/github/stars/hiddeninsolitude/media-downloader?style=social)
![GitHub forks](https://img.shields.io/github/forks/hiddeninsolitude/media-downloader?style=social)
![GitHub issues](https://img.shields.io/github/issues/hiddeninsolitude/media-downloader)
![GitHub pull requests](https://img.shields.io/github/issues-pr/hiddeninsolitude/media-downloader)

---

## ðŸ—ºï¸ Roadmap

### Version 1.1 (Planned)
- [ ] Playlist support
- [ ] Batch URL input from file
- [ ] Download history
- [ ] Resume interrupted downloads

### Version 1.2 (Planned)
- [ ] GUI version
- [ ] More platform support (Vimeo, Bandcamp)
- [ ] Custom quality settings
- [ ] Subtitle download

### Version 2.0 (Future)
- [ ] Web interface
- [ ] API for integration
- [ ] Cloud storage integration
- [ ] Mobile app

---

<div align="center">

### â­ If you find this project useful, please consider giving it a star! â­

**Made with â¤ï¸ by @hiddeninsolitude**

[Report Bug](https://github.com/hiddeninsolitude/media-downloader/issues) â€¢ [Request Feature](https://github.com/hiddeninsolitude/media-downloader/issues) â€¢ [Discussions](https://github.com/hiddeninsolitude/media-downloader/discussions)

</div>

