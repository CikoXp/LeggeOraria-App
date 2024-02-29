class MRU():

    def mru_s(self, si, v, t, ti):
        # s = v(t - ti) + s0
        S = (v * (t - ti)) + si
        return S

    def mru_v(self, s, si, t, ti):
        # v = (s - si) / (t - ti)
        V = (s - si) / (t - ti)
        return V

    def mru_t(self, s, si, v, ti):
        # t = (s - si) / v + ti
        T = ((s - si) / v) + ti
        return T
