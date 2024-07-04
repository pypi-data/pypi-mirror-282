# 一些功能函数
import os
from loguru import logger


def check_and_create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logger.info(f"Folder '{folder_path}' created.")
    else:
        logger.info(f"Folder '{folder_path}' already exists.")


if __name__ == '__main__':
    # 示例文件夹路径
    folder_path = "example_folder"
    check_and_create_folder(folder_path)
