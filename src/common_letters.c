#include <stdio.h>
#include <string.h>

#define MAX_WORDS 1000
#define MAX_LENGTH 100
#define ALPHABET_SIZE 26

int main() {
    char words[MAX_WORDS][MAX_LENGTH];
    int common_letters[ALPHABET_SIZE];
    int word_count = 0;
    int i, j;

    // Initialize common_letters array
    for (i = 0; i < ALPHABET_SIZE; i++) {
        common_letters[i] = 1;
    }

    // Read words
    while (scanf("%s", words[word_count]) != EOF) {
        word_count++;
    }

    // Check common letters
    for (i = 0; i < word_count; i++) {
        int current_word_letters[ALPHABET_SIZE] = {0};

        for (j = 0; j < strlen(words[i]); j++) {
            current_word_letters[words[i][j] - 'a'] = 1;
        }

        for (j = 0; j < ALPHABET_SIZE; j++) {
            if (current_word_letters[j] == 0) {
                common_letters[j] = 0;
            }
        }
    }

    // Print common letters
    for (i = 0; i < ALPHABET_SIZE; i++) {
        if (common_letters[i] == 1) {
            printf("%c", i + 'a');
        }
    }

    return 0;
}