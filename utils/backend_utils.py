def check_adjacency(qubit_pair_one, qubit_pair_two, backend):
    pairs = [[i, j] for i in qubit_pair_one for j in qubit_pair_two]
    for pair in pairs:
        for coupling in backend.configuration().coupling_map:
            if pair == coupling:
                return True
    return False



# def gen_control_circuit(qubit_pair, backend, duration = 3000, **transpiler_params):
#     if qubit_pair not in backend.configuration().coupling_map:
#         raise("The input qubit_pair is not in coupling_map.")
    
#     # cnot duration control
#     circ = QuantumCircuit(backend.configuration().n_qubits)
#     circ.cx(qubit_pair[0], qubit_pair[1])
#     cnot_duration = schedule(transpile(circ, backend), backend).duration
#     if cnot_duration > duration:
#         raise("CNOT duration on qubit_pair is longer than the specified duration")
    
#     # control
#     circ = QuantumCircuit(backend.configuration().n_qubits)
#     circ.barrier()
#     circ.cx(qubit_pair[0], qubit_pair[1])
#     circ.delay(duration - cnot_duration, qubit_pair)
#     circ.measure_all()
        
#     return transpile(circ, backend = backend, **transpiler_params)

    

# def gen_exp_circuits(qubit_pair_control, qubit_pair_adj, qubit_pair_nonadj, backend, duration = 3000, **transpiler_params):
#     if not check_adjacency(qubit_pair_control, qubit_pair_adj, backend):
#         raise("The input qubit_pair_control is not adjacent to qubit_pair_adj.")
#     if check_adjacency(qubit_pair_control, qubit_pair_nonadj, backend):
#         raise("The input qubit_pair_control is adjacent to qubit_pair_nonadj.")
    
#     # cnot duration control
#     circ = QuantumCircuit(backend.configuration().n_qubits)
#     circ.cx(qubit_pair_control[0], qubit_pair_control[1])
#     cnot_duration_control = schedule(transpile(circ, backend), backend).duration
#     if cnot_duration_control > duration:
#         raise("CNOT duration on qubit_pair_control is longer than the specified duration")
    
#     # cnot duration control
#     circ = QuantumCircuit(backend.configuration().n_qubits)
#     circ.cx(qubit_pair_adj[0], qubit_pair_adj[1])
#     cnot_duration_adj = schedule(transpile(circ, backend), backend).duration
#     if cnot_duration_adj > duration:
#         raise("CNOT duration on qubit_pair_adj is longer than the specified duration")
    
#     # cnot duration control
#     circ = QuantumCircuit(backend.configuration().n_qubits)
#     circ.cx(qubit_pair_nonadj[0], qubit_pair_nonadj[1])
#     cnot_duration_nonadj = schedule(transpile(circ, backend), backend).duration
#     if cnot_duration_nonadj > duration:
#         raise("CNOT duration on qubit_pair_nonadj is longer than the specified duration")
    
    
#     circs = []
    
#     # control
#     circ = QuantumCircuit(backend.configuration().n_qubits)
#     circ.barrier()
#     circ.cx(qubit_pair_control[0], qubit_pair_control[1])
#     circ.delay(duration - cnot_duration_control, qubit_pair_control)
#     circ.measure_all()
#     circs.append(circ)
    
#     # adjacent
#     circ = QuantumCircuit(backend.configuration().n_qubits)
#     circ.barrier()
#     circ.cx(qubit_pair_control[0], qubit_pair_control[1])
#     circ.delay(duration - cnot_duration_control, qubit_pair_control)
#     circ.cx(qubit_pair_adj[0], qubit_pair_adj[1])
#     circ.delay(duration - cnot_duration_adj, qubit_pair_adj)
#     circ.measure_all()
#     circs.append(circ)
    
#     # non-adjacent
#     circ = QuantumCircuit(backend.configuration().n_qubits)
#     circ.barrier()
#     circ.cx(qubit_pair_control[0], qubit_pair_control[1])
#     circ.delay(duration - cnot_duration_control, qubit_pair_control)
#     circ.cx(qubit_pair_nonadj[0], qubit_pair_nonadj[1])
#     circ.delay(duration - cnot_duration_nonadj, qubit_pair_nonadj)
#     circ.measure_all()
#     circs.append(circ)
    
#     transpiled_circs = transpile(circs, backend = backend, **transpiler_params)
    
#     circ_duration = [schedule(transpiled_circ, backend).duration for transpiled_circ in transpiled_circs]
#     if circ_duration[0] != circ_duration[1] or circ_duration[1] != circ_duration[2]:
#         raise("Circuit durations are not the same")
        
#     return transpiled_circs