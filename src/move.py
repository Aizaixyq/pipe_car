
import RPi.GPIO as GPIO
import socket
import time

GPIO.setmode(GPIO.BCM)

# 定义输出引脚
IN1 = 19
IN2 = 26
IN3 = 24
IN4 = 23

# 定义使能引脚
ENA = 13
ENB = 22

# 设置引脚为输出
pin_arr = [IN1, IN2, IN3, IN4, ENA, ENB];
for pin in pin_arr:
    GPIO.setup(pin, GPIO.OUT)

pwm_ENB = GPIO.PWM(ENB,500)
pwm_ENA = GPIO.PWM(ENA,500)
#pwm启动
pwm_ENA.start(0)
pwm_ENB.start(0)

def forward():
    GPIO.output(IN1, False)     # 将IN1设置为0
    GPIO.output(IN2, True)      # 将IN2设置为1
    #GPIO.output(ENA, True)      # 将ENA设置为1，启动A通道电机
    GPIO.output(IN3, False)     # 将IN3设置为0
    GPIO.output(IN4, True)      # 将IN4设置为1
    #GPIO.output(ENB, True)      # 将ENB设置为1，启动B通道电机
    pwm_ENB.ChangeDutyCycle(20)
    pwm_ENA.ChangeDutyCycle(20)


def stop():
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
        elif data.decode('utf-8') == 'go':
            forward()
        elif data.decode('utf-8') == 'stop':
            stop()
    sock.send(b"disconnect")
    sock.close()
    print("disconnect")

if __name__ == "__main__":
    ctrl_server();
    GPIO.cleanup() 