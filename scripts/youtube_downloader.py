import os 
from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def youtube_downloader():
    # Default download directory
    if os.name == 'nt':  # Windows
        default_download_dir = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:  # macOS/Linux
        default_download_dir = os.path.expanduser('~')

    download_dir = default_download_dir  # Initialize with default

    def select_download_directory():
        nonlocal download_dir
        selected_dir = filedialog.askdirectory(title="Select Download Folder")
        if selected_dir:
            download_dir = selected_dir
            download_path_label.config(text=f"Download Folder: {download_dir}")

    def fetch_video_details():
        try:
            link = url_entry.get()
            yt = YouTube(link)
            yt.check_availability()  # Check for availability
            title_label.config(text=f"Title: {yt.title}", fg="white")
            duration_label.config(text=f"Duration: {yt.length // 60} min {yt.length % 60} sec", fg="white")
            resolution_label.config(
                text=f"Available Resolutions: {', '.join([s.resolution for s in yt.streams.filter(progressive=True, file_extension='mp4') if s.resolution])}",
                fg="white"
            )
            return yt
        except VideoUnavailable:
            messagebox.showerror("Error", "This video is unavailable or restricted.")
            return None
        except Exception as e:
            print(f"Error: {e}")  # For debugging
            messagebox.showerror("Error", "Invalid YouTube URL or connection issue.")
            return None

    def download_mp3():
        yt = fetch_video_details()
        if yt:
            try:
                audio_stream = yt.streams.filter(only_audio=True).first()
                output_path = audio_stream.download(download_dir)
                base, ext = os.path.splitext(output_path)
                mp3_path = base + ".mp3"
                os.rename(output_path, mp3_path)
                messagebox.showinfo("Download Complete", f"Audio saved to: {mp3_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download MP3: {e}")

    def download_mp4():
        yt = fetch_video_details()
        if yt:
            try:
                video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
                video_stream.download(download_dir)
                messagebox.showinfo("Download Complete", f"Video saved to: {download_dir}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download MP4: {e}")

    # Button hover effects
    def on_hover(button, bg_color):
        button.config(bg=bg_color)

    def on_leave(button, bg_color):
        button.config(bg=bg_color)

    # GUI Setup
    root = Tk()
    root.title("[3TH1C4L] YouTube Downloader")
    root.geometry("850x600")  # Increased width and height
    root.configure(bg="#121212")  # Darker black background
    root.resizable(False, False)


    # [3TH1C4L] Label
    logo_label = Label(root, text="[3TH1C4L]", font=("Arial", 14, "bold"), bg="#121212", fg="purple")
    logo_label.pack(pady=5)

    # Heading
    heading = Label(root, text="YouTube Downloader", font=("Arial", 26, "bold"), bg="#121212", fg="#ff004c")  # Red
    heading.pack(pady=20)

    # Input Field for URL
    Label(root, text="Enter YouTube URL:", font=("Arial", 14), bg="#121212", fg="purple").pack(pady=10)
    url_entry = Entry(root, width=70, font=("Arial", 14), bg="#1f1f1f", fg="white", insertbackground="white", relief=FLAT, justify="center")
    url_entry.pack(pady=5)

    # Fetch Details Button
    fetch_btn = Button(root, text="Fetch Video Details", font=("Arial", 14, "bold"), bg="#ff004c", fg="white", relief=FLAT, command=fetch_video_details)
    fetch_btn.pack(pady=15)
    fetch_btn.bind("<Enter>", lambda e: on_hover(fetch_btn, "#cc0033"))
    fetch_btn.bind("<Leave>", lambda e: on_leave(fetch_btn, "#ff004c"))

    # Video Details Labels
    details_frame = Frame(root, bg="#121212")
    details_frame.pack(pady=10)

    title_label = Label(details_frame, text="Title: N/A", font=("Arial", 12), bg="#121212", fg="white")
    title_label.grid(row=0, column=0, sticky=W, padx=10, pady=5)

    duration_label = Label(details_frame, text="Duration: N/A", font=("Arial", 12), bg="#121212", fg="white")
    duration_label.grid(row=1, column=0, sticky=W, padx=10, pady=5)

    resolution_label = Label(details_frame, text="Available Resolutions: N/A", font=("Arial", 12), bg="#121212", fg="white")
    resolution_label.grid(row=2, column=0, sticky=W, padx=10, pady=5)

    # Download Folder Selection
    download_path_label = Label(root, text=f"Download Folder: {default_download_dir}", font=("Arial", 12), bg="#121212", fg="#ff004c")
    download_path_label.pack(pady=10)

    select_folder_btn = Button(root, text="Select Download Folder", font=("Arial", 12), bg="#ff004c", fg="white", relief=FLAT, command=select_download_directory)
    select_folder_btn.pack(pady=5)
    select_folder_btn.bind("<Enter>", lambda e: on_hover(select_folder_btn, "#cc0033"))
    select_folder_btn.bind("<Leave>", lambda e: on_leave(select_folder_btn, "#ff004c"))

    # MP3 and MP4 Download Buttons
    buttons_frame = Frame(root, bg="#121212")
    buttons_frame.pack(pady=20)

    mp3_button = Button(buttons_frame, text="Download as MP3", font=("Arial", 14, "bold"), bg="#8b00ff", fg="white", relief=FLAT, command=download_mp3)
    mp3_button.grid(row=0, column=0, padx=10)  # Position the button in the first column

    mp4_button = Button(buttons_frame, text="Download as MP4", font=("Arial", 14, "bold"), bg="#8b00ff", fg="white", relief=FLAT, command=download_mp4)
    mp4_button.grid(row=0, column=1, padx=10)  # Position the button in the second column




    # Start GUI Loop
    root.mainloop()
