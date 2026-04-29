import os
from pathlib import Path

def delete_markdown_files_in_subfolders():
    # 获取脚本所在目录
    script_dir = Path(__file__).resolve().parent

    deleted_count = 0

    # 遍历脚本所在目录下的所有内容
    for root, dirs, files in os.walk(script_dir):
        root_path = Path(root)

        # 跳过脚本所在目录本身，只处理子文件夹
        if root_path == script_dir:
            continue

        for file in files:
            file_path = root_path / file

            # 判断是否为 markdown 文件
            if file_path.suffix.lower() == ".md":
                try:
                    file_path.unlink()
                    print(f"已删除: {file_path}")
                    deleted_count += 1
                except Exception as e:
                    print(f"删除失败: {file_path}，原因: {e}")

    print(f"\n处理完成，共删除 {deleted_count} 个 markdown 文件。")

if __name__ == "__main__":
    delete_markdown_files_in_subfolders()