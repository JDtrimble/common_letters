local function updateLetterCount(word, letterCount)
    for i = 1, #word do
        local ch = word:sub(i, i)
        if ch:match("%a") then
            letterCount[ch] = (letterCount[ch] or 0) + 1
        end
    end
end

local letterCount = {}
local numWords = 0

-- Read words from input
while true do
    local word = io.read()
    if not word then break end
    updateLetterCount(word, letterCount)
    numWords = numWords + 1
end

-- Print common letters in alphabetical order
for code = string.byte('a'), string.byte('z') do
    local ch = string.char(code)
    if letterCount[ch] == numWords then
        io.write(ch)
    end
end
io.write("\n")
