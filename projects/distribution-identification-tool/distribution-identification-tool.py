# Distribution Identification Tool
## This tool helps identify potential discrete probability distributions

def calculate_mean_variance(values, frequencies):
    total_freq = 0
    total = 0

    for i in range(len(values)):
        total += values[i] * frequencies[i]
        total_freq += frequencies[i]

    mean = total / total_freq

    variance_sum = 0
    for i in range(len(values)):
        variance_sum += frequencies[i] * (values[i] - mean) ** 2

    variance = variance_sum / total_freq

    return mean, variance


#Input Section

print("Distribution Identification Tool")

values = list(map(float, input("Enter values of random variable (separated by space): ").split()))
frequencies = list(map(int, input("Enter corresponding frequencies: ").split()))

#Input validation
if len(values) != len(frequencies):
    print("Error: Number of values and frequencies must be equal.")
    exit()

mean, variance = calculate_mean_variance(values, frequencies)

print("\nMean =", mean)
print("Variance =", variance)

fixed_trials = input("\nIs the number of trials fixed? (yes/no): ").lower()


#Distribution Identification Logic 

if fixed_trials == "yes":
    categories = int(input("Enter number of categories: "))

    if categories == 2:
        replacement = input("Is sampling done with replacement? (yes/no): ").lower()

        if replacement == "yes":
            print("\nData is consistent with a Binomial distribution (indicative assessment).")
        else:
            print("\nData is consistent with a Hypergeometric distribution (indicative assessment).")

    elif categories > 2:
        print("\nData is consistent with a Multinomial distribution (indicative assessment).")

    else:
        print("\nInvalid number of categories.")


elif fixed_trials == "no":

    if mean != 0 and abs(mean - variance) / mean < 0.2:
        print("\nData is consistent with a Poisson distribution (indicative assessment).")

    elif variance > mean:
        stopped = input("Are trials stopped after first success? (yes/no): ").lower()

        if stopped == "yes":
            print("\nData is consistent with a Geometric distribution (indicative assessment).")
        else:
            print("\nData is consistent with a Negative Binomial distribution (indicative assessment).")

    else:
        print("\nNo standard discrete distribution suggested under current criteria.")


else:
    print("\nInvalid input. Please answer yes or no.")