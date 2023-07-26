program CommonLetters;
uses SysUtils;
var
  words: array[1..1000] of string[100];
  common: array['a'..'z'] of boolean;
  i, j, n: integer;
  c: char;
begin
  i := 1;
  while not eof do
  begin
    readln(words[i]);
    inc(i);
  end;
  n := i - 1;

  for c := 'a' to 'z' do
    common[c] := true;

  for c := 'a' to 'z' do
    for i := 1 to n do
      if pos(c, words[i]) = 0 then
        common[c] := false;

  for c := 'a' to 'z' do
    if common[c] then
      write(c);
end.
