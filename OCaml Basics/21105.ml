open Scanf
open Printf;;

for i = 1 to read_int() do
  scanf "%f %f\n" (fun p c-> printf "%f\n" (100.*.p/.(c+.100.)))
done
