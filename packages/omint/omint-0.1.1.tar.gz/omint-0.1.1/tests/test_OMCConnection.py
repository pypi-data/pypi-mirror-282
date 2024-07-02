from omint.OMCConnection import OMCConnection


def test__start_omc_process():
    omc = OMCConnection()
    proc = omc._start_omc_process(False)

    assert proc.pid

    proc.terminate()


def test_request():
    omc = OMCConnection()
    reply = omc.request("getVersion()", 5000)

    assert reply
