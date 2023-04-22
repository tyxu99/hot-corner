import tkinter as tk
import pyautogui
pyautogui.FAILSAFE = False


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.task_view_opened = False
        self.desktop_returned = False

    def create_widgets(self):
        self.position_label = tk.Label(self, text='鼠标位置：')
        self.position_label.pack(side='left')
        self.x_label = tk.Label(self, text='X: ')
        self.x_label.pack(side='left')
        self.y_label = tk.Label(self, text='Y: ')
        self.y_label.pack(side='left')
        self.size_label = tk.Label(self, text='屏幕尺寸：')
        self.size_label.pack(side='left')
        self.width_label = tk.Label(self, text='宽度: ')
        self.width_label.pack(side='left')
        self.height_label = tk.Label(self, text='高度: ')
        self.height_label.pack(side='left')

    def update_position(self):
        x, y = pyautogui.position()
        self.x_label.config(text='X: {}'.format(x))
        self.y_label.config(text='Y: {}'.format(y))

        if x <= 10 and y >= pyautogui.size().height - 10 and not self.task_view_opened:
            pyautogui.keyDown('win')
            pyautogui.keyDown('tab')
            pyautogui.keyUp('tab')
            pyautogui.keyUp('win')
            self.task_view_opened = True
        elif self.task_view_opened and not (x <= 10 and y >= pyautogui.size().height - 10):
            self.task_view_opened = False
        if x >= pyautogui.size().width - 10 and y >= pyautogui.size().height - 10 and not self.desktop_returned:
            pyautogui.keyDown("win")
            pyautogui.keyDown("d")
            pyautogui.keyUp("d")
            pyautogui.keyUp("win")
            self.desktop_returned = True
        elif self.desktop_returned and (x < pyautogui.size().width - 10 or y < pyautogui.size().height - 10):
            self.desktop_returned = False

        self.after(10, self.update_position)

    def update_size(self):
        width, height = pyautogui.size()
        self.width_label.config(text='宽度: {}'.format(width))
        self.height_label.config(text='高度: {}'.format(height))
        self.after(1000, self.update_size)


root = tk.Tk()
app = App(master=root)
app.update_position()
app.update_size()
app.mainloop()
