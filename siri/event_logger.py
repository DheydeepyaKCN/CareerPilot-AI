from datetime import datetime

AGENT_LOG = []


def log_agent(
    agent_name,
    status,
    input_data=None,
    output_data=None,
    execution_time=None,
    error=None,
):
    AGENT_LOG.append(
        {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "agent": agent_name,
            "status": status,
            "input": input_data,
            "output": output_data,
            "execution_time": execution_time,
            "error": error,
        }
    )