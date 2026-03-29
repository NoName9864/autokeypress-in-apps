import keyboard
import time
import win32gui
from win10toast import ToastNotifier

appWorking = True
toaster = ToastNotifier()
appName = "Antimatter Dimensions"  # Переменная с названием окна приложения
keyToPress = 'm'  # Переменная с названием кнопки для нажатия


# Функция для вывода уведомления при изменения состояния работы приложения
def show_toast(message):
    toaster.show_toast(
        "Уведомление",
        message,
        duration=1,
        threaded=True
    )


# Функция для проверки текущего активного окна, а также нажатия кнопки, при соответствии
def checkwindow():
    hwnd = win32gui.GetForegroundWindow()
    active_window_title = win32gui.GetWindowText(hwnd)
    if active_window_title == appName:
        keyboard.press(keyToPress)


# Цикл для проверок при запущенном приложении
try:
    while True:
        # Проверка состояния работы программы (пауза)
        if keyboard.is_pressed('insert'):
            appWorking = not appWorking
            show_toast("Состояние изменено: " + ("Включено" if appWorking else "Выключено"))
            time.sleep(0.5)

        if appWorking:
            checkwindow()

        time.sleep(0.01)

except KeyboardInterrupt:
    print("Программа завершена")
