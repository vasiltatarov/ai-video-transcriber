import streamlit as st
import whisper
from deep_translator import GoogleTranslator
import tempfile
import os
from datetime import datetime
import subprocess
import time

# Page config
st.set_page_config(
    page_title="🎬 AI Video Transcriber",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .feature-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        color: black;
    }
    .success-box {
        background: #d4edda;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'processing' not in st.session_state:
    st.session_state.processing = False
if 'whisper_model' not in st.session_state:
    st.session_state.whisper_model = None
if 'model_name' not in st.session_state:
    st.session_state.model_name = None
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'results_data' not in st.session_state:
    st.session_state.results_data = None

# Language options
LANGUAGES = {
    "Bulgarian": "bg",
    "Spanish": "es", 
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Russian": "ru",
    "Greek": "el",
    "Turkish": "tr",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Polish": "pl",
    "Czech": "cs"
}

FLAG_MAP = {
    "bg": "🇧🇬", "es": "🇪🇸", "fr": "🇫🇷", "de": "🇩🇪", 
    "it": "🇮🇹", "ru": "🇷🇺", "el": "🇬🇷", "tr": "🇹🇷",
    "pt": "🇵🇹", "nl": "🇳🇱", "pl": "🇵🇱", "cs": "🇨🇿"
}

def extract_audio_from_video(video_path, audio_path):
    """Extract audio from video using ffmpeg"""
    try:
        command = [
            "ffmpeg", "-i", video_path,
            "-ar", "16000", "-ac", "1", 
            "-c:a", "pcm_s16le",
            audio_path, "-y"
        ]
        
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        st.error(f"❌ Error extracting audio: {e.stderr}")
        return False
    except FileNotFoundError:
        st.error("❌ ffmpeg not found. This app requires ffmpeg to be installed on the server.")
        return False

@st.cache_resource
def load_whisper_model(model_name):
    """Load Whisper model with caching"""
    return whisper.load_model(model_name)

def transcribe_audio(audio_path, model_name):
    """Transcribe audio using Whisper"""
    try:
        model = load_whisper_model(model_name)
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        st.error(f"❌ Transcription error: {str(e)}")
        return None

def translate_text(text, target_lang_code, progress_bar=None):
    """Translate text using Google Translator"""
    try:
        # Split text into chunks for long content
        max_chunk_size = 4500
        chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
        
        translated_chunks = []
        translator = GoogleTranslator(source='auto', target=target_lang_code)
        
        for i, chunk in enumerate(chunks):
            if progress_bar:
                progress_bar.progress((i + 1) / len(chunks), f"Translating chunk {i+1}/{len(chunks)}...")
            
            try:
                translated = translator.translate(chunk)
                translated_chunks.append(translated)
                time.sleep(0.1)  # Be nice to the API
            except Exception as e:
                # Retry once
                time.sleep(1)
                translated = translator.translate(chunk)
                translated_chunks.append(translated)
        
        return " ".join(translated_chunks)
    except Exception as e:
        st.error(f"❌ Translation error: {str(e)}")
        return None

def create_output_file(english_text, translated_text, filename, target_language, model_name):
    """Create formatted output file"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    
    target_lang_code = LANGUAGES[target_language]
    flag = FLAG_MAP.get(target_lang_code, "🌍")
    
    content = f"""{'='*50}
🎬 AI VIDEO TRANSCRIPTION & TRANSLATION
{'='*50}

📁 Original file: {filename}
⏰ Processed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🤖 Model used: {model_name}
📊 Characters - English: {len(english_text)} | Translated: {len(translated_text)}

--- 🇬🇧 ENGLISH TRANSCRIPTION ---

{english_text}

--- {flag} {target_language.upper()} TRANSLATION ---

{translated_text}

---
Generated by AI Video Transcriber 🎬
"""
    return content

# Main UI
st.markdown("""
<div class="main-header">
    <h1>🎬 AI Video Transcriber</h1>
    <p>Transform your videos into text in multiple languages using AI</p>
</div>
""", unsafe_allow_html=True)

# Feature highlights
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
        <h3>🎤 AI Transcription</h3>
        <p>State-of-the-art Whisper AI converts speech to text with high accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <h3>🌐 Multi-Language</h3>
        <p>Translate to 12+ languages including Bulgarian, Spanish, French & more</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
        <h3>⚡ Fast Processing</h3>
        <p>Upload your video and get results in minutes, not hours</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Main interface
st.header("🚀 Process Your Video")

# File upload
uploaded_file = st.file_uploader(
    "Choose a video file",
    type=['mp4', 'avi', 'mov', 'mkv', 'wmv', 'flv'],
    help="Upload your video file (max 200MB recommended)"
)

if uploaded_file is not None:
    # Display file info
    file_size = len(uploaded_file.getvalue()) / (1024 * 1024)  # MB
    st.success(f"✅ File uploaded: **{uploaded_file.name}** ({file_size:.1f} MB)")
    
    # Settings
    col1, col2 = st.columns(2)
    
    with col1:
        target_language = st.selectbox(
            "🌐 Translate to:",
            options=list(LANGUAGES.keys()),
            index=0,
            help="Select the target language for translation"
        )
    
    with col2:
        model_size = st.selectbox(
            "🤖 AI Model:",
            options=["tiny", "base", "small", "medium", "large"],
            index=1,
            help="Larger models are more accurate but slower"
        )
    
    # Model info
    model_info = {
        "tiny": "⚡ Fastest, good for clear audio",
        "base": "⚖️ Balanced speed and accuracy", 
        "small": "🎯 Good accuracy, moderate speed",
        "medium": "🔍 High accuracy, slower",
        "large": "🏆 Best accuracy, slowest"
    }
    st.info(f"Selected model: **{model_size}** - {model_info[model_size]}")
    
    # Process button
    if st.button("🚀 Start Processing", type="primary", disabled=st.session_state.processing):
        if not st.session_state.processing:
            st.session_state.processing = True
            
            # Create progress indicators
            progress_bar = st.progress(0, "Starting processing...")
            status_text = st.empty()
            
            try:
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_video:
                    tmp_video.write(uploaded_file.getvalue())
                    video_path = tmp_video.name
                
                # Extract audio
                status_text.info("🎵 Extracting audio from video...")
                progress_bar.progress(0.2, "Extracting audio...")
                
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_audio:
                    audio_path = tmp_audio.name
                
                if extract_audio_from_video(video_path, audio_path):
                    # Transcribe
                    status_text.info("🎤 Transcribing audio with AI...")
                    progress_bar.progress(0.4, "AI transcription in progress...")
                    
                    english_text = transcribe_audio(audio_path, model_size)
                    
                    if english_text and english_text.strip():
                        # Translate
                        status_text.info("🌐 Translating text...")
                        progress_bar.progress(0.7, "Translating text...")
                        
                        translated_text = translate_text(
                            english_text, 
                            LANGUAGES[target_language],
                            progress_bar
                        )
                        
                        if translated_text:
                            # Generate output
                            progress_bar.progress(0.9, "Finalizing results...")
                            
                            output_content = create_output_file(
                                english_text, translated_text, 
                                uploaded_file.name, target_language, model_size
                            )
                            
                            progress_bar.progress(1.0, "✅ Complete!")
                            status_text.success("🎉 Processing completed successfully!")
                            
                            # Store results in session state
                            st.session_state.show_results = True
                            st.session_state.results_data = {
                                'english_text': english_text,
                                'translated_text': translated_text,
                                'output_content': output_content,
                                'filename': uploaded_file.name,
                                'target_language': target_language,
                                'flag': FLAG_MAP.get(LANGUAGES[target_language], "🌍")
                            }
                    
                    else:
                        st.error("❌ No speech detected in the video. Please try with a different file.")
                
                # Cleanup
                try:
                    os.unlink(video_path)
                    os.unlink(audio_path)
                except:
                    pass
                    
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
            
            finally:
                st.session_state.processing = False

# Display results if available (outside the processing block)
if st.session_state.show_results and st.session_state.results_data:
    results = st.session_state.results_data
    
    st.markdown("---")
    st.header("📊 Results")
    
    # Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🇬🇧 English Characters", len(results['english_text']))
    with col2:
        st.metric(f"{results['flag']} Translated Characters", len(results['translated_text']))
    with col3:
        st.metric("⏱️ Processing Time", "Complete")
    
    # Download button
    st.download_button(
        label="📥 Download Transcription",
        data=results['output_content'],
        file_name=f"{results['filename'].split('.')[0]}_transcription_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
        mime="text/plain",
        key="download_results"
    )
    
    # Preview with session state to keep it open
    with st.expander("👁️ Preview Results", expanded=True):
        st.subheader("🇬🇧 English Transcription")
        st.text_area("", results['english_text'], height=150, key="english_preview_persistent")
        
        st.subheader(f"{results['flag']} {results['target_language']} Translation")
        st.text_area("", results['translated_text'], height=150, key="translated_preview_persistent")
    
    # Clear results button
    if st.button("🔄 Process New Video", type="secondary"):
        st.session_state.show_results = False
        st.session_state.results_data = None
        st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>🎬 <strong>AI Video Transcriber</strong> | Powered by Whisper AI & Google Translate</p>
    <p>Transform your videos into multilingual text with cutting-edge AI</p>
</div>
""", unsafe_allow_html=True)

# Sidebar info
with st.sidebar:
    st.header("ℹ️ How It Works")
    st.markdown("""
    1. **Upload** your video file
    2. **Choose** target language
    3. **Select** AI model size
    4. **Process** with AI
    5. **Download** results
    """)
    
    st.header("🎯 Supported Formats")
    st.markdown("""
    - **Video**: MP4, AVI, MOV, MKV, WMV, FLV
    - **Languages**: 12+ including Bulgarian, Spanish, French, German, Italian, Russian
    - **Models**: Tiny to Large (accuracy vs speed)
    """)
    
    st.header("💡 Tips")
    st.markdown("""
    - **Clear audio** = better results
    - **Shorter videos** process faster
    - **Base model** good for most uses
    - **Large model** for best accuracy
    """)
