import os
import sys
import shutil
import subprocess

def build_app():
    print("開始打包距離量測應用程序...")
    
    # 檢查必要文件
    if not os.path.exists("image_distance_measurement.py"):
        print("錯誤：找不到主程序文件 image_distance_measurement.py")
        return False
    
    # 檢查作者頭像
    if not os.path.exists("author_avatar.png"):
        print("警告：找不到作者頭像文件 author_avatar.png")
        print("應用程序將無法顯示作者頭像")
    
    # 檢查應用程序圖標
    if not os.path.exists("app_icon.ico"):
        print("警告：找不到應用程序圖標 app_icon.ico")
        print("將使用默認圖標")
        icon_param = []
    else:
        # 修改圖標參數格式
        icon_param = ["--icon", "app_icon.ico"]
    
    # 安裝必要的依賴
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller", "pillow"])
    except subprocess.CalledProcessError:
        print("錯誤：安裝依賴失敗")
        return False
    
    # 使用 PyInstaller 打包
    try:
        cmd = [
            sys.executable, 
            "-m", 
            "PyInstaller", 
            "--name=距離量測工具", 
            "--windowed", 
            "--onefile", 
            "--add-data=author_avatar.png;."
        ]
        
        # 添加圖標參數（如果存在）
        cmd.extend(icon_param)
        
        # 添加主程序
        cmd.append("image_distance_measurement.py")
        
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        print("錯誤：打包失敗")
        return False
    
    print("打包完成！")
    print("可執行文件位於 dist/距離量測工具.exe")
    return True

if __name__ == "__main__":
    build_app()