import matplotlib.pyplot as plt
from impedance import preprocessing
from impedance.models.circuits import CustomCircuit
from impedance.visualization import plot_nyquist

if __name__ == '__main__':
    frequencies1, Z1 = preprocessing.readZPlot(
        'C:\\Users\\luowe\\Desktop\\IRP_code\\30th\\1.z')
    frequencies1, Z1 = preprocessing.ignoreBelowX(frequencies1, Z1)
    
    frequencies2, Z2 = preprocessing.readZPlot(
        'C:\\Users\\luowe\\Desktop\\IRP_code\\50th\\1.z')
    frequencies2, Z2 = preprocessing.ignoreBelowX(frequencies2, Z2)
    '''
    frequencies3, Z3 = preprocessing.readZPlot(
        'C:\\Users\\luowe\\Desktop\\IRP_code\\1st\\3.z')
    frequencies3, Z3 = preprocessing.ignoreBelowX(frequencies3, Z3)

    frequencies4, Z4 = preprocessing.readZPlot(
        'C:\\Users\\luowe\\Desktop\\IRP_code\\1st\\4.z')
    frequencies4, Z4 = preprocessing.ignoreBelowX(frequencies4, Z4)

    frequencies5, Z5 = preprocessing.readZPlot(
        'C:\\Users\\luowe\\Desktop\\IRP_code\\1st\\5.z')
    frequencies5, Z5 = preprocessing.ignoreBelowX(frequencies5, Z5)

    frequencies6, Z6 = preprocessing.readZPlot(
        'C:\\Users\\luowe\\Desktop\\IRP_code\\1st\\6.z')
    frequencies6, Z6 = preprocessing.ignoreBelowX(frequencies6, Z6)

    frequencies7, Z7 = preprocessing.readZPlot(
        'C:\\Users\\luowe\\Desktop\\IRP_code\\1st\\7.z')
    frequencies7, Z7 = preprocessing.ignoreBelowX(frequencies7, Z7)

    frequencies8, Z8 = preprocessing.readZPlot(
        'C:\\Users\\luowe\\Desktop\\IRP_code\\1st\\8.z')
    frequencies8, Z8 = preprocessing.ignoreBelowX(frequencies8, Z8)

    frequencies9, Z9 = preprocessing.readZPlot(
        'C:\\Users\\luowe\\Desktop\\IRP_code\\1st\\9.z')
    frequencies9, Z9 = preprocessing.ignoreBelowX(frequencies9, Z9)

    frequencies10, Z10 = preprocessing.readZPlot(
        'C:\\Users\\luowe\\Desktop\\IRP_code\\1st\\10.z')
    frequencies10, Z10 = preprocessing.ignoreBelowX(frequencies10, Z10)
    '''

    fig, ax = plt.subplots()
    plot_nyquist(ax, Z1, fmt='o')
    plot_nyquist(ax, Z2, fmt='o')
    plt.legend(['30th', '50th'])
    plt.show()