"""Capstone step 6: run the whole pipeline with `make pipeline`.

Fill in each TODO using what you built in the tutorials. Stop on the first failure.
"""
import subprocess
import sys


def run(cmd):
    print("+", " ".join(cmd))
    if subprocess.run(cmd).returncode != 0:
        sys.exit(1)


def main():
    # TODO 1: land bronze (masar.ingest.land_bronze)
    # TODO 2: register bronze tables (masar.register)
    # TODO 3: dbt build for silver (cd dbt/masar && dbt build)
    # TODO 4: build one gold mart
    # TODO 5: build the consumer table (BI-safe view or training set)
    # TODO 6: print row counts per layer
    raise NotImplementedError("Complete the TODOs")


if __name__ == "__main__":
    main()
