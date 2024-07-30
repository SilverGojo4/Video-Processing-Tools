"""
Module for converting MKV files to MP4 format using FFmpeg.
此模組提供使用 FFmpeg 將 MKV 文件轉換為 MP4 格式
"""

import os

import ffmpeg


def convert_mkv_to_mp4(input_file: str, output_file: str) -> None:
    """
    將 MKV 文件轉換為 MP4 文件

    ## Parameters
    ----------
    - input_file: str, 輸入的 MKV 文件路徑
    - output_file: str, 輸出的 MP4 文件路徑

    ## Raises
    ----------
    - FileNotFoundError: 如果輸入文件不存在
    - ffmpeg.Error: 如果轉換過程中發生錯誤
    - PermissionError: 如果沒有權限訪問輸入文件或輸出文件
    - Exception: 其他未預期的錯誤
    """
    # 檢查輸入文件是否存在
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"MKV file not found: {input_file}")

    try:
        # 使用 ffmpeg 進行轉換
        (
            ffmpeg.input(input_file)
            .output(output_file, vcodec="copy", acodec="copy")
            .run(overwrite_output=True)
        )
        print(f"Successfully converted {input_file} to {output_file}")

    # 處理 ffmpeg 轉換過程中的錯誤
    except ffmpeg.Error as ffmpeg_error:
        print("Conversion Error: Unable to convert the file.")
        print(f"Details: {ffmpeg_error.stderr.decode()}")
        raise

    # 處理權限不足的錯誤
    except PermissionError as perm_error:
        print("Permission Denied: Unable to access the MKV file.")
        print(f"Details: {perm_error}")
        raise

    # 處理其他意外錯誤
    except Exception as error:
        print("Unexpected Error: An unexpected error occurred.")
        print(f"Details: {error}")
        raise
