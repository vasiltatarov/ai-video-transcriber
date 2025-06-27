# 🎬 AI Video Transcriber

> Transform your videos into multilingual text with cutting-edge AI technology

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🎤 **AI-Powered Transcription** - Uses OpenAI's Whisper for state-of-the-art speech-to-text
- 🌐 **Multi-Language Translation** - Supports 12+ languages including Bulgarian, Spanish, French, German, Italian, Russian, and more
- ⚡ **Fast Processing** - Optimized for quick turnaround times
- 📱 **Web-Based Interface** - No downloads required, works on any device
- 📄 **Professional Output** - Clean, formatted transcription files
- 🔒 **Privacy Focused** - Files processed securely, not stored permanently

## 🚀 Live Demo

Try it out: **[AI Video Transcriber](https://your-app-url.streamlit.app)**

## 📸 Screenshots

![Main Interface](screenshots/main-interface.png)
*Clean, intuitive interface for video upload and processing*

![Results View](screenshots/results-view.png)
*Professional results with download and preview options*

## 🛠️ How It Works

1. **Upload** your video file (MP4, AVI, MOV, MKV, etc.)
2. **Select** your target language for translation
3. **Choose** AI model size (balance between speed and accuracy)
4. **Process** - AI extracts audio, transcribes, and translates
5. **Download** your formatted transcription file

## 📋 Supported Formats

### Video Formats
- MP4, AVI, MOV, MKV, WMV, FLV

### Languages
- 🇧🇬 Bulgarian
- 🇪🇸 Spanish  
- 🇫🇷 French
- 🇩🇪 German
- 🇮🇹 Italian
- 🇷🇺 Russian
- 🇬🇷 Greek
- 🇹🇷 Turkish
- 🇵🇹 Portuguese
- 🇳🇱 Dutch
- 🇵🇱 Polish
- 🇨🇿 Czech

### AI Models
- **Tiny** - ⚡ Fastest, good for clear audio
- **Base** - ⚖️ Balanced speed and accuracy (recommended)
- **Small** - 🎯 Good accuracy, moderate speed
- **Medium** - 🔍 High accuracy, slower
- **Large** - 🏆 Best accuracy, slowest

## 🏃‍♂️ Quick Start

### Online Usage
Simply visit the [live app](https://your-app-url.streamlit.app) and start processing videos immediately!

### Local Development

#### Prerequisites
- Python 3.8+
- FFmpeg installed on your system

#### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-video-transcriber.git
cd ai-video-transcriber

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

#### Installing FFmpeg

**Windows:**
```bash
# Using Chocolatey
choco install ffmpeg

# Using Scoop
scoop install ffmpeg
```

**macOS:**
```bash
# Using Homebrew
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

## 📦 Dependencies

- **streamlit** - Web application framework
- **openai-whisper** - AI transcription engine
- **deep-translator** - Translation services
- **torch** - PyTorch for AI models
- **torchaudio** - Audio processing

## 🔧 Configuration

The app works out of the box with default settings. For advanced users:

### Environment Variables
```bash
# Optional: Set custom model cache directory
export WHISPER_CACHE_DIR="/path/to/cache"

# Optional: Set translation API timeout
export TRANSLATION_TIMEOUT=30
```

### Model Selection Guide
- **For podcasts/interviews**: Base or Small model
- **For lectures/presentations**: Small or Medium model  
- **For noisy environments**: Medium or Large model
- **For quick testing**: Tiny model

## 📊 Performance

| Model | Speed | Accuracy | Best For |
|-------|-------|----------|----------|
| Tiny | ~32x realtime | Good | Quick tests, clear audio |
| Base | ~16x realtime | Better | General use, podcasts |
| Small | ~6x realtime | Good+ | Most content |
| Medium | ~2x realtime | High | Professional use |
| Large | ~1x realtime | Highest | Critical accuracy |

*Performance varies based on hardware and audio quality*

## 🚀 Deployment

### Streamlit Community Cloud (Free)

1. Fork this repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy your fork
5. Share your app URL!

### Other Platforms

- **Heroku**: Use the included `Procfile`
- **Railway**: Push to Railway for automatic deployment  
- **Google Cloud Run**: Containerized deployment
- **AWS/Azure**: Various deployment options available

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Run linting
flake8 app.py

# Run type checking
mypy app.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for the incredible Whisper model
- **Google Translate** for translation services
- **Streamlit** for the amazing web framework
- **FFmpeg** for video processing capabilities

## 📞 Support

- 🐛 **Bug Reports**: [Open an issue](https://github.com/yourusername/ai-video-transcriber/issues)
- 💡 **Feature Requests**: [Start a discussion](https://github.com/yourusername/ai-video-transcriber/discussions)
- 📧 **Email**: your-email@example.com
- 💬 **Discord**: [Join our community](https://discord.gg/your-invite)

## 🔄 Changelog

### v1.2.0 (Latest)
- ✨ Added persistent results display
- 🐛 Fixed preview collapsing on download
- 🎨 Improved UI responsiveness
- 📱 Better mobile experience

### v1.1.0
- 🌍 Added 4 new languages
- ⚡ Improved processing speed
- 🔧 Better error handling

### v1.0.0
- 🎉 Initial release
- 🎤 Whisper integration
- 🌐 Multi-language support
- 📱 Web interface

---

<div align="center">

**[⭐ Star this repo](https://github.com/yourusername/ai-video-transcriber)** if you find it useful!

Made with ❤️ by [Your Name](https://github.com/yourusername)

</div>