#!/bin/bash

case "$1" in
  build_generator)
    docker build -t football-generator ./generator
    ;;

  run_generator)
    docker run --rm -v "$(pwd)/data:/data" football-generator
    ;;

  *)
    echo "Unknown command"
    echo "Available commands:"
    echo "  build_generator"
    echo "  run_generator"
    ;;
esac