# qc-higher-energy-state-attack

This is the repository for ACM CCS 23 Artifact Appendix: Securing NISQ Quantum Computer Reset Operations Against
Higher-Energy State Attacks.

## Abstract

This paper first proposes to use the higher-energy states to attack quantum computers. This work shows that common reset protocols are ineffective in resetting a qubit from a higher-energy
state. To provide a defense, this work proposes a new Cascading Secure Reset (CSR) operation. CSR, without hardware modifications, is able to efficiently and reliably reset higher-energy states back to
|0⟩. CSR achieves a reduction in |3⟩-initialized state leakage channel capacity by between 1 and 2 orders of magnitude, and does so with a 25x speedup compared with the default decoherence reset.

In the artifact evaluation, we provide source code and experiments corroborating the claims made in this paper.

## Description & Requirements

### Security, Privacy, and Ethical Concerns

This study involves non-destructive procedures, posing no security, privacy, or ethical risks for evaluators.

### How to Access

Check the GitHub repository from https://github.com/caslab-code/qc-higher-energy-state-attack.

### Hardware Dependencies

The code is primarily Python-based and should be compatible with most CPUs. In addition, access to quantum computers is required. The experiments in this study were conducted on IBM Quantum's platforms. One can register it at https://www.ibm.com/quantum.

### Software Dependencies

Similarly, the code requires users to execute Python and Jupyter Notebook, and how to install the dependencies will be introduced in the following. Besides, there is no specific requirement for the software or operating systems. However, due to the path resolution issue with different operating systems, we may require users to manually change some path specifications in the code.

### Benchmarks

N/A.


## Set-up

### Installation

#### Software Dependencies

Python is the main programming language for this paper. We recommend creating a new Python environment for evaluations.

First, install the dependencies with the command:

```bash
pip install qiskit qiskit[visualization] qiskit-ibmq-provider qiskit-aer pandas matplotlib plotly seaborn ipykernel
```
These modules are `qiskit`, `qiskit[visualization]`, `qiskit-ibmq-provider`, `qiskit-aer`, which are the quantum computing software development kit we used in this paper. For more information, please see [Qiskit Official Website](https://qiskit.org/). Other modules are `pandas` for data manipulation, `matplotlib`, `plotly` and `seaborn` for figure plotting, and `ipykernel` for the Jupyter Notebook running.

Besides, the directory `utils` contains helper functions to shorten the code and speed up the process for the experiments.


#### Access to IBM Quantum

The access to IBM Quantum is required. One can register at [IBM Quantum Platform](https://quantum-computing.ibm.com/).

To setup the Qiskit account, visit the IBM Quantum Account web page and copy the account API token at: [IBM Quantum Account](https://quantum-computing.ibm.com/account). Replace `MY_API_TOKEN` below with it and execute the following code snippet:
```python
   from qiskit import IBMQ
   IBMQ.save_account('MY_API_TOKEN')
```

We provide a quick load function to access the provider. To set up, create a JSON file `provider.json` containing the credential information under the path `experiments`. For example, in the Linux system, this can be done with the command (starting from the root):
```bash
touch experiments/provider.json
```

Inside the file, include the access information. One example:
```json
{
   "hub": "ibm-q", 
   "group": "open", 
   "project": "main"
}
```

#### Notes on Reproducibility

Due to the fast updates of the needed Python modules, the code may not be successfully executed if different versions of dependencies are used. We provide here the version used in this paper:


| Name      | Version |
| ----------- | ----------- |
|matplotlib   |             3.8.0|
|numpy        |             1.23.5|
|pandas | 1.4.3 |
|python        |            3.9.18|
|qiskit         |           0.44.2|
|qiskit-aer      |          0.12.2|
|qiskit-ibmq-provider  |    0.20.2|
|qiskit-terra          |    0.25.2.1|

Additionally, quantum computers on IBM Quantum may retire in the future. On different quantum computers, the results may be different. However, this does not hurt the main claims in the paper. This paper mainly used `ibm_lagos` to perform the experiments, which is announced to be retired on November 28, 2023.

### Basic Test

Once installation is successful, the code should be executable. Follow the provided evaluation workflow to validate experiment reproducibility.


## Evaluation Workflow

### Major Claims

We provide all necessary code and experiments to generate the data and figures presented in the paper. Users can reproduce the results by following the outlined steps.

### Experiments

The experiments done in this paper are presented under the directory `experiments`. The authors did the experiments with a personal computer, which is equipped with 12th Gen Intel(R) Core(TM) i7-12700H 2.69 GHz and 32 GB RAM.

The experiments can be reproduced by executing the Jupyter Notebooks under the directory `experiments`. The estimated human-time is the time of running the Jupyter notebooks and thus is negligible. The estimated compute-time for personal machines is also negligible. Below, we list the approximated compute-hour for the current quantum computer, specifically, `ibm_lagos` that used in this paper. For each experiment, we posted the raw data in the paper under the directory `data` of each experiment directory for reference, and we also provide the calibration data for pulses under the directory `experiments/data`. The experiments include:

1. `0-calibration` [1 compute-hour]:
   This directory contains the code to obtain the calibration data for $\pi$ pulse.
   1. `calibration.ipynb`: Figure 4, which shows the calibration data for $\pi$ pulse.

2. `1-basis_gate_and_decoherence` [1 compute-hour]: This directory contains the code for the basis gate tomography and the decoherence pattern of higher-energy states.
   1. `basis_gate_tomography.ipynb`: Table 1, which shows the influence of basis gates on different states.
   2. `delay.ipynb`: Figure 5, which shows the higher-energy states decoherence patterns on the IQ plane. Figure 7, which shows the decoherence behavior of different states.
   3. `reset.ipynb`: Figure 6, which shows the influence of the normal reset and CSR on different states.

3. `2-state_leakage` [6 compute-hours]: This directory contains the code to evaluate state leakage and Shannon capacity of the covert channel with different reset mechanisms and delay times.
    1. `state_leakage.ipynb`: Figure 9, which displays the state leakage of various reset protocols as a function of end-to-end delay; Figure 10, which examines the worst-case Shannon capacity across the state leakage covert channel of various protocols as a function of end-to-end delay. The notebook utilizes experiment data stored in the `data` subdirectory and exports PDF and interactive HTML figures to the `figures` subdirectory. The relevant data directly informs Table 3.

4. `3-attack_on_quantum_algorithms` [3 compute-hours]: This directory contains the code for the attack on four quantum algorithms: Deutsch-Jozsa, inverse quantum Fourier transformation, Grover's search, and variational quantum eigensolver (VQE).
   1. `vqe`: (Due to the IBM Quantum architecture update, this may be disabled temporarily for the custom program, so this may not be successfully executed) This directory contains the code for creating the custom VQE program, and the code to generate Figure 13, which shows the optimization process of VQE with different input states.
   2. `quantum_algorithms.ipynb`: Table 4 and Figure 12, which shows the results of Deutsch-Jozsa, inverse quantum Fourier transformation, and Grover's search with different input states.

5. `4-trojan_circuit_attack` [10 compute-minutes]: This directory contains the code for the trojan circuit attack.
   1. `attack_circuit.ipynb`: Figure 14, which shows the trojan circuit attack that drives the qubit to higher-energy states.
   2. `state_sensing_grover.ipynb`: Figure 15, which shows the example of trojan attacks on two-qubit Grover's search.


## Version

Based on the LaTeX template for Artifact Evaluation V20231005. Submission,
reviewing and badging methodology followed for the evaluation of this artifact
can be found at https://secartifacts.github.io/acmccs2023/.