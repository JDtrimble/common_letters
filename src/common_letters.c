#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* common_letters(char** words, int num_words) {
    if (num_words == 0) {
        return strdup("");
    }

    char* common = strdup(words[0]);
    for (int i = 1; i < num_words; ++i) {
        int k = 0;
        for (int j = 0; j < strlen(common); ++j) {
            if (strchr(words[i], common[j]) != NULL) {
                common[k++] = common[j];
            }
        }
        common[k] = '\0';
    }

    return common;
}

int main() {
    char* words[1000];
    int num_words = 0;
    char word[101];

    while (fgets(word, sizeof(word), stdin)) {
        word[strcspn(word, "\n")] = '\0';
        words[num_words] = strdup(word);
        num_words++;
    }

    char* result = common_letters(words, num_words);
    printf("%s\n", result);

    // Free allocated memory
    for (int i = 0; i < num_words; ++i) {
        free(words[i]);
    }
    free(result);

    return 0;
}
