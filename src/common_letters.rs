use std::collections::HashSet;
use std::io::{self, BufRead};

fn common_letters(words: Vec<String>) -> String {
    if words.is_empty() {
        return String::new();
    }

    let mut common: HashSet<char> = words[0].chars().collect();
    for word in words.iter().skip(1) {
        let word_set: HashSet<char> = word.chars().collect();
        common = common.intersection(&word_set).cloned().collect();
    }

    let mut result: Vec<char> = common.into_iter().collect();
    result.sort();
    result.into_iter().collect()
}

fn main() {
    let stdin = io::stdin();
    let words: Vec<String> = stdin.lock().lines().filter_map(|line| line.ok()).collect();
    
    let result = common_letters(words);
    println!("{}", result);
}