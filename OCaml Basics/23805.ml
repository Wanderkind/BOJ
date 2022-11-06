open Scanf
open Printf
;;
let n = read_int()
;;
let f n s =
    for j=1 to n do
        printf s
    done
;;

for i=1 to n do
    f n "@@@";
    f n " ";
    f n "@";
    printf "\n"
done
;;

for i=1 to 3*n do
    f n "@";
    f n " ";
    f n "@";
    f n " ";
    f n "@";
    printf "\n"
done
;;

for i=1 to n do
    f n "@";
    f n " ";
    f n "@@@";
    printf "\n"
done
;;
