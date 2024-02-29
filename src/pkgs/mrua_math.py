class MRUA():

    def mrua_s(self, t, vi, a, si):
        # S = vi*t+1/2*a*t*t
        S = si+vi*t+1/2*a*t**2
        return S
    
    def mrua_v(self, s, tf, si, ti):
        # V = (s - si) / (t - ti)
        V = (s - si) / (tf - ti)
        return V
    
    def mrua_a(self, v, t, ti, vi):
        # A = (v - vi ) / (t - ti) accellerazione
        A = (v - vi ) / (t - ti)
        return A
    
    def mrua_t(self, tf, ti):
        # T = tempo s
        T = tf - ti 
        return T
    
    def mrua_ta(self, a, vf, vi):
        # TA = tempo in funzione dell'accellerazione
        TA = (vf - vi ) / a
        return TA
