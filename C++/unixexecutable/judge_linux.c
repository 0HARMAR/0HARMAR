#include <stdio.h>
#include <string.h>

#define _LINUX 0
#define _WSL 1

int judge_system() {
    FILE *fp = fopen("/proc/version", "r");
    if (fp == NULL) {
        perror("Error opening /proc/version");
        return -1;
    }
    
    char buffer[256];
    if (fgets(buffer, sizeof(buffer), fp) != NULL) {
        if (strstr(buffer, "microsoft") != NULL) {
            fclose(fp); 
            return 1;  // WSL detected
        }
    }
    
    fclose(fp);
    return 0;  // Not WSL, assuming standard Linux
}

int _system = judge_system();--

