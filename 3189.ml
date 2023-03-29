Scanf.scanf "%d %d %d\n" @@ fun a b c ->
  let rec f x =
    if x < 10 then 10
    else 10*(f @@ x/10) in
  let t = f c in
  let rec find e = function
  | [] -> false
  | h :: t -> if e = h then true else find e t in
  let rec loop cnt x lst =
    let z = loop (cnt + 1) @@ b*x mod t in
    if find x lst then -1
    else if x <> c then z @@ x :: lst
    else if cnt = 0 then z lst
    else cnt in
  let ans = loop 0 a [] in
  if ans = -1 then print_string "NIKAD" else print_int ans
