#!/bin/bash

#open ACH channel and run python scripts

IPC_CHAN='ipc-chan'

MakeACH(){
  ach -1 -C $IPC_CHAN -m 30 -n 30000
  sudo chmod 777 /dev/shm/achshm-*
}

KillAll(){
  sudo rm -r /dev/shm/achshm*
}

case "$1" in
  'make' )
    MakeACH
  ;;
  'kill' )
    KillAll
  ;;
  *)
    MakeACH
    #call python scripts
  ;;
esac

exit 0
#END
