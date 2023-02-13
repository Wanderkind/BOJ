let rec moo n =
  let rec len = function
  | -1 -> 0
  | x -> (len (x - 1))*2 + x + 3 in
  let rec s k =
    if n <= len k then k
    else s (k + 1) in
  let stage = s 0 in
  let newn = n - len (stage - 1) in
  if newn = 1 then 'm'
  else if newn <= stage + 3 then 'o'
  else moo (newn - stage - 3) in
read_int() |> moo |> print_char
