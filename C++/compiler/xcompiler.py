with open(r'/mnt/c/Just-For-Fun/C++/compiler/add.x') as src:
    globalvartb = {}
    for line in src:
        tokens = line.split(" ")
        if tokens[0] == 'int':
            globalvartb[tokens[1]] = tokens[3].strip()
    with open(r'/mnt/c/Just-For-Fun/C++/compiler/add.S','w') as asm:
        asm.write('.section .data\n')
        for key,value in globalvartb.items():
            asm.write(f'{key}:      .quad {value}\n')
        
        asm.write('.section .text\n')
        asm.write('.global _start\n')
        
        asm.write('_start:\n') 
        asm.write('\t')