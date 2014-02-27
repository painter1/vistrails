import core.modules
import core.modules.module_registry
from core.modules.vistrails_module import Module, ModuleError
from Array import *
import scipy
import scipy.signal
from scipy import sparse, fftpack
import numpy

class WindowModule(object):
    my_namespace = 'scipy|signals|windows'

class HanningWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        out = NDArray()
        out.set_array(scipy.signal.hanning(size))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

class TriangularWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        out = NDArray()
        out.set_array(scipy.signal.triang(size))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

class BlackmanWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        out = NDArray()
        out.set_array(scipy.signal.blackman(size))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

class BlackmanHarrisWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        out = NDArray()
        out.set_array(scipy.signal.blackmanharris(size))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

class ParzenWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        out = NDArray()
        out.set_array(scipy.signal.parzen(size))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

class HammingWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        out = NDArray()
        out.set_array(scipy.signal.hamming(size))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

class KaiserWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        beta = self.getInputFromPort("Beta")
        out = NDArray()
        out.set_array(scipy.signal.kaiser(size, beta))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_input_port(cls, "Beta", (basic.Float, 'Beta'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

class BartlettHannWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        out = NDArray()
        out.set_array(scipy.signal.barthann(size))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

class GaussianWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        sigma = self.getInputFromPort("Sigma")
        out = NDArray()
        out.set_array(scipy.signal.gaussian(size, sigma))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_input_port(cls, "Sigma", (basic.Float, 'Sigma'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

class BoxcarWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        out = NDArray()
        out.set_array(scipy.signal.boxcar(size))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

class BohmanWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        out = NDArray()
        out.set_array(scipy.signal.bohman(size))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

class BartlettWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        out = NDArray()
        out.set_array(scipy.signal.bartlett(size))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

class NuttallBlackmanHarrisWindow(WindowModule, Module):
    def compute(self):
        size = self.getInputFromPort("Window Size")
        out = NDArray()
        out.set_array(scipy.signal.nuttall(size))
        self.setResult("Window", out)

    @classmethod
    def register(cls, reg, basic):
        reg.add_module(cls, namespace=cls.my_namespace)
        reg.add_input_port(cls, "Window Size", (basic.Integer, 'Window Size'))
        reg.add_output_port(cls, "Window", (NDArray, 'Window Function'))

