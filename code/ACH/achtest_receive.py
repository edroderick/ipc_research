import ach
import ipc_include as ipc

chan = ach.Channel(ipc.CONTROLLER_REF_NAME)
chan.flush()
message = ipc.CONTROLLER_REF()


[status, framesize] = chan.get(message, wait=True, last=True)
test = message.msg
print test


