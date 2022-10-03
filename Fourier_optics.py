import numpy as np
from scipy.fft import fft2, fftfreq, fftshift, ifft2
import pint

unit = pint.UnitRegistry()

class AngularSpectrumMethod: