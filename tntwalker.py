import time
import minescript as ms
import keyboard

TICK = 0.05  # 1 game tick (50ms)
ms.echo("TNT Walker activated! Press 'Q' to stop.")
ms.execute("gamemode survival") 
while True:
    time.sleep(TICK)
    ms.execute(f"/setblock ~ ~-1 ~ minecraft:tnt")
    if keyboard.is_pressed("q"):
        break
