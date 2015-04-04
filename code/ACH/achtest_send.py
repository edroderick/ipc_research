import ach
import ipc_include as ipc

chan = ach.Channel(ipc.CONTROLLER_REF_NAME)
chan.flush()
message = ipc.CONTROLLER_REF()


message.msg = 't'
chan.put(message)
