import platform
import subprocess
import psutil
import wmi
import traceback
import sys

def get_system_info():
    info = {}

    # OS info
    uname = platform.uname()
    info['OS NAME'] = uname.system
    info['VERSION'] = uname.release
    info['OS MANUFACTURER'] = uname.version

    # Sysinfo using Windows Windows Management Instrumentation
    wmi_c = wmi.WMI()
    computer_system = wmi_c.Win32_ComputerSystem()[0]
    system_info = wmi_c.Win32_OperatingSystem()[0]
    bios_info = wmi_c.Win32_BIOS()[0]
    baseboard_info = wmi_c.Win32_BaseBoard()[0]
    system_sku = wmi_c.Win32_SystemEnclosure()[0].SerialNumber
    system_bios = wmi_c.Win32_SystemBIOS()[0]

    try:
        info['SYSTEM NAME'] = computer_system.Name
        info['SYSTEM MANUFACTURER'] = computer_system.Manufacturer
        info['SYSTEM MODEL'] = computer_system.Model
        info['SYSTEM TYPE'] = computer_system.SystemType
        info['SYSTEM SKU'] = system_sku if system_sku else "Not Available"
        info['PROCESSOR'] = computer_system.NumberOfProcessors
        info['BIOS VERSION/DATE'] = str(bios_info.BIOSVersion) + " " + str(bios_info.ReleaseDate)
        info['SMBIOS VERSION'] = bios_info.SMBIOSBIOSVersion
        info['BIOS MODE'] = system_bios.BiosCharacteristics if hasattr(system_bios, 'BiosCharacteristics') else "Not Available"
        info['BASEBOARD MANUFACTURER'] = baseboard_info.Manufacturer
        info['BASEBOARD PRODUCT'] = baseboard_info.Product
        info['BASEBOARD VERSION'] = baseboard_info.Version
    
        # Other sysinfo
        info['WINDOWS DIRECTORY'] = system_info.WindowsDirectory
        info['SYSTEM DIRECTORY'] = system_info.SystemDirectory

        info['LOCALE'] = subprocess.check_output(["systeminfo", "/fo", "list"]).decode("utf-8")
        locale_line = [line.strip() for line in info['LOCALE'].split('\n') if 'System Locale' in line]
        info['LOCALE'] = locale_line[0].split(':')[1].strip() if locale_line else "Not Available"

        info['USER NAME'] = subprocess.check_output(["whoami"], text=True).strip()

        # Memory info
        virtual_memory = psutil.virtual_memory()
        info['TOTAL PHYSICAL MEMORY'] = virtual_memory.total
        info['AVAILABLE PHYSICAL MEMORY'] = virtual_memory.available
        info['TOTAL VIRTUAL MEMORY'] = virtual_memory.total
        info['AVAILABLE VIRTUAL MEMORY'] = virtual_memory.available
    except AttributeError as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        line_number = exc_tb.tb_lineno
        error_type = exc_type.__name__
        print("AttributeError Unknown or Not availeble:  ", e)
    except TypeError as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        line_number = exc_tb.tb_lineno
        error_type = exc_type.__name__
        print(f"{error_type} occured at line {line_number}: {exc_obj}")
    

    return info

if __name__ == "__main__":
    info = get_system_info()
    with open("sysinfo.txt", "a") as file:
        for key, value in info.items():
            file.write(f"{key}: {value}\n")
    print("DEBUG: Successfully appended data to file.")