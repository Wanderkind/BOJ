open Int64;;
let sol _ =
  let lovely n =
    let rec f n =
    if n < 10L then sub 9L n
    else add(mul 10L (f @@ div n 10L)) @@ f @@ rem n 10L in
    mul n @@ f n in
    let rec d n =
      if n < 10L then 5L
      else mul (d @@ div n 10L) 10L in
      let n = read_int () |> of_int in
      let c = d n in
      (if n < c then n else c) |> lovely |> Printf.printf "%Ld\n";;
for i = 1 to read_int () do sol () done
