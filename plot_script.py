import matplotlib.pyplot as plt

# File paths
basic_path = "outputs/basic/"
efficient_path = "outputs/efficient/"

def get_last_two_floats(file_path):
    with open(file_path, "r") as f:
        lines = f.read().strip().split("\n")
        return float(lines[-2]), float(lines[-1])

def get_time_and_mem_from_file(file_path):
    with open(file_path,"r") as f:
        lines = f.read().strip().split("\n")
        return (float(lines[3]), float(lines[4]))

if __name__ == '__main__':
    basic_time_values = []
    basic_mem_values = []
    efficient_time_values = []
    efficient_mem_values = []
    total_str_lens_values = [16, 64,128,256,384, 512,768,1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968]

    for i in range(1, 16):
        basic_file = basic_path + str(i) + '.txt'
        efficient_file = efficient_path + str(i) + '.txt'

        basic_time, basic_mem = get_time_and_mem_from_file(basic_file)
        efficient_time, efficient_mem = get_time_and_mem_from_file(efficient_file)

        basic_time_values.append(basic_time)
        basic_mem_values.append(basic_mem)
        efficient_time_values.append(efficient_time)
        efficient_mem_values.append(efficient_mem)

    # Plot time comparison
    plt.figure(figsize=(10,5))
    plt.plot(total_str_lens_values, basic_time_values,   'o-', label='Basic Time')
    plt.plot(total_str_lens_values, efficient_time_values,'o-', label='Efficient Time')
    plt.xlabel("Total String Length")
    plt.ylabel("Time")
    plt.title("Time vs. Total String Length")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("time_vs_length.png")

    # Plot memory comparison
    plt.figure(figsize=(10, 5))
    plt.plot(total_str_lens_values,basic_mem_values, 'o-', label='Basic Time')
    plt.plot(total_str_lens_values,efficient_mem_values, 'o-', label='Efficient Time')
    plt.xlabel("Total String Length")
    plt.ylabel("Memory")
    plt.title("Memory vs. Total String Length")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("memory_vs_length.png")
