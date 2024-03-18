import platform, psutil

my_sys = platform.uname()
cpufreq = psutil.cpu_freq()

def displaySpecification():
    print(f"System: \t{my_sys.system}")
    print(f"Node name: \t{my_sys.node}")
    print(f"Version: \t{my_sys.version}")
    print(f"Machine: \t{my_sys.machine}")
    print(f"Processor: \t{my_sys.processor}")
    print(f"Physical Core: \t{psutil.cpu_count(logical=False)}")
    print(f"Max CPU Freq: \t{cpufreq.max:.2f} Mhz")
    print(f"Memory: \t{str(round(psutil.virtual_memory().total / (1024.0 ** 3)))} GB")
displaySpecification()