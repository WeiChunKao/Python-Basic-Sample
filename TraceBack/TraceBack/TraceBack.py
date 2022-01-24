import sys
import traceback
import os
try:
    a=1/0
except Exception as e:
   error_class = e.__class__.__name__ #取得錯誤類型
   detail = e.args[0] #取得詳細內容
   cl, exc, tb = sys.exc_info() #取得Call Stack
   lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
   fileName = lastCallStack[0] #取得發生的檔案名稱
   lineNum = lastCallStack[1] #取得發生的行號
   funcName = lastCallStack[2] #取得發生的函數名稱
   print("File:[{0}] , Line:{1} , in {2}:[{3}] {4}".format(fileName, lineNum, funcName, error_class, detail)) 
os.system("pause")