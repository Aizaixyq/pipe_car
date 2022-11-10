
import RPi.GPIO as GPIO
import socket

# 定义输出引脚
IN1 = 19
IN2 = 26
IN3 = 24
IN4 = 23

# 定义使能引脚
ENA = 13
ENB = 22

# 设置引脚为输出
GPIO.setup([IN1, IN2, IN3, IN4, ENA, ENB], GPIO.OUT)

pwm_ENB = GPIO.PWM(ENB,2000)
pwm_ENA = GPIO.PWM(ENA,2000)
#pwm启动
pwm_ENA.start(0)
pwm_ENB.start(0)

def forward(){
    pwm_ENB.ChangeDutyCycle(20)
    pwm_ENA.ChangeDutyCycle(20)
}

def stop(){
    pwm_ENA.stop();
    pwm_ENB.stop();
}

def ctrl_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.3.18', 8080))
    server.listen(5)
    sock, addr = server.accept()
    print('Accept new connection from %s:%s...' % addr)
    sock.send('Accept!')
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        elif data.decode('utf-8') == 'go':
            forward()
        elif data.decode('utf-8') == 'stop':
            stop()
    sock.close()
    print("disconnect")

if __name__ == "__main__":
    ctrl_server();