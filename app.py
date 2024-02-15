import os
import streamlit as st
from moviepy.editor import *

def main():
    st.title("Video to MP3 Converter")

    # File uploader for video input
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        temp_file_path = "temp_video_file.mp4"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.getvalue())

        # Display a nice message while processing
        progress_bar = st.progress(0)
        status_text = st.empty()

        try:
            # Load the video file
            video = VideoFileClip(temp_file_path)
            
            # Extract audio from the video
            audio = video.audio
            
            # Save the audio as an MP3 file
            output_file_path = f"output_{uploaded_file.name.split('.')[0]}.mp3"
            audio.write_audiofile(output_file_path)
            
            # Display success message with download link
            status_text.success("Audio extracted successfully!")
            st.audio(output_file_path, format='audio/mp3')
            
            # Close the video file
            video.close()
        except Exception as e:
            status_text.error(f"An error occurred: {e}")
        finally:
            # Delete the temporary file
            os.remove(temp_file_path)

if __name__ == "__main__":
    main()
