#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <time.h>

#include "config.h"
#include "ErrorHandle.h"


void printError(char *label) {
    printf("[%s]: %s\n", label, strerror(errno));
}

void createFile(char *name) {
    char file_name[MAX_SIZE];
    sprintf(file_name, "%s%s.txt", FILE_DIR, name);
    int fd =open(file_name, O_RDWR | O_APPEND | O_CREAT, S_IRWXU | O_EXCL);
    printError("Status");
}

void createTempFile() {
    char template[MAX_SIZE];
    sprintf(template, "%stemp-XXXXXX", FILE_DIR);
    mkstemp(template);

    // unlinking
    unlink(template);
}


int main() {
    char file_name[MAX_SIZE];
    sprintf(file_name, "%stest.txt", FILE_DIR);

    mkfifo(file_name, S_IRWXU);

    sleep(10);
    return 0;
}