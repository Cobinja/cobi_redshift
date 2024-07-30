from Xlib import X, display, Xutil
from Xlib.ext import randr
import sys
import gamma_ramp

class X11Randr:
    
    def __init__(self):
        dpy = display.Display()
        if dpy == None:
            sys.stderr.write("Unable to open display\n")
        
        if not dpy.has_extension("RANDR"):
            print("X11 server does not have the RandR extension")
            sys.exit(1)
        
        screen = dpy.screen()
        root = screen.root
        res = randr.get_screen_resources_current(root)
        if res is None:
            sys.stderr.write("Unable to get screen resources\n")
            dpy.close()
            sys.exit(1)
        
        self.dpy = dpy
        self.res = res
    
    def close(self):
        self.dpy.close()
    
    def show_info(self, only_connected: bool = True):
        for c in range(len(self.res.outputs)):
            output_info = randr.get_output_info(self.dpy, self.res.outputs[c], 0)
            
            if (only_connected and output_info.connection == 0) or not only_connected:
                connected = "C" if output_info.connection == 0 else "D"
                w = 0
                h = 0
                if output_info.connection == 0:
                    crtc_info = randr.get_crtc_info(self.dpy, self.res.crtcs[c], 0)
                    w = crtc_info.width
                    h = crtc_info.height
                print(f"{c}:{connected}:{output_info.name}:{w}:{h}")
        self.close()
    
    def set_temperature(self, kelvin: int, bright: float, gamma: float):
        gammas: gamma_ramp.Gamma = None
        for output in self.res.outputs:
            output_info = randr.get_output_info(self.dpy, output, 0)
            if output_info.connection == 1:
                continue
            
            current_gamma = randr.get_crtc_gamma(self.dpy, output_info.crtc)
            if gammas is None:
                gammas = gamma_ramp.calculate_gamma_ramp(kelvin, bright, gamma, len(current_gamma.red))
            randr.set_crtc_gamma(self.dpy, output_info.crtc, len(gammas.r), gammas.r, gammas.g, gammas.b)
            
