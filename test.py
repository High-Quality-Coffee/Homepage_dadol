# import psutil
# import GPUtil

# # Get GPU information
# gpus = GPUtil.getGPUs()

# # Get CPU information
# cpu_count = psutil.cpu_count(logical=True)  # Logical cores
# cpu_freq = psutil.cpu_freq()  # CPU frequency in MHz

# # Get RAM information
# ram = psutil.virtual_memory()

# print(f"CPU Count: {cpu_count}")
# print(f"CPU Frequency: {cpu_freq.current} MHz")
# print(f"Total RAM: {ram.total / (1024 ** 3):.2f} GB")

# for gpu in gpus:
#     print(f"GPU Name: {gpu.name}")
#     print(f"GPU Load: {gpu.load * 100:.1f}%")
#     print(f"GPU Memory Free: {gpu.memoryFree:.1f}MB")
#     print(f"GPU Memory Total: {gpu.memoryTotal:.1f}MB")
#     print(f"GPU Temperature: {gpu.temperature} °C")


import wmi
import GPUtil

c = wmi.WMI()
for cpu in c.Win32_Processor():
    print(f"CPU 모델명: {cpu.Name}")
    print(f"장치 ID: {cpu.DeviceID}")

for memory in c.Win32_PhysicalMemory():
    print(f"RAM 모델명: {memory.Manufacturer}")
    print(f"용량: {int(memory.Capacity) / (1024**3)} GB")
    print(f"장치 ID: {memory.DeviceLocator}")

gpus = GPUtil.getGPUs()
for gpu in gpus:
    print(f"GPU 모델명: {gpu.name}")
    print(f"장치 ID: {gpu.id}")

