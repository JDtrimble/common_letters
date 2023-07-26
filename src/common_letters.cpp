#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

string common_letters(const vector<string>& words) {
    if (words.empty()) {
        return "";
    }

    string common = words[0];
    for (int i = 1; i < words.size(); ++i) {
        string word = words[i];
        sort(common.begin(), common.end());
        sort(word.begin(), word.end());
        string temp;
        set_intersection(common.begin(), common.end(), word.begin(), word.end(), back_inserter(temp));
        common = temp;
    }

    return common;
}

int main() {
    vector<string> words;
    string word;
    while (cin >> word) {
        words.push_back(word);
    }

    string result = common_letters(words);
    cout << result << endl;

    return 0;
}
