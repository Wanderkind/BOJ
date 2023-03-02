let rec f _ = let p = print_char in match read_int() with 0 -> () | x -> for i = 1 to x do for j = 1 to i do p '*' done; p '\n' done; f() in f ();;
