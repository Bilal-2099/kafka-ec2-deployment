# Kafka EC2 Deployment

## Overview

Repository for deploying **Apache Kafka and Zookeeper** on an **AWS EC2 instance** with related example scripts and notebooks.

## Structure

```
├── Data/
├── Jupyter Notebook/
├── Python/
├── Commands.txt
├── README.md
```

- `Data/`: Example data used in notebooks or scripts.  
- `Jupyter Notebook/`: Notebooks demonstrating Kafka producer/consumer usage.  
- `Python/`: Python scripts for Kafka clients.  
- `Commands.txt`: Shell commands used for EC2 + Kafka + Zookeeper setup.

## Requirements

Install Python Kafka library:

```bash
pip install kafka-python
```

## Usage
Running Python Producers/Consumers

Navigate to the Python/ folder and run scripts:

```bash
python producer_script.py
python consumer_script.py
```
Insufficient data to verify exact filenames inside Python/.

## Notebooks
Open notebooks under Jupyter Notebook/:

```bash
jupyter notebook
```

Use these for step‑by‑step Kafka producer/consumer demonstrations.

## Deployment Reference

Use commands in Commands.txt to:
- SSH into your AWS EC2 instance.
- Install Java (required for Kafka).
- Download and extract Kafka binaries.
- Configure and start Zookeeper service.
- Configure and start Kafka broker.
- Open required security group ports on AWS (e.g., 2181 for Zookeeper, 9092 for Kafka). 
CodeBurps

