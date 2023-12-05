import win32process
import win32con
import win32api
import ctypes
import win32gui

Process_All_Access = 0x10FFFF
WindowHandle = win32gui.FindWindow("UnrealWindow","KOFXV  ")
Hid,Pid = win32process.GetWindowThreadProcessId(WindowHandle)
Process = win32api.OpenProcess(Process_All_Access,False,Pid)