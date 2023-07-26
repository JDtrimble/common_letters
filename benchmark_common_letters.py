import subprocess
import time

input_str = "apple\npeach\n"

def benchmark_python():
    cmd = ['python3', 'common_letters.py']
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_cpp():
    cmd = ['./common_letters_cpp']
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_rust():
    cmd = ['./common_letters_rust']
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_c():
    cmd = ['./common_letters_c']
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

    print(f"Python time:\t{python_time:.6f} seconds")
    print(f"C++ time:\t{cpp_time:.6f} seconds")
    print(f"Rust time:\t{rust_time:.6f} seconds")
    print(f"C time:   \t{c_time:.6f} seconds")

    print(f"python output:\t{python_output}")
    print(f"c++ output:\t{cpp_output}")
    print(f"rust output:\t{rust_output}")
    print(f"c output:\t{c_output}")

    print(f"c++ is faster than python in {(python_time / cpp_time):.6f} times")
    print(f"rust is faster than c++ in {(cpp_time/rust_time):.6f} times")
    print(f"c is faster than rust in {(rust_time/c_time):.6f} times")