#include "config.h"
#include "ReadData.h"
#include "ErrorHandle.h"
#include "timer.h"

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>


clock_t start;

void printError(char *label) {
    printf("[%s]: %s\n", label, strerror(errno));
}

double calculateTime(clock_t start) {
    double cpu_time_used;
    clock_t end;

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    return cpu_time_used;
}

void PrintTime() {
    printf("cpu time taken: %f\n", calculateTime(start));
}

int main() {
    double cpu_time_used;
    start = clock();

    for(int i=0; i<1000000000; i++) {
        
    }
    
    PrintTime();
    return 0;
}