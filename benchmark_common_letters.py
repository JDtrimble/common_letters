import subprocess
import time
import sys

class UnknownPlatformError(Exception):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "If you have encountered this exception, you are using os, that is not supported"

input_str = "apple\npeach\n"

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

if __name__ == "__main__":
    python_output, python_time = benchmark_python()
    cpp_output, cpp_time = benchmark_cpp()
    rust_output, rust_time = benchmark_rust()
    c_output, c_time = benchmark_c()
    java_output, java_time = benchmark_java()
    go_output, go_time = benchmark_go()
    r_output, r_time = benchmark_r()

    print(f"Java time:\t{java_time:.6f} seconds")
    print(f"Python time:\t{python_time:.6f} seconds")
    print(f"Go time:\t{go_time:.6f} seconds")
    print(f"C++ time:\t{cpp_time:.6f} seconds")
    print(f"Rust time:\t{rust_time:.6f} seconds")
    print(f"C time:   \t{c_time:.6f} seconds")
    print(f"R time:   \t{r_time:.6f} seconds")
    print()
    print(f"python output:\t{python_output}")
    print(f"c++ output:\t{cpp_output}")
    print(f"rust output:\t{rust_output}")
    print(f"c output:\t{c_output}")
    print(f"java output:\t{java_output}")
    print(f"go output:\t{go_output}")
    print(f"r output:\t{r_output}")
    print()
    print(f"java is faster than r in {(r_time / java_time):.6f} times")
    print(f"python is faster than java in {(java_time / python_time):.6f} times")
    print(f"c++ is faster than python in {(python_time / cpp_time):.6f} times")
    print(f"go is faster than python in {(python_time / go_time):.6f} times")
    if go_time < cpp_time:
        print(f"go is faster than c++ in {(cpp_time/go_time):.6f} times")
    else:
        print(f"c++ is faster than go in {(go_time/cpp_time):.6f} times")
    print(f"rust is faster than c++ in {(cpp_time/rust_time):.6f} times")
    print(f"c is faster than rust in {(rust_time/c_time):.6f} times")
