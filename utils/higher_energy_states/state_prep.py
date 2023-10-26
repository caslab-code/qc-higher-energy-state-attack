from qiskit.circuit import QuantumCircuit, Gate

def gen_circ(state, num_qubit, qubit_list, sched = None, sched_list = None, num_reset = 0, reset_list = None, add_secure_reset = False, measure = True):
    circ = QuantumCircuit(num_qubit)

    if state > 1 and not sched_list:
        sched_list = list(range(len(qubit_list)))

    if state == -1:
        pass
    elif state == 0:
        pass
        # if add_delay:
        #     circ.delay(x_duration + x12_duration + x23_duration, qubit_list)
    elif state == 1:
        # if add_delay:
        #     circ.delay(x12_duration + x23_duration, qubit_list)
        circ.x(qubit_list)
    elif state == 2:
        # if add_delay:
        #     circ.delay(x23_duration, qubit_list)

        circ.x(qubit_list)

        if not sched:
            raise("Please specify Sched class!")
        x12_gate = Gate("x12_gate", 1, [])
        for i, qubit in enumerate(qubit_list):
            circ.append(x12_gate, [qubit])
            circ.add_calibration(x12_gate, (qubit, ), sched.get_sched(label = 'X12', qubit = sched_list[i]))
    elif state == 3:

        circ.x(qubit_list)

        if not sched:
            raise("Please specify Sched class!")

        x12_gate = Gate("x12_gate", 1, [])
        x23_gate = Gate("x23_gate", 1, [])
        for i, qubit in enumerate(qubit_list):
            circ.append(x12_gate, [qubit])
            circ.add_calibration(x12_gate, (qubit, ), sched.get_sched(label = 'X12', qubit = sched_list[i]))
            circ.append(x23_gate, [qubit])
            circ.add_calibration(x23_gate, (qubit, ), sched.get_sched(label = 'X23', qubit = sched_list[i]))
    for _ in range(num_reset):
        if add_secure_reset:
            x12_gate = Gate("x12_gate", 1, [])
            x23_gate = Gate("x23_gate", 1, [])
            if reset_list:
                for qubit in reset_list:
                    circ.reset(qubit)
                    circ.append(x12_gate, [qubit])
                    circ.add_calibration(x12_gate, (qubit, ), sched.get_sched(label = 'X12', qubit = qubit))
                    circ.reset(qubit)
                    circ.append(x23_gate, [qubit])
                    circ.add_calibration(x23_gate, (qubit, ), sched.get_sched(label = 'X23', qubit = qubit))
                    circ.append(x12_gate, [qubit])
                    circ.add_calibration(x12_gate, (qubit, ), sched.get_sched(label = 'X12', qubit = qubit))
                    circ.reset(qubit)
            else:
                for qubit in qubit_list:
                    circ.reset(qubit)
                    circ.append(x12_gate, [qubit])
                    circ.add_calibration(x12_gate, (qubit, ), sched.get_sched(label = 'X12', qubit = qubit))
                    circ.reset(qubit)
                    circ.append(x23_gate, [qubit])
                    circ.add_calibration(x23_gate, (qubit, ), sched.get_sched(label = 'X23', qubit = qubit))
                    circ.append(x12_gate, [qubit])
                    circ.add_calibration(x12_gate, (qubit, ), sched.get_sched(label = 'X12', qubit = qubit))
                    circ.reset(qubit)
        else:
            if reset_list:
                circ.reset(reset_list)
            else:
                circ.reset(qubit_list)
    
    if measure:
        circ.measure_all()
    
    return circ