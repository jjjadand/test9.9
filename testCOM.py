import serial
import time
import json

def configure_serial(port, baudrate):
    """配置串口"""
    ser = serial.Serial(port, baudrate, timeout=1)
    return ser

def send_data(ser, data):
    """发送数据到串口"""
    if isinstance(data, dict):
        data = json.dumps(data)  # 将字典转换为 JSON 字符串
    ser.write(data.encode('utf-8'))
    print(f"发送数据: {data}")

def read_data(ser):
    """从串口读取数据"""
    time.sleep(1)  # 等待数据返回
    if ser.in_waiting > 0:
        response = ser.read(ser.in_waiting).decode('utf-8')
        print(f"接收数据: {response}")
        return response
    else:
        print("没有接收到数据")
        return None

def main():
    port = '/dev/ttyTHS0'  # 替换为你的串口设备
    baudrate = 256000      # 替换为你的波特率

    # 配置串口
    ser = configure_serial(port, baudrate)

    try:
        # 测试数据，包含不同类型
        test_data = [
            "Hello, World!",               # 字符串
            str(42),                        # 整数
            "0x1A",                         # 十六进制字符串
            str(3.14159),                  # 浮点数
            {"key": "value", "num": 123},  # 字典（JSON格式）
            bytes([0x01, 0x02, 0x03]),     # 字节数据
        ]
        
        for data in test_data:
            send_data(ser, data)
            read_data(ser)

    finally:
        ser.close()
        print("串口已关闭")

if __name__ == "__main__":
    main()

