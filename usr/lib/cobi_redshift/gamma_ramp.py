from cmath import log
from dataclasses import dataclass
from typing import List

@dataclass
class RGB:
    r: float
    g: float
    b: float

@dataclass
class Gamma:
    r: List[int]
    g: List[int]
    b: List[int]

def kelvin_to_rgb(kelvin) -> RGB:
    temp = kelvin / 100.0
    color = RGB(255, 255, 255)
    r = 0.0
    g = 0.0
    b = 0.0
    
    if kelvin == 6500:
        return color
    
    if temp <= 66:
        r = 255.0
        g = 99.4708025861 * log(temp).real - 161.1195681661
        if temp <= 19:
            b = 0.0
        else:
            b = 138.5177312231 * log(temp - 10).real - 305.0447927307
    else:
        r = 329.698727446 * pow(temp - 60, -0.1332047592)
        g = 288.1221695283 * pow(temp - 60, -0.0755148492)
        b = 255.0
    
    color.r = min(max(0.0, r), 255.0)
    color.g = min(max(0.0, g), 255.0)
    color.r = min(max(0.0, b), 255.0)
    
    return color

def calculate_gamma_ramp(kelvin: int, bright: float, gamma: float, ramp_size: int):
    MAX = 256.0
    temperature = kelvin_to_rgb(kelvin)
    gamma_ramps = Gamma([], [], [])
    for i in range(0, ramp_size):
        value = float(i) / ramp_size
        
        r = value * temperature.r * bright
        g = value * temperature.g * bright
        b = value * temperature.b * bright
        
        gamma_ramps.r.append(int(pow(r, 1.0 / gamma) * MAX))
        gamma_ramps.g.append(int(pow(g, 1.0 / gamma) * MAX))
        gamma_ramps.b.append(int(pow(b, 1.0 / gamma) * MAX))
    return gamma_ramps

