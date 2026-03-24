#!/usr/bin/env python3
"""Watch a directory and create ABR HLS/DASH outputs."""
import argparse, shutil, subprocess, time
from pathlib import Path

def require(x):
    if shutil.which(x) is None: raise SystemExit(f'Missing required binary: {x}')

def transcode(src, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd=['ffmpeg','-y','-i',str(src),'-filter_complex','[0:v]split=2[v1][v2];[v1]scale=1280:-2[v1o];[v2]scale=854:-2[v2o]','-map','[v1o]','-map','0:a?','-c:v:0','libx264','-b:v:0','3000k','-map','[v2o]','-map','0:a?','-c:v:1','libx264','-b:v:1','1200k','-c:a','aac','-f','hls','-hls_time','6',str(out_dir/'index.m3u8')]
    subprocess.check_call(cmd)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('watch_dir'); p.add_argument('output_root'); p.add_argument('--poll',type=int,default=5); p.add_argument('--dry-run',action='store_true')
    a=p.parse_args(); require('ffmpeg')
    seen=set()
    while True:
        for src in Path(a.watch_dir).glob('*'):
            if src.is_file() and src.suffix.lower() in {'.mp4','.mov','.mkv'} and src not in seen:
                print(f'Found {src}')
                if a.dry_run:
                    print('Would transcode to', Path(a.output_root)/src.stem)
                else:
                    transcode(src, Path(a.output_root)/src.stem)
                seen.add(src)
        time.sleep(a.poll)

if __name__ == '__main__': main()
