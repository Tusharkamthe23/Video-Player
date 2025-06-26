import streamlit as st
from yt_dlp import YoutubeDL
import os
import re
import tempfile


CORRECT_PASSWORD =os.getenv("PASSWORD")
st.set_page_config(page_title="Video Downloader", layout="centered")

# Password Authentication
st.sidebar.title("Authentication")
password = st.sidebar.text_input("Password", type="password")

if password == CORRECT_PASSWORD:
    st.title("Video Downloader & Player")
    st.write("This is only for educational purpose")

    url= st.text_input("Enter  Video URL:")


    def get_video_info(url):
        ydl_opts = {"quiet": True, "skip_download": True}
        with YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)

    def format_filesize(size_bytes):
        if not size_bytes:
            return "Unknown size"
        return f"{round(size_bytes/(1024 * 1024), 1)} MB"

    if url:

        try:
            info = get_video_info(url)
            st.success("✅ Video loaded successfully!")

            
            
            
            st.markdown("---")
            st.subheader("📥 Download Options")
            download_type = st.radio("Choose format:", ["Video", "Audio"])

            formats = info.get("formats", [])
            if download_type == "Video":
                video_streams = [f for f in formats if f.get("vcodec") != "none" and f.get("acodec") != "none" and f.get("ext") == "mp4"]
                video_streams = sorted(video_streams, key=lambda x: x.get("height", 0), reverse=True)
                options = [f"{v.get('format_note', '')} - {v.get('height', '?')}p ({format_filesize(v.get('filesize'))})" for v in video_streams]
            else:
                audio_streams = [f for f in formats if f.get("vcodec") == "none" and f.get("acodec") != "none"]
                audio_streams = sorted(audio_streams, key=lambda x: int(x.get("abr", 0) or 0), reverse=True)
                options = [f"{a.get('abr', 'N/A')}kbps ({format_filesize(a.get('filesize'))})" for a in audio_streams]

            selected_streams = video_streams if download_type == "Video" else audio_streams

            if not selected_streams:
                st.error("❌ No downloadable formats found.")
                st.stop()


            choice = st.selectbox("Choose quality:", options)
            selected_format = selected_streams[options.index(choice)]

            with st.spinner("🔄 Downloading and preparing..."):
                temp_dir = tempfile.mkdtemp()
                ext = selected_format.get("ext", "mp4")
                temp_path = os.path.join(temp_dir, f"preview.{ext}")

                ydl_opts = {
                    'quiet': True,
                    'outtmpl': temp_path,
                    'format': 'best[ext=mp4][vcodec^=avc1][acodec^=mp4a]/best',
                    'http_headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/122.0.0.0 Safari/537.36',
                        'Accept-Language': 'en-US,en;q=0.9',
                    }
                }
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

            st.success("✅ Download complete!")

            st.subheader("🎬 Preview")
            if download_type == "Video":
                st.video(temp_path)
            else:
                st.audio(temp_path)

            with open(temp_path, "rb") as f:

                st.download_button(
                    label="💾 Save This File",
                    data=f,
                    file_name=os.path.basename(temp_path),
                    mime="video/mp4" if download_type == "Video" else "audio/mp4"
                )

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
