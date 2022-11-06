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

let s1 n =
    for i=1 to n do
        f n "@";
        f (3*n) " ";
        f n "@";
        f 1 "\n"
    done
;;

let s2 n =
    for i=1 to n do
        f n "@";
        f (2*n) " ";
        f n "@";
        f 1 "\n"
    done
;;

let s3 n =
    for i=1 to n do
        f (3*n) "@";
        f 1 "\n"
    done
;;

s1 n;s2 n;s3 n;s2 n;s1 n
;;
