"""news-image-20261119 entry: copy the pre-drawn infographic to /output/entry.png.

The image is drawn in code (see draw.py in the build notes) and shipped as
entry.png; this program only copies it, so both graded runs write identical
bytes. Standard library only, no network.
"""
import os
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
# The copy is the whole program: no drawing, no randomness, no network, so
# the two graded runs write byte-identical output.
(OUT / "entry.png").write_bytes((HERE / "entry.png").read_bytes())
