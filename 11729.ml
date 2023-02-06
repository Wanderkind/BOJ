let rec hanoi from into use = function
  | 1 -> Printf.printf "%d %d\n" from into
  | x -> hanoi from use into (x-1); Printf.printf "%d %d\n" from into; hanoi use into from (x-1);;
let n = read_int() in  Printf.printf "%d\n" (1 lsl n - 1); hanoi 1 3 2 n;;
