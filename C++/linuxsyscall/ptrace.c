#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/user.h>
#include <unistd.h>
#include <signal.h>

void print_registers(struct user_regs_struct *regs) {
    printf("R15: 0x%llx\n", regs->r15);
    printf("R14: 0x%llx\n", regs->r14);
    printf("R13: 0x%llx\n", regs->r13);
    printf("R12: 0x%llx\n", regs->r12);
    printf("R11: 0x%llx\n", regs->r11);
    printf("R10: 0x%llx\n", regs->r10);
    printf("R9: 0x%llx\n", regs->r9);
    printf("R8: 0x%llx\n", regs->r8);
    printf("RAX: 0x%llx\n", regs->rax);
    printf("RBX: 0x%llx\n", regs->rbx);
    printf("RCX: 0x%llx\n", regs->rcx);
    printf("RDX: 0x%llx\n", regs->rdx);
    printf("RSI: 0x%llx\n", regs->rsi);
    printf("RDI: 0x%llx\n", regs->rdi);
    printf("RBP: 0x%llx\n", regs->rbp);
    printf("RSP: 0x%llx\n", regs->rsp);
    printf("RIP: 0x%llx\n", regs->rip);
    printf("EFL: 0x%llx\n", regs->eflags);
    printf("CS: 0x%x\n", regs->cs);
    printf("SS: 0x%x\n", regs->ss);
    printf("DS: 0x%x\n", regs->ds);
    printf("ES: 0x%x\n", regs->es);
    printf("FS: 0x%x\n", regs->fs);
    printf("GS: 0x%x\n", regs->gs);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <pid>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    pid_t target_pid = atoi(argv[1]);

    // 附加到目标进程
    if (ptrace(PTRACE_ATTACH, target_pid, NULL, NULL) == -1) {
        perror("ptrace");
        exit(EXIT_FAILURE);
    }

    // 等待目标进程停止
    waitpid(target_pid, NULL, 0);

    // 获取寄存器信息
    struct user_regs_struct regs;
    if (ptrace(PTRACE_GETREGS, target_pid, NULL, &regs) == -1) {
        perror("ptrace");
        exit(EXIT_FAILURE);
    }

    // 打印寄存器信息
    print_registers(&regs);

    // 从目标进程中分离
    if (ptrace(PTRACE_DETACH, target_pid, NULL, NULL) == -1) {
        perror("ptrace");
        exit(EXIT_FAILURE);
    }

    return 0;
}
