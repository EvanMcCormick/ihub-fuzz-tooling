# Dockerfile for InspireHub C# fuzzing with SharpFuzz
# This file exists for OSS-Fuzz compatibility but the actual build
# is handled by ButterCup's build_fuzzers_csharp() method.
FROM mcr.microsoft.com/dotnet/sdk:10.0

RUN apt-get update && apt-get install -y --no-install-recommends \
    clang git ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /src
COPY . /src/
