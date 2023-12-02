import numpy as np
from dataclasses import dataclass


def ciao():
    print('ciao')

@dataclass
class HarmonicOscillator:
    
    damped: bool = False

    def undamped_equation(self, t, A, k, m,  phi ):
        """
        General equation of an undamped harmonic oscillator.
        x(t) = Acos(omega * t + phi) where omega = np.sqrt(k/m) with m = the mass
        and k > 0 is a constant

        Parameters
        ----------
        t : array
            time array
        A : float
            amplitude
        k : float
            the positive constant
        m : float
            the mass of the oscillator
        phi : float
            the phase

        Returns
        -------
        array of floats
            return A(omega * t + phi)
        """
        omega = np.sqrt(k/m)
        return A*np.cos(omega * t + phi )
    

    def damped_equation(self, t, A, k, m,  phi, mu):
        """
        General equation of an damped harmonic oscillator.
        x(t) = e^(-sigma*t) * 2A*cos(omega * t + phi) where omega = np.sqrt(omega_0**2-sigma**2) and sigma = sigma = mu / (2*m) and omega_0 = np.sqrt(k/m) with sigma < omega_0 and k > 0 is a constant.

        Parameters
        ----------
        t : array
            time array
        A : float
            amplitude
        k : float
            the positive constant
        m : float
            the mass of the oscillator
        phi : float
            the phase
        mu : float
            something

        Returns
        -------
        array of floats
            return np.exp(-sigma*t) * (2*A * np.cos(omega*t + phi))
        """
        sigma = mu / (2*m)
        omega_0 = np.sqrt(k/m)
        assert sigma < omega_0
        omega = np.sqrt(omega_0**2-sigma**2)

        return np.exp(-sigma*t) * (2*A * np.cos(omega*t + phi))
    
    def equation(self, t, A, k, m,  phi, mu=0):
        if self.damped:
            return self.damped_equation( t, A, k, m,  phi, mu)
        else:
            return self.undamped_equation( t, A, k, m,  phi )



