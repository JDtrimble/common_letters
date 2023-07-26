#include <stdio.h>
#include <string.h>

#define MAX_WORD_LENGTH 100
#define ALPHABET_SIZE 26

void updateLetterCount(const char *word, int letterCount[]) {
    int len = strlen(word);
    for (int i = 0; i < len; i++) {
        char ch = word[i];
        if (ch >= 'a' && ch <= 'z') {
            letterCount[ch - 'a']++;
        }
    }
}

int main() {
    int letterCount[ALPHABET_SIZE] = {0};
    int numWords = 0;
    
    // Read words from input
    char word[MAX_WORD_LENGTH + 1];
    while (scanf("%s", word) != EOF) {
        updateLetterCount(word, letterCount);
        numWords++;
    }

    // Print common letters in alphabetical order
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (letterCount[i] == numWords) {
            printf("%c", 'a' + i);
        }
    }
    printf("\n");

    return 0;
}
