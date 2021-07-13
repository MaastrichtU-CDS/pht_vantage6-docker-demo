cp /containerfiles/${1}.yaml ./${1}.yaml
vnode-local start -c ./${1}.yaml --dockerized