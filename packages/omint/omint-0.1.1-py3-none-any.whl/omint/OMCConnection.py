import random
import shutil
import subprocess

import zmq


class OMCConnection:

    def __init__(self, random_socket_name=False, port=10000):
        self._port = port
        self._omc_process = self._start_omc_process(random_socket_name)
        self._context = zmq.Context()
        self._omc_socket = self._create_client_socket()

    def __del__(self):
        self._omc_process.terminate()

    def _start_omc_process(self, random_socket_name):
        rand_string = str(random.randbytes(8))
        omc_executable = shutil.which("omc")
        cmd = [
            omc_executable, "--interactive=zmq",
            f"--interactivePort={self._port}"
        ]
        if random_socket_name:
            cmd.append(f"-z={rand_string}")

        proc = subprocess.Popen(cmd)

        return proc

    def _create_client_socket(self):
        sock = self._context.socket(zmq.REQ)
        sock.setsockopt(zmq.LINGER, 0)
        sock.connect(f"tcp://localhost:{self._port}")

        return sock

    def request(self, expression, timeout):
        self._omc_socket.send_string(expression)
        if self._omc_socket.poll(timeout) & zmq.POLLIN:
            reply = self._omc_socket.recv_string()

        return reply
