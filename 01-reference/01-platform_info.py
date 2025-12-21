import sys
import platform

# python3 01-platform_info.py

def main():
    print('sys_platform : ', sys.platform)
    print('platform_machine : ', platform.machine())
    print('platform_system : ', platform.system())

if __name__ == '__main__':
    main()

#sys_platform: linux
#platform_machine: x86_64
#platform_system: Linux