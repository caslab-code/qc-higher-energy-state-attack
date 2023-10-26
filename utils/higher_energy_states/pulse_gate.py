from typing import Iterable


class Sched:
    def __init__(self, backend):
        self.backend = backend

        # example:
        # gate_data = [
        #     {
        #         "name": 'parametric_pulse',
        #         "label": 'X01',
        #         "pulse_shape": 'Gaussian',
        #         "freq": None,
        #         'qubit': 0,
        #         "parameters": {
        #                         'duration': 160,
        #                         'amp': 0.15,
        #                         'sigma': 40,
        #                         'name': 'x12_pulse'
        #                     }
        #     }
        # ]
        self.gate_data = []

        self.scheds = []

        self.num_qubits = backend.configuration().num_qubits

    def add_gate_data(self, data_name, data):
        self.gate_data[data_name] = data



    def get_gate_data(self, data_name = None):
        if data_name:
            return self.gate_data[data_name]
        else:
            return self.gate_data



    def create_scheds(self):
        from qiskit import pulse
        for gate in self.gate_data:
            sched_dict = {
                "name": gate["name"],
                "label": gate["label"],
                "qubit": gate["qubit"]
            }
            with pulse.build(backend=self.backend, default_alignment='sequential', name=gate["label"]) as sched:
                drive_chan = pulse.drive_channel(gate["qubit"])
                if gate["freq"]:
                    pulse.set_frequency(gate["freq"], drive_chan)
                if gate["pulse_shape"] == 'Gaussian':
                    waveform = pulse.Gaussian
                # TODO: add other waveform
                pulse.play(waveform(**gate["parameters"]), drive_chan)
            sched_dict["sched"] = sched
            self.scheds.append(sched_dict)



    def get_sched(self, label = None, qubit = None):
        if isinstance(qubit, Iterable):
            sched_list = []
            for sched in self.scheds:
                if sched['label'] == label and sched['qubit'] in qubit:
                    sched_list.append(sched['sched'])
            return sched_list
        elif isinstance(qubit, int):
            for sched in self.scheds:
                if sched['label'] == label and sched['qubit'] == qubit:
                    return sched['sched']



    def get_scheds(self):
        return self.scheds



    def save_gate_data(self, filename = None):
        import json, os, sys
        with open(filename if filename else os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), self.backend.name() + "_gate_data.json"), "w") as f:
            json.dump(self.gate_data, f, indent = 4)



    def load_gate_data(self, filename = None):
        import json, os, sys
        with open(filename if filename else os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), self.backend.name() + "_gate_data.json"), "r") as f:
            self.gate_data = json.load(f)
            return self.gate_data



    def parse_pi_12_23_gate_data(self, freq_12_list, pi_amp_12_list, freq_23_list, pi_amp_23_list, pi_duration_12 = 160, pi_sigma_12 = 40, pi_duration_23 = 160, pi_sigma_23 = 40, save = False, filename = None):
        for qubit, (freq, amp) in enumerate(zip(freq_12_list, pi_amp_12_list)):
            self.gate_data.append({
                    "name": 'parametric_pulse',
                    "label": 'X12',
                    "pulse_shape": 'Gaussian',
                    "freq": freq,
                    'qubit': qubit,
                    "parameters": {
                                    'duration': pi_duration_12,
                                    'amp': amp,
                                    'sigma': pi_sigma_12,
                                    'name': 'x12_pulse'
                                }
            })

        for qubit, (freq, amp) in enumerate(zip(freq_23_list, pi_amp_23_list)):
            self.gate_data.append({
                    "name": 'parametric_pulse',
                    "label": 'X23',
                    "pulse_shape": 'Gaussian',
                    "freq": freq,
                    'qubit': qubit,
                    "parameters": {
                                    'duration': pi_duration_23,
                                    'amp': amp,
                                    'sigma': pi_sigma_23,
                                    'name': 'x23_pulse'
                                }
            })
        
        if save:
            self.save_gate_data(filename)