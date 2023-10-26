def load_job_ids(dirname = None, filename = None, num = None):
    from datetime import datetime
    import json
    import os

    if not dirname:
        dirname = './'
    
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    
    if not filename:
        filename = "jobs_ids_" + str(datetime.now()).replace('-','_').replace(' ','_').replace(':','_')[:19] + ".json"
    
    with open(os.path.join(dirname, filename), 'r') as f:
        data = json.load(f)
        print('job_ids were successfully loaded')
    
    if isinstance(num, int):
        return data["job_ids"][-1 * num:]
    else:
        return data["job_ids"]



def get_time_taken(job_ids, backend):
    return [backend.retrieve_job(job_id).result().to_dict()['time_taken'] for job_id in job_ids]



def single_qubit_count(counts, qubit_idx):
    num_qubits = len(list(counts[0].keys())[0])
    count_single_qubit = [[0, 0] for _ in range(len(counts))] 
    for circ_idx in range(len(counts)):
        count = counts[circ_idx].int_outcomes()
        for i in range(2**(num_qubits - qubit_idx)):
            for j in range(i * 2**qubit_idx, (i+1) * 2**qubit_idx):
                if j in count.keys():
                    state = i % 2
                    count_single_qubit[circ_idx][state] += count[j]
    return count_single_qubit



def baseline_remove(values, axis, reshape):
    """Center data around 0."""
    import numpy as np
    return np.array(values) - np.mean(values, axis = axis).reshape(reshape)



def fit_function(x_values, y_values, function, init_params):
    """Fit a function using scipy curve_fit."""
    from scipy.optimize import curve_fit
    fitparams, conv = curve_fit(function, x_values, y_values, init_params, maxfev = 50000)
    y_fit = function(x_values, *fitparams)
    
    return fitparams, y_fit