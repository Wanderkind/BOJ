open Scanf
open Printf
;;
let a _ =
    for j = 1 to read_int() do
        printf "="
    done
;;
for i = 1 to read_int() do
    a();
    printf "\n"
done
