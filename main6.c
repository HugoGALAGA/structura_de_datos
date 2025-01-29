//Call stack
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

char* make_upper(const char* text) {
    char buffer[100];
    snprintf(buffer, sizeof(buffer), "%s!!!", text);

    for (int i = 0; buffer[i]; i++) {
        buffer[i] = toupper(buffer[i]);
    }

    return strdup(buffer);
}

int main() {
    const char *text = "Run!";
    char *upper_text = make_upper(text);

    printf("Length: %zu\n", strlen(upper_text));
    free(upper_text);
    return 0;
}


