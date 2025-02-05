
import psutil
import platform

class SystemUtils:

     def get_cpu_usage(self):
        return psutil.cpu_percent(interval = 1) #Get CPU %

     def get_memory_usage(self):
         mem = psutil.virtual_memory()
         return mem.percent # Get % used memory

     def get_os_name(self):
        return platform.system() #Get operating system


if __name__ == '__main__':
    system_utils = SystemUtils()
    print("CPU %: ", system_utils.get_cpu_usage())
    print("Memory %: ", system_utils.get_memory_usage())
    print("OS: ", system_utils.get_os_name())