def run_exp(circ, num_exp, backend, shots = 500):
    job_ids = []
    for _ in range(num_exp):
        job = backend.run(circ, shots = shots)
        job_ids.append(job.job_id())
    return job_ids

def dump_job_ids(job_ids, qubit_layout, dirname = None, filename = None, mode = 'a'):
    from datetime import datetime
    import json
    import os
    
    file = {}
    file["time"] = [str(datetime.now())]
    file["qubit_layout"] = qubit_layout
    file["num_jobs"] =  [len(job_ids)]
    file["job_ids"] = job_ids
    
    if not dirname:
        dirname = './'
    
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    
    if not filename:
        filename = "jobs_ids_" + str(datetime.now()).replace('-','_').replace(' ','_').replace(':','_')[:19] + ".json"
    
    
    if mode == 'a':
        if os.path.isfile(os.path.join(dirname, filename)):
            with open(os.path.join(dirname, filename), 'r') as f:
                previous_data = json.load(f)
                if qubit_layout != previous_data["qubit_layout"]:
                    raise("qubit_layout is different")
            with open(os.path.join(dirname, filename), 'w') as f:
                file["time"] = previous_data["time"] + file["time"]
                file["num_jobs"] = previous_data["num_jobs"] + file["num_jobs"]
                file ["job_ids"] = previous_data["job_ids"] + file ["job_ids"]
                json.dump(file, f, indent = 4)
                print('jobs_ids were successfully saved to "' + filename + '"')
        else:
            with open(os.path.join(dirname, filename), 'w') as f:
                json.dump(file, f, indent = 4)
                print('jobs_ids were successfully saved to "' + filename + '"')
        
    elif mode == 'w':
        with open(os.path.join(dirname, filename), 'w') as f:
            json.dump(file, f, indent = 4)
            print('jobs_ids were successfully saved to "' + filename + '"')
    
    else:
        raise("Please specify open() mode, either 'a' or 'w'")