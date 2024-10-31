#!/bin/bash


qemu-system-x86_64  -s -S -drive file=xv6.img,format=raw &

gdb -q -ex "arget remote localhost:1234"
