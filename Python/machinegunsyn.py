import threading
import time
import math

# 设置参数
propeller_speed_rpm = 2400  # 螺旋桨转速，单位：转/分钟
bullet_interval_ms = 50     # 子弹发射间隔，单位：毫秒
propeller_gap_count = 10    # 间隙数量

# 将转速转换为转/秒
propeller_speed_rps = propeller_speed_rpm / 60.0

# 计算每转的时间（秒）
propeller_period = 1.0 / propeller_speed_rps

# 计算每个间隙的角度（度）
gap_angle = 360.0 / propeller_gap_count

# 同步机制
event = threading.Event()
current_angle = 0

def propeller_thread():
    global current_angle
    while True:
        time.sleep(propeller_period / 360.0)  # 每个角度单位时间
        current_angle = (current_angle + 360.0 / propeller_gap_count) % 360.0
        event.set()  # 通知子弹线程螺旋桨已旋转

def gun_thread():
    last_shot_time = time.time()
    while True:
        event.wait()  # 等待螺旋桨线程通知
        event.clear()
        
        # 计算当前时间所对应的角度
        if (current_angle % gap_angle) < (gap_angle / 2):
            if (time.time() - last_shot_time) >= (bullet_interval_ms / 1000.0):
                print(f"Shot fired at {time.time():.2f} seconds")
                last_shot_time = time.time()

# 启动线程
propeller = threading.Thread(target=propeller_thread, daemon=True)
gun = threading.Thread(target=gun_thread, daemon=True)

propeller.start()
gun.start()

# 运行一定时间后退出
time.sleep(10)  # 模拟运行10秒钟
