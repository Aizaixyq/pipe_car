
import RPi.GPIO as GPIO
import socket
import time
from typing import List

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# 定义输出引脚
IN1 = 19
IN2 = 26
IN3 = 24
IN4 = 23

# 定义使能引脚
ENA = 13
ENB = 22

dir = {"go":[True, True], "back":[False, False], "right":[True, False], "left":[False, True]}

# 设置引脚为输出
pin_arr = [IN1, IN2, IN3, IN4, ENA, ENB];
for pin in pin_arr:
    GPIO.setup(pin, GPIO.OUT)

#创建实例
pwm_ENB = GPIO.PWM(ENB,500)
pwm_ENA = GPIO.PWM(ENA,500)
#pwm启动
pwm_ENA.start(0)
pwm_ENB.start(0)

def move_direction(state_box: List[bool]) -> None:

    Lad1, Lad2, Rad3, Rad4 = True, False, True, False
    if state_box[0]:#左轮是否前进
        Lad1 = False
        Lad2 = True
    if state_box[1]:#右轮是否前进
        Rad3 = False
        Rad4 = True
    GPIO.output(IN1, Lad1)     # 将IN1设置为0
    GPIO.output(IN2, Lad2)      # 将IN2设置为1
    GPIO.output(IN3, Rad3)     # 将IN3设置为0
    GPIO.output(IN4, Rad4)      # 将IN4设置为1
    pwm_ENB.ChangeDutyCycle(20)
    pwm_ENA.ChangeDutyCycle(20)


def stop() -> None:
    pwm_ENB.ChangeDutyCycle(0)
    pwm_ENA.ChangeDutyCycle(0)


def ctrl_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.3.18', 8080))
    server.listen(5)
    sock, addr = server.accept()
    print('Accept new connection from %s:%s...' % addr)

    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        elif data.decode('utf-8') in dir:
            move_direction(dir[data.decode('utf-8')])
        elif data.decode('utf-8') == "stop":
            stop()
    
    sock.send(b"disconnect")
    sock.close()
    print("disconnect")

if __name__ == "__main__":
    ctrl_server();
    GPIO.cleanup() 