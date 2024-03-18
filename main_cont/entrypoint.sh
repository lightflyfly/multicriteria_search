#!/bin/bash

wait_for_elasticsearch() {
  tries=1
  echo "Waiting for Elastisearch node 1..."
  until curl "$ELASTIC_HOST:$ELASTIC_PORT/_cluster/health?wait_for_status=yellow&timeout=30s"; do
    >&2 echo "Elastisearch is unavailable - waiting for it... 😴 ($tries)"
    sleep 1
    tries=$(expr $tries + 1)
  done
  echo "Elasticsearch is ready!"
}

wait_for_elasticsearch

uvicorn main:app --proxy-headers --host "$MAIN_HOST" --port "$MAIN_PORT"