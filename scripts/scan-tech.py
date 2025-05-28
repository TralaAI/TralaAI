#!/usr/bin/env python3
import os

# List of repos (folders) we checked out
REPOS = ["", "blazor-ui", "core-api", "fastapi", "model-trainer"]

# Mapping of file patterns to tech names
EXT_TECH = {
    ".csproj": "C#/.NET",
    ".cs":     "C#/.NET",
    "requirements.txt": "Python",
    ".py":     "Python",
    "package.json":      "Node.js",
    ".js":     "Node.js",
    ".ts":     "TypeScript",
}

nodes = set()
edges = set()

for repo in REPOS:
    base = repo or "."  # "" means root (main repo)
    label = os.path.basename(os.path.abspath(base))
    nodes.add(f'"{label}"')
    for root, _, files in os.walk(base):
        for f in files:
            for key, tech in EXT_TECH.items():
                if f.endswith(key) or f == key:
                    nodes.add(f'"{tech}"')
                    edges.add(f'"{label}" --> "{tech}"')

# Output Mermaid
print("```mermaid")
print("graph LR")
for n in sorted(nodes):
    print(f"  {n}")
for e in sorted(edges):
    print(f"  {e}")
print("```")
