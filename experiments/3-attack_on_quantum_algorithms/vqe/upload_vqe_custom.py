meta = {
    "name": "vqe_custom",
    "description": "A customized VQE program.",
    "max_execution_time": 180000,
    "spec": {},
}

meta["spec"]["parameters"] = {
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "properties": {
        "hamiltonian": {
            "description": "Hamiltonian whose ground state we want to find.",
            "type": "array",
        },
        "ansatz_circ": {
            "description": "The ansatz quantum circuit to use.",
            "type": "QuantumCircuit",
        },
        "initial_parameters": {
            "description": "Initial parameters of the ansatz. Can be an array or False to choose random initial parameters.", 
            "type": "Union[numpy.ndarray, str]", 
            "default": "False"
        },
        "state_prep_circ": {
            "description": "State preparation circuit.", 
            "type": "QuantumCircuit", 
            "default": "False"
        },
        "rep_delay": {
            "description": "rep_delay in IBMBackend.run().", 
            "type": "float", 
            "default": "None"
        },
        "init_qubits": {
            "description": "init_qubits in IBMBackend.run().", 
            "type": "bool", 
            "default": "None"
        },
        "add_delay_after_meas": {
            "description": "Whether add delay gate after the measurement circuits.", 
            "type": "bool", 
            "default": "False"
        },
        "delay_dt_after_meas": {
            "description": "Delay time in dt after the measure circuit. Only when add_delay_after_meas = True.", 
            "type": "int", 
            "default": "False"
        },
        "num_reset_after_prep": {
            "description": "Num of reset gate after the state preparation circuit. Only when add_reset_after_prep = True.", 
            "type": "int", 
            "default": "False"
        },
        "optimizer": {
            "description": "Classical optimizer to use, default='SPSA'.",
            "type": "string",
            "default": "SPSA",
        },
        "optimizer_config": {
            "description": "Configuration parameters for the optimizer.",
            "type": "object",
        },
        "shots": {
            "description": "The number of shots used for each circuit evaluation.",
            "type": "integer",
        },
        "use_measurement_mitigation": {
            "description": "Use measurement mitigation, default=False.",
            "type": "boolean",
            "default": False,
        },
    },
    "required": ["hamiltonian"],
}

meta["spec"]["return_values"] = {
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "description": "Final result in SciPy optimizer format",
    "type": "object",
}

meta["spec"]["interim_results"] = {
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "description": "Step, parameter vector at current optimization step, eigenvalue.",
    "type": "List",
}

from qiskit_ibm_runtime import QiskitRuntimeService
import os

service = QiskitRuntimeService(channel = "ibm_quantum")

# program_id = service.upload_program("./vqe_custom.py", metadata=meta)
program_id = "vqe-custom-k6DXyb1G46"
service.update_program(program_id=program_id, data="./vqe_custom.py", metadata=meta)
