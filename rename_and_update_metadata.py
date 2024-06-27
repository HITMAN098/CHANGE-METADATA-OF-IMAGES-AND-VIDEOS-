from PIL import Image
from moviepy.editor import VideoFileClip
import os

def rename_and_update_metadata_image(file_path):
    try:
        # Open image file
        img = Image.open(file_path)

        # Process image (if needed)

        # Update EXIF metadata (if needed)
        # Example: Modify the exif_dict as necessary
        # exif_dict = piexif.load(img.info['exif'])
        # Modify exif_dict as necessary

        # Save the modified image with updated metadata
        img.save(file_path)
        
        print(f"Metadata updated for {os.path.basename(file_path)}")

    except Exception as e:
        print(f"Error processing {os.path.basename(file_path)}: {e}")

def rename_and_update_metadata_video(file_path):
    try:
        # Open video file
        video = VideoFileClip(file_path)

        # Process video (if needed)
        # Example: video.set_duration(10.5)

        # Update video metadata (if needed)
        # Save the modified video with updated metadata
        video.write_videofile(file_path, codec="libx264", audio_codec="aac", preset="ultrafast")
        
        print(f"Metadata updated for {os.path.basename(file_path)}")

    except Exception as e:
        print(f"Error processing {os.path.basename(file_path)}: {e}")

def process_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            rename_and_update_metadata_image(file_path)
        elif filename.lower().endswith(('.mp4', '.mov')):
            rename_and_update_metadata_video(file_path)
        else:
            print(f"Skipping {filename}: Not a supported file format")

if __name__ == "__main__":
    directory_path = "path_to_your_directory"  # Replace with your directory path
    process_files_in_directory(directory_path)
