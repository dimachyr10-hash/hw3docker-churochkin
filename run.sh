#!/bin/bash

case "$1" in
  build_generator)
    docker build -t football-generator ./generator
    ;;

  run_generator)
    docker run --rm -v "$(pwd)/data:/data" football-generator
    ;;

  create_local_data)
    mkdir -p local_data
    python generator/generate.py local_data
    ;;

  build_reporter)
    docker build -t football-reporter ./reporter
    ;;

  run_reporter)
    docker run --rm -v "$(pwd)/data:/data" football-reporter
    ;;
    
  *)
    echo "Unknown command"
    echo "Available commands:"
    echo "  build_generator"
    echo "  run_generator"
    echo "  create_local_data"
    echo "  build_reporter"
    echo "  run_reporter"
    ;;
esac