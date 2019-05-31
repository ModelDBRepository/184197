'''
Defines a class, Neuron472421285, of neurons from Allen Brain Institute's model 472421285

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472421285:
    def __init__(self, name="Neuron472421285", x=0, y=0, z=0):
        '''Instantiate Neuron472421285.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472421285_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Htr3a-Cre_NO152_Ai14_IVSCC_-178910.03.01.01_475125267_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472421285_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 83.11
            sec.e_pas = -91.8781604767
        
        for sec in self.axon:
            sec.cm = 2.45
            sec.g_pas = 0.000885550177117
        for sec in self.dend:
            sec.cm = 2.45
            sec.g_pas = 2.54573505548e-05
        for sec in self.soma:
            sec.cm = 2.45
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.0012797
            sec.gbar_Ih = 0.000133831
            sec.gbar_NaTs = 0.559007
            sec.gbar_Nap = 0.000445455
            sec.gbar_K_P = 0.0619124
            sec.gbar_K_T = 0.0172329
            sec.gbar_SK = 0.0396592
            sec.gbar_Kv3_1 = 0.205513
            sec.gbar_Ca_HVA = 0.000671399
            sec.gbar_Ca_LVA = 0.00361713
            sec.gamma_CaDynamics = 0.000422722
            sec.decay_CaDynamics = 249.354
            sec.g_pas = 0.000818114
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

