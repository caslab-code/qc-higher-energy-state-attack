import pickle

def get_job_data(job, average, scale_factor = 1):
    """Retrieve data from a job that has already run.
    Args:
        job (Job): The job whose data you want.
        average (bool): If True, gets the data assuming data is an average.
                        If False, gets the data assuming it is for single shots.
        scale_factor (float): Scaling factor for result data.
    Return:
        list: List containing job result data. 
    """
    import numpy as np

    if isinstance(job, list):
        result_data = [get_job_data(j, average, scale_factor=scale_factor) for j in job]
    else:
        num_qubits = job.backend_options()['n_qubits']
        job_results = job.result(timeout = 120) # timeout parameter set to 120 s
        if average:
            result_data = np.zeros((num_qubits, len(job_results.results)))
        else:
            shape = job_results.get_memory(0).shape
            result_data = np.zeros((num_qubits, len(job_results.results), shape[0]), dtype=complex)
        for i in range(len(job_results.results)):
            if average: # get avg data
                result_data[:, i] = np.real(job_results.get_memory(i) * scale_factor)
            else: # get single data
                result_data[:, i, :] = (job_results.get_memory(i) * scale_factor).reshape((-1, shape[0]))
    return result_data



def save_job(job, filename):
    """Save a job or a list of job to a pickle file.
    Args:
        filename (str): The name of the file.
        job (IBMQJob or list): The job to save
    Return:
        Job: The job that was saved in the pickle file.
    """
    with open(filename, 'wb') as f:
        pickle.dump(job, f)

def load_job(filename):
    """Save a job or a list of job to a pickle file.
    Args:
        filename (str): The name of the file.
    Return:
        Job: The job that was saved in the pickle file.
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)
