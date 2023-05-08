import ctypes
import os
import sys
import time

logo = '''
=========================================================================
=     ____  __           __      ________           __       _       __ =
=    / __ )/ /___ ______/ /__   / ____/ /___ ______/ /_     | |     / / =
=   / __  / / __ `/ ___/ //_/  / /_  / / __ `/ ___/ __ \    | | /| / /  =
=  / /_/ / / /_/ / /__/ ,<    / __/ / / /_/ (__  ) / / /    | |/ |/ /   =
= /_____/_/\__,_/\___/_/|_|  /_/   /_/\__,_/____/_/ /_/     |__/|__/    =
=========================================================================
   '''


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def cleanSystem():
    print("正在清理系统垃圾文件...")
    os.system("del /f /s /q %userprofile%\\AppData\\Local\\Temp\\*.*")
    os.system("del /f /s /q %userprofile%\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\*.*")
    os.system("del /f /s /q %windir%\\Offline Web Pages\\*.*")
    os.system("del /f /s /q %userprofile%\\AppData\\Local\\Steam\\htmlcache\\*.*")
    os.system("del /f /s /q %systemdrive%\\*.old")
    os.system("del /f /s /q %systemdrive%\\*.tmp")
    os.system("del /f /s /q %systemdrive%\\*._mp")
    os.system("del /f /s /q %systemdrive%\\*.log")
    os.system("del /f /s /q %systemdrive%\\*.gid")
    os.system("del /f /s /q %systemdrive%\\*.chk")
    os.system("del /f /s /q %windir%\\SoftwareDistribution\\download\\*.*")
    os.system("del /f /s /q %windir%\\Prefetch\\*.*")
    os.system("del /f /s /q %userprofile%\\AppData\\Local\\Microsoft\\Windows\\INetCookies\\*.*")
    os.system("del /f /s /q %userprofile%\\AppData\\Local\\Microsoft\\Windows\\INetCookies\\Low\\*.*")
    print("系统垃圾清理完成！\n")
    os.system("pause")
    os.system("cls")


def cleanChrome():
    print("正在清理谷歌浏览器垃圾文件...")
    # os.system("del /f /s /q %userprofile%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache\\*.*")
    # os.system("del /f /s /q %userprofile%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Code Cache\\*.*")
    # os.system("del /f /s /q %userprofile%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\GPUCache\\*.*")
    # os.system("del /f /s /q %userprofile%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Media Cache\\*.*")
    # os.system(
    #     "del /f /s /q %userprofile%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Service Worker\\CacheStorage\\*.*")
    # os.system(
    #     "del /f /s /q %userprofile%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Service Worker\\ScriptCache\\*.*")
    time.sleep(3)
    print("谷歌浏览器垃圾清理完成！\n")
    os.system("pause")
    os.system("cls")


def cleanEdge():
    print("正在清理Edge浏览器垃圾文件...")
    os.system("del /f /s /q %userprofile%\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\*.*")
    os.system(
        "del /f /s /q %userprofile%\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AC\\INetCache\\*.*")
    print("Edge浏览器垃圾清理完成！\n")
    os.system("pause")
    os.system("cls")


def cleanTencent():
    print("正在清理腾讯垃圾......\n")
    print("3秒后将关闭腾讯相关进程...\n")
    time.sleep(3)
    os.system("TASKKILL /f /IM \"Tencent TenioDL for Game.exe\"")
    os.system("TASKKILL /f /IM \"QQMicroGameBoxTray.exe\"")
    os.system("TASKKILL /f /IM \"QQMicroGameBoxService.exe\"")
    os.system("del /f /s /q %userprofile%\\AppData\\Roaming\\Tencent\\QQMGBDownload\\*.*")
    os.system("del /f /s /q %userprofile%\\AppData\\Local\\Tencent\\Cross\\*.*")
    os.system("del /f /s /q %userprofile%\\AppData\\Roaming\\Tencent\\QQMicroGameBox\\*.*")
    os.system("del /f /s /q %userprofile%\\AppData\\Roaming\\Tencent\\QQMiniGameBox\\*.*")
    os.system("del /f /s /q %userprofile%\\AppData\\Roaming\\Tencent\\QQMiniDL\\*.*")
    os.system("del /f /s /q %userprofile%\\AppData\\Roaming\\Tencent\\游戏人生cross\\*.*")
    os.system("del /f /s /q %userprofile%\\AppData\\Local\\Tencent\\QQPet\\*.*")
    os.system("del /f /s /q %systemdrive%\\Program Files (x86)\\Tencent\\QQMicroGameBoxService\\*.*")
    os.system("del /f /s /q %userprofile%\\Roaming\\Tencent\\Logs\\*.*")
    os.system("del /f /s /q %userprofile%\\AppData\\Roaming\\Tencent\\QQGAMETempest\\Download\\*.*")
    os.system("del /f /s /q %userprofile%\\AppData\\Roaming\\Tencent\\QQ\\Temp\\*.*")
    print("腾讯垃圾清理完成！\n")
    os.system("pause")
    os.system("cls")


def main():
    print(logo)
    print("1.清理系统垃圾")
    print("2.清理谷歌浏览器垃圾")
    print("3.清理Edge浏览器垃圾")
    print("4.清理腾讯垃圾")
    print("5.我全都要！\n")
    print("请输入您要清理的垃圾编号：")
    choice = input()
    if choice == "1":
        cleanSystem()
    elif choice == "2":
        cleanChrome()
    elif choice == "3":
        cleanEdge()
    elif choice == "4":
        cleanTencent()
    elif choice == "5":
        cleanSystem()
        cleanChrome()
        cleanEdge()
        cleanTencent()
    else:
        print("输入错误！")
        os.system("pause")
        os.system("cls")


if __name__ == '__main__':
    if is_admin():
        main()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
