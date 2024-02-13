
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_rtu as modbus_rtu
import serial
from threading import Thread
class ModbusMaster:
    def __init__(self, port='/dev/ttyAMA2', baudrate=19200, timeout=1.0):
        # Инициализация последовательного порта
        self.master = modbus_rtu.RtuMaster(
            serial.Serial(port=port, baudrate=baudrate, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        self.master.set_timeout(timeout)
        self.master.set_verbose(True)
        self.slaves = [1, 2, 3, 4, 5]  # ID slave устройств

    def send_data(self, slave_id, address, data):
        # Отправка данных одному устройству
        try:
            self.master.execute(slave_id, cst.WRITE_MULTIPLE_REGISTERS, address, output_value=data)
        except modbus_tk.modbus.ModbusError as e:
            print(f"Modbus error: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def read_data(self, slave_id, address, size):
        # Чтение данных с одного устройства
        try:
            return self.master.execute(slave_id, cst.READ_HOLDING_REGISTERS, address, size)
        except modbus_tk.modbus.ModbusError as e:
            print(f"Modbus error: {str(e)}")
            return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    def query_all(self):
        # Опрос всех устройств
        threads = []
        for slave in self.slaves:
            t = Thread(target=self.query_slave, args=(slave,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

    def query_slave(self, slave_id):
        # Запрос к конкретному slave. Здесь можно добавить логику обработки данных
        # Например, чтение с адреса 0, размером 10 регистров
        data = self.read_data(slave_id, 0, 6)
        #if data:
          #  print(f"Data from slave {slave_id}: {data}")
            # Здесь можно добавить отправку данных в другие классы или методы

if __name__ == "__main__":
    master = ModbusMaster()  # Укажите правильный COM-порт
    master.query_slave(1)