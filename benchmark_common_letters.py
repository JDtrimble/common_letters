import subprocess
import time
import sys

class UnknownPlatformError(Exception):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "If you have encountered this exception, you are using os, that is not supported"

input_str = "abcdef\nbcdefg\ncdefgh\ndefghi\nefghij\nfghijk\n"

def benchmark_python():
    if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        cmd = ['python3', 'common_letters.py']
    elif sys.platform.startswith("win"):
        cmd = ['python', 'common_letters.py']
    else:
        print()
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_cpp():
    if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        cmd = ['./common_letters_cpp']
    elif sys.platform.startswith("win") or sys.platform.startswith("win"):
        cmd = ['.\common_letters_cpp']
    else:
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_rust():
    if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        cmd = ['./common_letters_rust']
    elif sys.platform.startswith("win") or sys.platform.startswith("win"):
        cmd = ['.\common_letters_rust']
    else:
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_c():
    if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        cmd = ['./common_letters_c']
    elif sys.platform.startswith("win") or sys.platform.startswith("win"):
        cmd = ['.\common_letters_c']
    else:
        print(sys.platform)
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_java():
    cmd = ['java', 'CommonLetters']
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_go():
    if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        cmd = ['./common_letters_go']
    elif sys.platform.startswith("win") or sys.platform.startswith("win"):
        cmd = ['.\common_letters_go']
    else:
        print(sys.platform)
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_r():
    cmd = ['Rscript', 'common_letters.R']
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_pascal():
    if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        cmd = ['./common_letters_pascal']
    elif sys.platform.startswith("win") or sys.platform.startswith("win"):
        cmd = ['.\common_letters_pascal']
    else:
        print(sys.platform)
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_lua():
    cmd = ['lua', 'common_letters.lua']
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

if __name__ == "__main__":
    final_python = 0
    final_cpp = 0
    final_rust = 0
    final_c = 0
    final_java = 0
    final_go = 0
    final_r = 0
    final_pascal = 0
    final_lua = 0
    for i in range(100):
        python_output, python_time = benchmark_python()
        cpp_output, cpp_time = benchmark_cpp()
        rust_output, rust_time = benchmark_rust()
        c_output, c_time = benchmark_c()
        java_output, java_time = benchmark_java()
        go_output, go_time = benchmark_go()
        # r_output, r_time = benchmark_r()
        pascal_output, pascal_time = benchmark_pascal()
        lua_output, lua_time = benchmark_lua()
        
        final_python += python_time
        final_cpp += cpp_time
        final_rust += rust_time
        final_c += c_time
        final_java += java_time
        final_go += go_time
        # final_r += r_time
        final_pascal += pascal_time
        final_lua += lua_time
    final_python /= 100
    final_cpp /= 100
    final_rust /= 100
    final_c /= 100
    final_java /= 100
    final_go /= 100
    # final_r /= 100
    final_pascal /= 100
    final_r /= 100
    
    r_output, final_r = benchmark_r()  # 40 seconds is too long

    print(f"R time:   \t{final_r:.6f} seconds")
    print(f"Lua time:\t{final_lua:.6f} seconds")
    print(f"Java time:\t{final_java:.6f} seconds")
    print(f"Python time:\t{final_python:.6f} seconds")
    print(f"Go time:\t{final_go:.6f} seconds")
    print(f"C++ time:\t{final_cpp:.6f} seconds")
    print(f"Rust time:\t{final_rust:.6f} seconds")
    print(f"Pascal time:\t{final_pascal:.6f} seconds")
    print(f"C time:   \t{final_c:.6f} seconds")
    print()
    print(f"python output:\t{python_output}")
    print(f"c++ output:\t{cpp_output}")
    print(f"rust output:\t{rust_output}")
    print(f"c output:\t{c_output}")
    print(f"java output:\t{java_output}")
    print(f"go output:\t{go_output}")
    print(f"r output:\t{r_output}")
    print(f"pascal output:\t{pascal_output}")
    print(f"lua output:\t{lua_output}")
