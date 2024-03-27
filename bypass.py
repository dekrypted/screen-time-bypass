import customtkinter
import time

import subprocess
import ctypes

subprocess.getoutput("sc stop WpcMonSvc /Y")
subprocess.getoutput("net stop WpcMonSvc /Y")

class ScreenTimeBypass:
    def __init__(self):
        self.root = customtkinter.CTk()
        centerX = self.root.winfo_screenwidth() // 2 - 150
        centerY = self.root.winfo_screenheight() // 2 - 100
        self.root.geometry("300x200+{}+{}".format(centerX, centerY))
        self.root.title("Screen Time Bypass")
        self.root.resizable(False, False)
        self.root.overrideredirect(True)
        self.root.attributes("-alpha", 0.0)

        self.topBar = customtkinter.CTkFrame(self.root, fg_color="gray50", height=5, corner_radius=0)
        self.topBar.pack(fill="x")

        try:
            admin = ctypes.windll.shell32.IsUserAnAdmin()
        except AttributeError:
            admin = False
        
        if admin:
            self.disabledLabel = customtkinter.CTkLabel(self.root, text="Screen Time Disabled", font=("Century Gothic", 20, "bold"))
            self.disabledLabel.pack(pady=30)

            self.enableButton = customtkinter.CTkButton(self.root, text="Enable", font=("Century Gothic", 15), command=self.goAway, fg_color="gray25", hover_color="gray20", height=50, corner_radius=5)
            self.enableButton.pack(pady=20)
        else:
            self.problemLabel = customtkinter.CTkLabel(self.root, text="Run as Admin", font=("Century Gothic", 20, "bold"))
            self.problemLabel.pack(pady=30)

            self.exitButton = customtkinter.CTkButton(self.root, text="Ok", font=("Century Gothic", 15), command=self.goAway, fg_color="gray25", hover_color="gray20", height=50, corner_radius=5)
            self.exitButton.pack(pady=20)

        for i in range(51):
            self.root.attributes("-alpha", i/50)
            self.root.update()
            time.sleep(0.005)
    
    def goAway(self):
        for i in range(51):
            self.root.attributes("-alpha", 1-i/50)
            self.root.update()
            time.sleep(0.005)
        self.root.destroy()

ScreenTimeBypass().root.mainloop()
subprocess.getoutput("sc start WpcMonSvc")
subprocess.getoutput("net start WpcMonSvc")
