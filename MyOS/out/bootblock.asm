
out/bootblock.o:     file format elf32-i386


Disassembly of section .text:

00007c00 <start>:
    7c00:	fa                   	cli    
    7c01:	31 c0                	xor    %eax,%eax
    7c03:	8e d8                	mov    %eax,%ds
    7c05:	8e c0                	mov    %eax,%es
    7c07:	8e d0                	mov    %eax,%ss

00007c09 <seta20.1>:
    7c09:	e4 64                	in     $0x64,%al
    7c0b:	a8 02                	test   $0x2,%al
    7c0d:	75 fa                	jne    7c09 <seta20.1>
    7c0f:	b0 d1                	mov    $0xd1,%al
    7c11:	e6 64                	out    %al,$0x64

00007c13 <seta20.2>:
    7c13:	e4 64                	in     $0x64,%al
    7c15:	a8 02                	test   $0x2,%al
    7c17:	75 fa                	jne    7c13 <seta20.2>
    7c19:	b0 df                	mov    $0xdf,%al
    7c1b:	e6 60                	out    %al,$0x60
    7c1d:	0f 01 16             	lgdtl  (%esi)
    7c20:	68 7c 0f 20 c0       	push   $0xc0200f7c
    7c25:	66 83 c8 01          	or     $0x1,%ax
    7c29:	0f 22 c0             	mov    %eax,%cr0
    7c2c:	ea                   	.byte 0xea
    7c2d:	31 7c 08 00          	xor    %edi,0x0(%eax,%ecx,1)

00007c31 <start32>:
    7c31:	66 b8 10 00          	mov    $0x10,%ax
    7c35:	8e d8                	mov    %eax,%ds
    7c37:	8e c0                	mov    %eax,%es
    7c39:	8e d0                	mov    %eax,%ss
    7c3b:	66 b8 00 00          	mov    $0x0,%ax
    7c3f:	8e e0                	mov    %eax,%fs
    7c41:	8e e8                	mov    %eax,%gs
    7c43:	bc 00 7c 00 00       	mov    $0x7c00,%esp
    7c48:	e8 94 00 00 00       	call   7ce1 <bootmain>

00007c4d <spin>:
    7c4d:	eb fe                	jmp    7c4d <spin>
    7c4f:	90                   	nop

00007c50 <gdt>:
	...
    7c58:	ff                   	(bad)  
    7c59:	ff 00                	incl   (%eax)
    7c5b:	00 00                	add    %al,(%eax)
    7c5d:	9a cf 00 ff ff 00 00 	lcall  $0x0,$0xffff00cf
    7c64:	00                   	.byte 0x0
    7c65:	92                   	xchg   %eax,%edx
    7c66:	cf                   	iret   
	...

00007c68 <gdtdesc>:
    7c68:	17                   	pop    %ss
    7c69:	00 50 7c             	add    %dl,0x7c(%eax)
	...

00007c6e <readsect>:
    7c6e:	f3 0f 1e fb          	endbr32 
    7c72:	55                   	push   %ebp
    7c73:	89 e5                	mov    %esp,%ebp
    7c75:	57                   	push   %edi
    7c76:	bf f7 01 00 00       	mov    $0x1f7,%edi
    7c7b:	8b 4d 0c             	mov    0xc(%ebp),%ecx
    7c7e:	89 fa                	mov    %edi,%edx
    7c80:	ec                   	in     (%dx),%al
    7c81:	83 e0 c0             	and    $0xffffffc0,%eax
    7c84:	3c 40                	cmp    $0x40,%al
    7c86:	75 f6                	jne    7c7e <readsect+0x10>
    7c88:	b0 01                	mov    $0x1,%al
    7c8a:	ba f2 01 00 00       	mov    $0x1f2,%edx
    7c8f:	ee                   	out    %al,(%dx)
    7c90:	ba f3 01 00 00       	mov    $0x1f3,%edx
    7c95:	89 c8                	mov    %ecx,%eax
    7c97:	ee                   	out    %al,(%dx)
    7c98:	89 c8                	mov    %ecx,%eax
    7c9a:	ba f4 01 00 00       	mov    $0x1f4,%edx
    7c9f:	c1 e8 08             	shr    $0x8,%eax
    7ca2:	ee                   	out    %al,(%dx)
    7ca3:	89 c8                	mov    %ecx,%eax
    7ca5:	ba f5 01 00 00       	mov    $0x1f5,%edx
    7caa:	c1 e8 10             	shr    $0x10,%eax
    7cad:	ee                   	out    %al,(%dx)
    7cae:	89 c8                	mov    %ecx,%eax
    7cb0:	ba f6 01 00 00       	mov    $0x1f6,%edx
    7cb5:	c1 e8 18             	shr    $0x18,%eax
    7cb8:	83 c8 e0             	or     $0xffffffe0,%eax
    7cbb:	ee                   	out    %al,(%dx)
    7cbc:	b0 20                	mov    $0x20,%al
    7cbe:	89 fa                	mov    %edi,%edx
    7cc0:	ee                   	out    %al,(%dx)
    7cc1:	ba f7 01 00 00       	mov    $0x1f7,%edx
    7cc6:	ec                   	in     (%dx),%al
    7cc7:	83 e0 c0             	and    $0xffffffc0,%eax
    7cca:	3c 40                	cmp    $0x40,%al
    7ccc:	75 f8                	jne    7cc6 <readsect+0x58>
    7cce:	8b 7d 08             	mov    0x8(%ebp),%edi
    7cd1:	b9 80 00 00 00       	mov    $0x80,%ecx
    7cd6:	ba f0 01 00 00       	mov    $0x1f0,%edx
    7cdb:	fc                   	cld    
    7cdc:	f3 6d                	rep insl (%dx),%es:(%edi)
    7cde:	5f                   	pop    %edi
    7cdf:	5d                   	pop    %ebp
    7ce0:	c3                   	ret    

00007ce1 <bootmain>:
    7ce1:	f3 0f 1e fb          	endbr32 
    7ce5:	55                   	push   %ebp
    7ce6:	89 e5                	mov    %esp,%ebp
    7ce8:	83 ec 10             	sub    $0x10,%esp
    7ceb:	6a 01                	push   $0x1
    7ced:	68 00 00 40 00       	push   $0x400000
    7cf2:	e8 77 ff ff ff       	call   7c6e <readsect>
    7cf7:	e9 04 83 3f 00       	jmp    400000 <__bss_start+0x3f82a0>
    7cfc:	83 c4 10             	add    $0x10,%esp
    7cff:	c9                   	leave  
    7d00:	c3                   	ret    
