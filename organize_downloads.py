import os
import shutil
from pathlib import Path

# 配置区（用户可自定义）
DOWNLOAD_PATH = "E:\\程序员客栈\\text\\Downloads"  # 需替换为实际路径
FILE_TYPES = {
    "图片": [".jpg", ".png", ".gif", ".webp"],
    "文档": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
    "压缩包": [".zip", ".rar", ".7z"],
    "安装程序": [".exe", ".msi", ".dmg"],
    "音视频": [".mp3", ".mp4", ".avi", ".mov"]
}


def organize_downloads():
    """自动整理下载文件夹的核心函数"""
    # 创建分类文件夹（如果不存在）
    for folder_name in FILE_TYPES.keys():
        (Path(DOWNLOAD_PATH) / folder_name).mkdir(exist_ok=True)

    # 遍历下载文件夹中的所有文件
    for file_path in Path(DOWNLOAD_PATH).iterdir():
        # 跳过目录和隐藏文件
        if file_path.is_dir() or file_path.name.startswith('.'):
            continue

        # 按扩展名分类
        target_folder = None
        for category, extensions in FILE_TYPES.items():
            if file_path.suffix.lower() in extensions:
                target_folder = Path(DOWNLOAD_PATH) / category
                break

        # 移动文件到目标文件夹
        if target_folder:
            try:
                shutil.move(str(file_path), str(target_folder / file_path.name))
                print(f"✅ 已移动: {file_path.name} -> {target_folder.name}/")
            except Exception as e:
                print(f"❌ 移动失败: {file_path.name} | 错误: {e}")


if __name__ == "__main__":
    print("====== 开始整理下载文件夹 ======")
    organize_downloads()
    print("====== 整理完成！ ======")
