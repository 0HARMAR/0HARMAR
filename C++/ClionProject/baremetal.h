#include <stdint.h>
typedef uint8_t u8;
typedef int32_t i32;
typedef uint32_t u32;
typedef uint64_t u64;
typedef uintptr_t uptr;

#if __STDC_HOSTED__ == 1 // gcc a.c 会激活此分支代码 (else 分支代码被删除) 有操作系统
  #include <stdio.h>
  #include <stdlib.h>
  static inline void putch(u32 ch) { putchar(ch); }
  static inline void putd(u32 d) { printf("%d", d); }
  static inline void halt() { exit(0); }
  #define entry main // 用 “main” 替换 entry
#else // gcc -ffreestanding a.c 会激活 else 分支代码 无操作系统
  static inline void putch(u32 ch) {
    register u32 op asm ("rax") = 1, val asm ("rbx") = ch;
    asm volatile("int $0x03" : : "r"(op), "r"(val));
  }
  static inline void putd(u32 d) {
    register u32 op asm ("rax") = 2, val asm ("rbx") = d;
    asm volatile("int $0x03" : : "r"(op), "r"(val));
  }
  __attribute__((noreturn)) static inline void halt() { register u32 op asm ("rax") = 3; asm volatile("int $0x03" : : "r"(op)); while (1); // 声明了 “nonreturn”，避免编译器给出警告 }
#endif
