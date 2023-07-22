#!/bin/bash

# Common variables.
env_file='./develop/compose-env.sh'
compose_file='./develop/compose.yaml'
compose_common_arg="--file $compose_file --env-file $env_file"

# Preflight checks.
if ! test -f $env_file; then
    echo "The env file ${env_file} is not found."
    exit 1
fi
source $env_file

if ! test -f $compose_file; then
    echo "The docker compose config is not found."
    exit 1
fi

# Exit functions that stops containers by Ctrl+C call.
trap ctrl_c INT 
ctrl_c () {
    docker compose $compose_common_arg down
}

# Run them!
docker compose $compose_common_arg up --wait --force-recreate --renew-anon-volumes 

# Wait for the startup process. Don't use sleep() here! Only pooling!
while true; do
    curl -s http://127.0.0.1:${VAULT_PORT}/v1/sys/init | fgrep -q '{"initialized":true}'
    retval=$?
    test $retval -eq 0 && break
    sleep 1
done
echo -e "\nThe vault on port ${VAULT_PORT} has started!\n"
docker ps

# Now it can make smth with the vault.
# curl ....

# The command waits for Ctrl+C but Ctrl+C makes is trapped.
echo -e "\nPress Ctrl+C to exit and stop containers."
sleep $((2**30))