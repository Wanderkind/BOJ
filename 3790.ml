let f _ = let n = read_int () in (n - 1)*(n - 1)/4 |> Printf.printf "%d\n" in for i = 1 to read_int () do f () done;;
