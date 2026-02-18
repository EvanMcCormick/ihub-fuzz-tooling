#!/usr/bin/env python3
"""Minimal OSS-Fuzz helper.py stub for ButterCup compatibility.

ButterCup's ChallengeTask requires infra/helper.py to exist in the fuzz tooling
repository. For C# and JavaScript projects, the actual build is handled by
custom build methods (build_fuzzers_csharp, build_fuzzers_javascript) and this
file is not invoked.
"""
import sys

if __name__ == "__main__":
    print("This is a stub helper.py for ButterCup C#/JS fuzz tooling.")
    print("The actual build is handled by ButterCup's custom build methods.")
    sys.exit(0)
