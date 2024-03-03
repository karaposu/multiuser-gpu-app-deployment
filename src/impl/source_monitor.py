import psutil
from pydantic import AnyUrl, BaseModel, EmailStr, Field

def get_disk_space():
    return "Disk space usage: 75%"

def get_memory_usage():
    return "Memory usage: 60%"

def get_gpu_usage():
    return "GPU usage: 40%"

def get_queue_lengths():
    return "Queue lengths: 5"


class SystemMonitoringResponse(BaseModel):
    disk_space_usage: str
    memory_usage: str
    gpu_usage: str  # This requires a more specialized approach, possibly with a library like GPUtil
    queue_lengths: str  # This is highly application-specific


def prepare_response_for_source_monitoring():
    def bytes_to_gb(bytes, round_digits=2):
        return round(bytes / (1024 ** 3), round_digits)

    disk = psutil.disk_usage('/')
    memory = psutil.virtual_memory()

    # Convert each attribute to GB
    disk_total_gb = bytes_to_gb(disk.total)
    disk_used_gb = bytes_to_gb(disk.used)
    disk_free_gb = bytes_to_gb(disk.free)

    memory_total_gb = bytes_to_gb(memory.total)
    memory_available_gb = bytes_to_gb(memory.available)

    # Placeholder values
    gpu_usage = "50%"
    queue_lengths = "42"

    return SystemMonitoringResponse(
        disk_space_usage=f"Total: {disk_total_gb} GB, Used: {disk_used_gb} GB, Free: {disk_free_gb} GB",
        memory_usage=f"Total: {memory_total_gb} GB, Available: {memory_available_gb} GB",
        gpu_usage=gpu_usage,
        queue_lengths=queue_lengths
    )



    return SystemMonitoringResponse(
        disk_space_usage=f"Total: {disk_usage.total}, Used: {disk_usage.used}, Free: {disk_usage.free}",
        memory_usage=f"Total: {memory_usage.total}, Available: {memory_usage.available}",
        gpu_usage=gpu_usage,
        queue_lengths=queue_lengths
    )

