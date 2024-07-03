import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import upfirdn
from scipy.special import erfc
def qpsk_mod(a,fc,of):
    """
    Perform Quadrature Phase Shift Keying (QPSK) modulation on the input signal.

    Parameters:
    a (array-like): Input binary data stream.
    fc (float): Carrier frequency.
    of (int): Oversampling factor, determining the number of samples per symbol.

    Returns:
    tuple:
        s_t (numpy.ndarray): The modulated signal in the time domain.
        I (numpy.ndarray): The in-phase component of the input signal.
        Q (numpy.ndarray): The quadrature component of the input signal.

    This function performs the following steps:
    1. Separates the input data stream into in-phase (I) and quadrature (Q) components.
    2. Upsamples and converts the binary data into bipolar format.
    3. Modulates the in-phase component with a cosine carrier.
    4. Modulates the quadrature component with a sine carrier.
    5. Combines the modulated components to form the QPSK modulated signal.
    6. Plots various intermediate signals for visualization.

    Example:
    >>> a = np.array([0, 1, 1, 0, 1, 1, 0, 0])
    >>> fc = 100
    >>> of = 4
    >>> s_t, I, Q = qpsk_mod(a, fc, of)
    """
    L=2*of
    I=a[0::2];Q=a[1::2]
    I=upfirdn(h=[1]*L,x=2*I-1,up=L)
    Q=upfirdn(h=[1]*L,x=2*Q-1,up=L)
    plt.plot(I)
    plt.title('inphase msg signal')
    plt.show()
    plt.plot(Q)
    plt.title('quadphase msg signal')
    plt.show()
    fs=of*fc
    t=np.arange(0,len(I)/fs,1/fs)
    I_t=I*np.cos(2*np.pi*fc*t)
    Q_t=-Q*np.sin(2*np.pi*fc*t)
    plt.plot(t,I_t)
    plt.title('inphase modulated signal')
    plt.show()
    plt.plot(t,Q_t)
    plt.title('quadphase modulated signal')
    plt.show()
    s_t=I_t+Q_t
    plt.plot(s_t)
    plt.title('transmitted signal')
    plt.show()
    return s_t,I,Q
