Scanf.scanf "%d\n%s\n" @@ fun n s ->
  let comp k =
    let rec f acc x =
      if x = k then acc = 1 else
        f (acc + if s.[x] <> s.[n - k + x] then 1 else 0) @@ x + 1
    in f 0 0 in
  let rec f x =
    if x = n then false else
      if comp x then true else f @@ x + 1 in
  print_endline @@ if f 1 then "YES" else "NO"
