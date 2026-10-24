#!/bin/sh
# Pull the latest rsmify image from GHCR and restart the service only if the
# image actually changed. Driven by a */5 cron on syenite:
#
#   */5 * * * * ~/home-server/scripts/rsmify-update.sh >> ~/home-server/logs/rsmify-update.log 2>&1
#
# The image is public, so no docker login is needed. CI (the rsmify-image
# workflow) builds and pushes ghcr.io/aris-pub/rsmify:latest on each push to
# main that touches the importer or grammar.
set -eu

IMAGE=ghcr.io/aris-pub/rsmify:latest

before=$(docker image inspect --format '{{.Id}}' "$IMAGE" 2>/dev/null || echo none)
if ! docker pull -q "$IMAGE" >/dev/null 2>&1; then
    echo "$(date -Is) pull failed, keeping the current image"
    exit 0
fi
after=$(docker image inspect --format '{{.Id}}' "$IMAGE" 2>/dev/null || echo none)

if [ "$before" != "$after" ]; then
    echo "$(date -Is) image changed ($before -> $after), restarting rsmify"
    sudo systemctl restart rsmify.service
    docker image prune -f >/dev/null 2>&1 || true
else
    echo "$(date -Is) no change"
fi
