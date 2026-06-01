import os

MIC_DEVICE_INDEX = os.getenv("SAM_MIC_DEVICE_INDEX")
MIC_DEVICE_INDEX = int(MIC_DEVICE_INDEX) if MIC_DEVICE_INDEX else None

VSCODE_PATH = os.getenv("SAM_VSCODE_PATH", "code")

YOUTUBE_URL = os.getenv ("SAM_YOUTUBE_URL", "https://www.youtube.com/")