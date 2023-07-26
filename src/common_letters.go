package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	words := readWords()

	// Find the common characters
	commonChars := getCommonCharacters(words)

	// Sort and print the characters in alphabetical order without spaces
	for c := range commonChars {
		fmt.Print(string(c))
	}
}

func readWords() []string {
	var words []string
	scanner := bufio.NewScanner(os.Stdin)

	// Read words from the input
	for scanner.Scan() {
		words = append(words, scanner.Text())
	}

	return words
}

func getCommonCharacters(words []string) map[rune]bool {
	// Initialize the map with characters from the first word
	commonChars := make(map[rune]bool)
	for _, c := range words[0] {
		commonChars[c] = true
	}

	// Find the intersection of all maps
	for _, word := range words[1:] {
		wordChars := make(map[rune]bool)
		for _, c := range word {
			wordChars[c] = true
		}

		// Remove characters not present in the current word
		for c := range commonChars {
			if !wordChars[c] {
				delete(commonChars, c)
			}
		}
	}

	return commonChars
}
