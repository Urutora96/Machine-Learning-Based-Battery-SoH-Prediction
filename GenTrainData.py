import matplotlib.pyplot as plt
from impedance import preprocessing
from impedance.models.circuits import CustomCircuit
from impedance.visualization import plot_nyquist

circuit = 'R0-p(R1,C1)-p(R2-Wo1,C2)'
initial_guess = [.1, .01, .1, .05, .001, 20, 1]
circuit = CustomCircuit(circuit, initial_guess=initial_guess)

if __name__ == '__main__':
    # Read and fit EIS data
    frequencies, Z = preprocessing.readZPlot(
        'C:\\Users\\luowe\\Desktop\\IRP_code\\Battery_Data\\50th\\10.z')
    frequencies, Z = preprocessing.ignoreBelowX(frequencies, Z)
    circuit.fit(frequencies, Z)
    para = circuit.parameters_

    # Generate training data
    f = 'training data.txt'
    with open(f, "a") as file:
        file.write(
            '50' + ',' + str(para[0]) + ',' + str(para[1]) + ',' + str(para[3]) + '\n')
        file.close()

    # Plot data curve and fit curve
    Z_fit = circuit.predict(frequencies)
    fig, ax = plt.subplots()
    plot_nyquist(ax, Z, fmt='o')
    plot_nyquist(ax, Z_fit, fmt='-')
    plt.legend(['Data', 'Fit'])
    plt.show()
