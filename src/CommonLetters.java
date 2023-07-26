import java.util.*;

public class CommonLetters {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<String> words = new ArrayList<>();

        // Read words from the input
        while (scanner.hasNext()) {
            words.add(scanner.next());
        }

        // Find the common characters
        Set<Character> commonChars = getCommonCharacters(words);

        // Sort the characters in alphabetical order
        List<Character> sortedChars = new ArrayList<>(commonChars);
        Collections.sort(sortedChars);

        // Print the sorted common characters without spaces
        for (char c : sortedChars) {
            System.out.print(c);
        }
    }

    static Set<Character> getCommonCharacters(List<String> words) {
        // Initialize the set with characters from the first word
        Set<Character> commonChars = new HashSet<>();
        for (char c : words.get(0).toCharArray()) {
            commonChars.add(c);
        }

        // Find the intersection of all sets
        for (int i = 1; i < words.size(); i++) {
            Set<Character> wordChars = new HashSet<>();
            for (char c : words.get(i).toCharArray()) {
                wordChars.add(c);
            }
            commonChars.retainAll(wordChars);
        }

        return commonChars;
    }
}
