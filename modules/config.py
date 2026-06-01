import os

MIC_DEVICE_INDEX = int(os.getenv("SAM_MIC_DEVICE_INDEX", "1"))

# App paths / URLs
VSCODE_PATH = os.getenv("SAM_VSCODE_PATH", r"D:\Microsoft VS Code\Code.exe")
YOUTUBE_URL = os.getenv("SAM_YOUTUBE_URL", "https://www.youtube.com/")