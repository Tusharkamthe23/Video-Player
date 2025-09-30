# Video-Player


# 🎬 YouTube Downloader Web App

A Streamlit-based web application that allows users to download videos and audio from YouTube URLs. It provides a user-friendly interface for entering a URL, selecting the desired download quality, and initiating the download process. The application also includes basic password authentication for security. This project simplifies the process of downloading YouTube content for offline use or archival purposes.

🚀 **Key Features**

*   **Password Protection:** Secure the application with a password to restrict access.
*   **URL Input:** Easily input YouTube video URLs through a simple text field.
*   **Video Information Extraction:** Retrieve video metadata, including available formats, resolutions, and file sizes, using `yt-dlp`.
*   **Format Selection:** Choose between various video and audio formats and quality options. Formats are dynamically filtered based on user preference (video or audio). Video formats are sorted by height, and audio formats by bitrate for easy selection.
*   **Download Initiation:** Download the selected video or audio stream directly from the web interface.
*   **User-Friendly Interface:** A clean and intuitive interface built with Streamlit components.
*   **Error Handling:** Robust error handling to gracefully manage potential issues during video information extraction and download processes.
*   **Temporary File Management:** Utilizes temporary files for downloads, ensuring clean and efficient resource management.
*   **Download Button:** Provides a direct download link to the user upon successful download using Streamlit's `st.download_button`.

🛠️ **Tech Stack**

*   **Frontend:**
    *   `streamlit`: Web application framework for building the user interface.
*   **Backend:**
    *   `Python`: Core programming language.
    *   `yt-dlp`: YouTube download library.
*   **Other:**
    *   `os`: For accessing environment variables (password).
    *   `re`: For regular expressions (used by `yt-dlp`).
    *   `tempfile`: For creating temporary directories.

📦 **Getting Started**

### Prerequisites

*   Python 3.6+
*   pip package installer

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install streamlit yt-dlp
    ```

4.  Set the password as an environment variable:

    ```bash
    export PASSWORD="your_secret_password" # On Linux/macOS
    # OR
    set PASSWORD="your_secret_password"  # On Windows
    ```

    **Note:** Replace `"your_secret_password"` with your desired password.

### Running Locally

1.  Navigate to the project directory in your terminal.
2.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

3.  Open your web browser and go to the address displayed in the terminal (usually `http://localhost:8501`).

💻 **Usage**

1.  Enter the password in the sidebar to access the application.
2.  Paste the YouTube video URL into the provided text input field.
3.  Select the desired video or audio format and quality from the options.
4.  Click the "Download" button.
5.  Wait for the download to complete. A download link will appear.
6.  Click the download link to save the file to your computer.

📂 **Project Structure**

```
.
├── app.py           # Main Streamlit application file
├── README.md        # Project documentation
└── venv/            # Virtual environment directory (if created)
```

📸 **Screenshots**
<img width="1905" height="798" alt="image" src="https://github.com/user-attachments/assets/768c5906-dbe9-4838-923b-49c6631d8ef3" />



🤝 **Contributing**

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Push your changes to your fork.
5.  Submit a pull request.

📝 **License**

This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for details.

📬 **Contact**

If you have any questions or suggestions, feel free to contact me at [tusharkamthe@gamil.com](mailto:tusharkamthe@gamil.com.com).

💖 **Thanks Message**

Thank you for checking out this project! I hope it's helpful. Your feedback and contributions are greatly appreciated.

This is written byTushar Kamthe
