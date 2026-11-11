import pyautogui
import pydirectinput
import time
import random
import os
import pathlib
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = Path(__file__).resolve().parent
img_1 = BASE_DIR / "shop_button.png" / "dialog_button.png" / "but_button.png"

CONFIDENCE = 0.6
pyautogui.FAILSAFE = False
pydirectinput.PAUSE = 0.05

def ultimate_click(location):
    if not location:
        return False
        
    # центр кнопок
    target_x = int(location.left + location.width / 2)
    target_y = int(location.top + location.height / 2)
    
    safe_x = target_x - 120
    safe_y = target_y - 120
    
    if safe_x < 10: safe_x = 10
    if safe_y < 10: safe_y = 10

    pydirectinput.moveTo(safe_x, safe_y)
    time.sleep(0.2)
    
    current_x, current_y = pyautogui.position()
    distance_x = target_x - current_x
    distance_y = target_y - current_y
    
    steps = max(abs(distance_x), abs(distance_y))
    if steps == 0: steps = 1
    
    step_x = distance_x / steps
    step_y = distance_y / steps
    
    print(f"  > Телепорт в зону. Ползу ({steps} шагов)...")
    
    for _ in range(steps):
        pydirectinput.moveRel(
            int(step_x) if abs(step_x) >= 1 else (1 if step_x > 0 else -1),
            int(step_y) if abs(step_y) >= 1 else (1 if step_y > 0 else -1)
        )
        time.sleep(random.uniform(0.003, 0.01)) 
        
    print("  > На месте. Жду...")
    time.sleep(random.uniform(0.4, 0.7))
    
    print("  > Клик!")
    pydirectinput.mouseDown()
    time.sleep(random.uniform(0.1, 0.2))
    pydirectinput.mouseUp()
    
    time.sleep(1.5) # Ждем после клика
    return True

print("Бот запущен! Нажми Ctrl+C в терминале, чтобы остановить.")
print("У тебя есть 3 секунды, чтобы переключиться в Roblox...")
time.sleep(3)

try:
    while True:
        print("\n--- Новый круг ---")
        
        # 1. Магазин
        print("Ищу кнопку магазина...")
        shop_location = pyautogui.locateOnScreen('shop_button.png', confidence=CONFIDENCE)
        
        if shop_location:
            print("Магазин найден! Кликаю...")
            ultimate_click(shop_location)
            
            print("Жду 3 секунды, пока прогрузится меню...")
            time.sleep(3)
            
            # 2. Диалог
            print("Ищу кнопку диалога...")
            dialog_location = pyautogui.locateOnScreen('dialog_button.png', confidence=CONFIDENCE)
            
            if dialog_location:
                print("Диалог найден! Кликаю...")
                ultimate_click(dialog_location)
                time.sleep(2) # Пауза после клика по диалогу
            else:
                print("❌ Кнопка диалога НЕ НАЙДЕНА на экране.")
            
            # 3. Покупка
            print("Ищу кнопку покупки...")
            buy_location = pyautogui.locateOnScreen('buy_button.png', confidence=CONFIDENCE)
            
            if buy_location:
                while True:
                    time.sleep(1)
                    print("Кнопка покупки найдена! Покупаю...")
                    ultimate_click(buy_location)
            else:
                print("❌ Кнопка покупки НЕ НАЙДЕНА.")
                
            # 4. Выход
            
            
        else:
            print("Кнопка магазина не видна. Жду...")
            
        time.sleep(2)
        
except KeyboardInterrupt:
    print("\nБот остановлен.")