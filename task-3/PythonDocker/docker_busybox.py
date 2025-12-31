import docker
import time


client = docker.from_env()


container = client.containers.run(
    image="busybox",
    command="sleep 300", #מחכה 5 דקות עד שהקונטיינר יסגר
    detach=True #מריץ ברקע את הפקודה
)

print("Container started")

time.sleep(1)

exec_result = container.exec_run("hostname")

print("Container hostname:", exec_result.output.decode())


container.stop()
container.remove()
