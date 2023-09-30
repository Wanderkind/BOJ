type expr =
| Var of char
| Null
;;

type 'a tree =
| Leaf
| Node of 'a node

and 'a node = {
  value: expr;
  negate: bool;
  precedence: int;
  left: 'a tree;
  right: 'a tree
};;

let sapling p = Node {
  value = Null;
  negate = false;
  precedence = p;
  left = Leaf;
  right = Leaf
};;

let isvar c =
  let n = Char.code c in
  96 < n && n < 123
;;

let binop = function '&' -> 1 | '^' -> 2 | '|' -> 3 | _ -> 0
;;

let rec parse (complete : bool) (prc : int) (neg : bool) (negstack : int list) (charlist : char list) (tree: 'a tree) =
  match charlist with
  | [] -> ([], tree)
  | c :: tail -> (
    if isvar c then ( if complete then (charlist, tree) else
      let rec f x = match x with Node xn -> (match xn.right with
      | Node node -> Node {xn with right = f xn.right}
      | _ ->  Node {xn with value = Var c; negate = neg}
      ) | _ -> assert false
      in let newtree = f tree in
      parse (prc = 3) prc false negstack tail newtree
    ) else match c with
    | '(' -> ( if complete then (charlist, tree) else
      let rec f x = match x with Node xn -> (match xn.right with
      | Node node -> Node {xn with right = f xn.right}
      | _ -> Node {xn with precedence = prc + 4}
      ) | _ -> assert false
      in let newtree = f tree in
      parse false (prc + 4) neg negstack tail newtree)
    | ')' -> ( let newcomplete = prc = 7 in
      match negstack with
      | [] -> parse newcomplete (prc - 4) neg [] tail tree
      | ns :: stacktail -> (
        if ns = prc then (
          let rec f x = match x with Node xn -> ( let xp = xn.precedence in
            if xp <= ns - 4 then Node {xn with right = f xn.right}
            else Node {xn with negate = not xn.negate}
          ) | _ -> assert false
          in let newtree = f tree in
          parse newcomplete (prc - 4) neg stacktail tail newtree)
        else parse newcomplete (prc - 4) neg negstack tail tree))
    | '~' -> ( if complete then (charlist, tree) else
      let rec f ng cl = match cl with
      | [] -> assert false
      | h :: t -> (
        if h = '~' then f (not ng) t
        else (ng, cl)
      ) in let (newneg, newcharlist) = f (not neg) tail in
      match newcharlist with [] -> assert false | h :: t -> (
        if newneg && h = '(' then parse false prc false ((prc + 4) :: negstack) newcharlist tree
        else parse false prc newneg negstack newcharlist tree))
    | _ -> let b = binop c in match b with
      | 0 -> parse complete prc neg negstack tail tree
      | _ -> ( let k = prc - b in
        let rec f x = match x with Node xn -> (
          if k <= xn.precedence then Node {
            value = Var c; negate = false; precedence = k; left = x; right = sapling prc}
          else Node {xn with right = f xn.right}
        ) | _ -> assert false
        in let newtree = f tree in
        parse false prc neg negstack tail newtree)
);;

let init charlst =
  parse false 3 false [] charlst @@ sapling 3
;;

let explode s = s |> String.to_seq |> List.of_seq
;;

let rec getvar acc = function
| [] -> acc
| h :: t -> (
  if isvar h && not @@ List.mem h acc then getvar (acc @ [h]) t
  else getvar acc t
);;

let rec product = function
| 0 -> [0]
| x -> (
  let rec f acc = function
  | [] -> acc
  | h :: t -> f (acc @ [2*h; 2*h + 1]) t in
  f [] @@ product @@ x - 1
);;

let rec getindex lst item = match lst with
| [] -> 0
| h :: t -> if item = h then 1 else 2 * getindex t item
;;

let setsubtract large small =
  let rec f acc b a = match a with
  | [] -> acc
  | h :: t -> ( match b with
    | [] -> acc @ a
    | h' :: t' -> (
      if h <> h' then f (acc @ [h]) b t
      else f acc t' t)
  ) in f [] small large
;;

let sol z =
  let l = explode @@ read_line () in
  let variables = getvar [] l in
  let ln = List.length variables in
  let leftovers, tree1 = init l in
  let tree2 = snd @@ init leftovers in
  let p0, p1 = product ln, product @@ ln - 1 in
  let rec logic = function
  | Leaf -> assert false
  | Node node -> ( match node.right with
    | Leaf -> ( match node.value with Null -> assert false | Var c ->
      let k = getindex variables c in
      let alter x = x mod k + (if node.negate then 0 else k) + 2*k*(x/k) in
      let rec newtable acc = function
      | [] -> acc
      | h :: t -> newtable (acc @ [alter h]) t
      in newtable [] p1)
    | _ -> (let a, b = logic node.left, logic node.right in
      match node.value with
      | Var '&' -> (
        let rec f acc p q = match q with
        | [] -> acc
        | h :: t -> ( match p with
          | [] -> acc
          | h' :: t' -> (
            if h = h' then f (acc @ [h]) t' t
            else if h' < h then f acc t' q else f acc p t
        )) in let res = f [] a b in
        if node.negate then setsubtract p0 res else res)
      | Var '^' -> (
        let rec f acc p q = match q with
        | [] -> acc @ p
        | h :: t -> ( match p with
          | [] -> acc @ q
          | h' :: t' -> (
            if h = h' then f acc t' t
            else if h' < h then f (acc @ [h']) t' q else f (acc @ [h]) p t
        )) in let res = f [] a b in
        if node.negate then setsubtract p0 res else res)
      | Var '|' -> (
        let rec f acc p q = match q with
        | [] -> acc @ p
        | h :: t -> ( match p with
          | [] -> acc @ q
          | h' :: t' -> (
            if h = h' then f (acc @ [h]) t' t
            else if h' < h then f (acc @ [h']) t' q else f (acc @ [h]) p t
        )) in let res = f [] a b in
        if node.negate then setsubtract p0 res else res)
      | _ -> assert false
    )) in Printf.printf "Data set %d: %s\n" z @@ (
      if logic tree1 = logic tree2 then "Equivalent" else "Different"
);;

for z = 1 to read_int () do sol z done
;;
