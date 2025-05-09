import matplotlib.pyplot as plt

# File paths
basic_path = "outputs/basic/"
efficient_path = "outputs/efficient/"


def get_last_two_floats(file_path):
    with open(file_path, "r") as f:
        lines = f.read().strip().split("\n")
        return float(lines[-2]), float(lines[-1])

if __name__ == '__main__':
    basic_time_values = []
    basic_mem_values = []
    efficient_time_values = []
    efficient_mem_values = []

    for i in range(1, 16):
        basic_file = basic_path + str(i) + '.txt'
        efficient_file = efficient_path + str(i) + '.txt'

        basic_time, basic_mem = get_last_two_floats(basic_file)
        efficient_time, efficient_mem = get_last_two_floats(efficient_file)

        basic_time_values.append(basic_time)
        basic_mem_values.append(basic_mem)
        efficient_time_values.append(efficient_time)
        efficient_mem_values.append(efficient_mem)

    # Plot time comparison
    plt.figure(figsize=(10, 5))
    plt.plot(basic_time_values, label='Basic Time', marker='o')
    plt.plot(efficient_time_values, label='Efficient Time', marker='o')
    plt.xlabel("Test Case (1 to 15)")
    plt.ylabel("Time")
    plt.title("Time Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("time_comparison.png")

    # Plot memory comparison
    plt.figure(figsize=(10, 5))
    plt.plot(basic_mem_values, label='Basic Memory', marker='o')
    plt.plot(efficient_mem_values, label='Efficient Memory', marker='o')
    plt.xlabel("Test Case (1 to 15)")
    plt.ylabel("Memory")
    plt.title("Memory Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("memory_comparison.png")
