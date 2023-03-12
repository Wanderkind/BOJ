let bbun a t =
  let rec f round step howmany x =
    let turn = step = 0 || step = 2 || (3 < step && step < 5 + round) in
    if turn && howmany = 1 then x else
      if step = 5 + 2*round then f (round + 1) 0 howmany @@ (x + 1) mod a
      else f round (step + 1) (if turn then howmany - 1 else howmany) @@ (x + 1) mod a
  in f 1 0 t 0
;;
let degi a t =
  let rec f round step howmany x =
    let turn = step = 1 || step = 3 || 4 + round < step in
    if turn && howmany = 1 then x else
      if step = 5 + 2*round then f (round + 1) 0 (howmany - 1) @@ (x + 1) mod a
      else f round (step + 1) (if turn then howmany - 1 else howmany) @@ (x + 1) mod a
  in f 1 0 t 0
;;
let sol _ =
  Scanf.scanf "%d\n%d\n%d\n" @@ fun a t ask ->
    if ask = 0 then bbun a t |> print_int
    else degi a t |> print_int
;;
sol ()
;;
