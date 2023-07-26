# Function to get common characters
get_common_characters <- function(words) {
  # Initialize the list with characters from the first word
  common_chars <- strsplit(words[[1]], "")[[1]]
  
  # Find the intersection of all lists
  for (i in 2:length(words)) {
    word_chars <- strsplit(words[[i]], "")[[1]]
    common_chars <- intersect(common_chars, word_chars)
  }
  
  common_chars
}

# Main code
words <- readLines(con = "stdin")
common_chars <- get_common_characters(words)

# Sort and print the characters in alphabetical order without spaces
cat(sort(common_chars, decreasing = FALSE), sep = "")
