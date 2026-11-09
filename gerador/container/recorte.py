#!/usr/bin/env python3
"""Recorta a pessoa da foto (u2net_human_seg.onnx). Uso: recorte.py <modelo.onnx> <foto> <saida.png>"""
import sys, numpy as np, onnxruntime as ort
from PIL import Image, ImageFilter
mod, src, out = sys.argv[1:4]
im = Image.open(src).convert("RGB")
x = np.asarray(im.resize((320, 320), Image.LANCZOS)).astype(np.float32) / 255.0
x = (x - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
x = x.transpose(2, 0, 1)[None].astype(np.float32)
s = ort.InferenceSession(mod, providers=["CPUExecutionProvider"])
m = s.run(None, {s.get_inputs()[0].name: x})[0][0, 0]
m = (m - m.min()) / (m.max() - m.min() + 1e-8)
mask = Image.fromarray((m * 255).astype(np.uint8)).resize(im.size, Image.LANCZOS).filter(ImageFilter.GaussianBlur(1))
rgba = im.copy(); rgba.putalpha(mask)
rgba.crop(rgba.getbbox()).save(out)
