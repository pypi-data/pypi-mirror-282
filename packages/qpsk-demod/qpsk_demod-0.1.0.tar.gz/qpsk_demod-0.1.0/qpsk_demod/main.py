import numpy as np
def qpsk_demod(r,fc,of):
     """
    Perform Quadrature Phase Shift Keying (QPSK) demodulation on the received signal.

    Parameters:
    r (array-like): The received modulated signal.
    fc (float): Carrier frequency.
    of (int): Oversampling factor, determining the number of samples per symbol.

    Returns:
    tuple:
        a_hat (numpy.ndarray): The estimated binary data stream.
        x (numpy.ndarray): The demodulated in-phase component.
        y (numpy.ndarray): The demodulated quadrature component.

    This function performs the following steps:
    1. Demodulates the in-phase (I) and quadrature (Q) components from the received signal.
    2. Applies a low-pass filter to extract the baseband signal.
    3. Downsamples the filtered signals to the symbol rate.
    4. Estimates the binary data stream by thresholding the demodulated signals.

    Example:
    >>> r = np.array([0.5, -0.5, 1.0, -1.0, 0.5, -0.5, -1.0, 1.0])
    >>> fc = 100
    >>> of = 4
    >>> a_hat, x, y = qpsk_demod(r, fc, of) """
     fs=of*fc
     L=2*of
     t=np.arange(0,len(r)/fs,1/fs)
     x=r*np.cos(2*np.pi*fc*t)
     y=-r*np.sin(2*np.pi*fc*t)
     x=np.convolve(x,np.ones(L))
     y=np.convolve(y,np.ones(L))
     x=x[L-1::L]
     y=y[L-1::L]
     a_hat=np.zeros((2*len(x)))
     a_hat[0::2]=(x>0)
     a_hat[1::2]=(y>0)
     return(a_hat,x,y)
