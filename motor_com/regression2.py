import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def regression():
    dist = np.array([2.003, 2.987, 4.041, 5.055, 6.016, 6.996, 7.937, 9.04, 9.995])
    pos = np.array([333000, 280000, 254000, 239000, 229000, 222000, 217000, 213000, 209500])

    # Define the inverse function to fit: x = a / (y - c) + b
    def inverse_func(y, a, b, c):
        return a / (y - c) + b

    # Initial guess for a, b, c
    initial_guess = [10000, 200000, 0]

    # Curve fitting
    popt, pcov = curve_fit(inverse_func, dist, pos, p0=initial_guess)

    # Extract fitted parameters
    a_fit, b_fit, c_fit = popt
    print(f"Fitted parameters: a = {a_fit}, b = {b_fit}, c = {c_fit}")
    #return a_fit, b_fit, c_fit

    # Generate fitted curve
    dist_fit = np.linspace(min(dist), max(dist), 1000)
    pos_fit = inverse_func(dist_fit, *popt)

    # Plot the data points
    plt.figure(figsize=(8, 6))
    plt.scatter(dist, pos, color='blue', label='Data Points')
    plt.plot(dist_fit, pos_fit, color='red', label=f'Fitted: {a_fit:.5f} / (y - {c_fit:.2f}) + {b_fit:.0f}')

    # Adding labels and title
    plt.xlabel('Distance (m)')
    plt.ylabel('Position (m)')
    plt.title(r'$y=\frac{a}{x - c} + b$')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()


if __name__ == '__main__':
    regression()