open System
open System.IO

let sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()))
let sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()))


let ( %% ) (a: int64) (b: int64) : int64 = (a % b + abs(b)) % (abs b)

let rec gcd (a: int64) (b: int64) : int64 =
    let p, q = abs a, abs b
    if q = 0L then p
    else gcd q (p %% q)

type num =
| Zero
| Int of int64
| Frc of num * int64
| Add of num * num

let rec reducible (p: num) (q: num) : bool =
    match (p, q) with
    | (Zero, _) -> true
    | (_, Zero) -> true
    | (Int _, Int _) -> true
    | (Int _, Frc (Int _, _)) -> true
    | (Frc (Int _, _), Int _) -> true
    | (Frc (Int _, _), Frc (Int _, _)) -> true
    | (Add (a, b), _) -> reducible a q || reducible b q
    | (_, Add (a, b)) -> reducible a p || reducible b p
    | _ -> false

and intmul (x: int64) (y: num) : num =
    if x = 0L then Zero else
    match y with
    | Zero -> Zero
    | Int 0L -> Zero
    | Int a -> Int (x*a)
    | Frc (a, b) -> Frc (intmul x a, b) |> fracSanitize
    | Add (a, b) -> add (intmul x a) (intmul x b)

and negate (x: num) : num = intmul -1L x

and fracSanitize (x: num) : num =
    match x with
    | Frc (p, q) ->
        match (q: int64) with
        | 0L -> failwith "#### module Num: Frc (_, 0) generated. ####"
        | 1L -> p
        | _ ->
            if q < 0L then Frc (negate p, -q) |> fracSanitize else
            match (p: num) with
            | Zero -> Zero
            | Int a ->
                let g = gcd a q
                if g = q then Int (a/g)
                else Frc (Int (a/g), q/g)
            | Frc (a, b) -> Frc (a, b*q) |> fracSanitize
            | Add (a, b) -> add (Frc (a, q) |> fracSanitize) (Frc (b, q) |> fracSanitize) |> addSanitize
    | _ -> x

and reduce (lst: num list) : num list =
    let rec inner (acc: num list) = function
    | [] -> acc
    | h :: t ->
        let rec f (prot: num) (save: num list) = function
        | [] -> inner (prot :: acc) save
        | h' :: t' ->
            if reducible prot h' then f (add prot h' |> addSanitize) save t'
            else f prot (h' :: save) t'
        f h [] t
    inner [] lst

and addSanitize (y: num) : num =
    let rec g (x: num) : num list =
        match x with
        | Add (p, q) -> g p @ g q
        | _ -> [x]
    let redlst = g y |> reduce
    let rec maketree (acc: num) = function
    | [] -> acc
    | h :: t ->
        match (t: num list) with
        | [] -> Add (h, acc)
        | _ -> maketree (Add (h, acc)) t
    maketree (List.head redlst) (List.tail redlst)

and add (x: num) (y: num) : num =
    match (x, y) with
    | (Zero, _) -> y
    | (_, Zero) -> x
    | (Int a, Int b) -> if a + b = 0L then Zero else Int (a + b)
    | (Int a, Frc (b, c)) -> if reducible x b then Frc (add (Int (a*c)) b, c) |> fracSanitize else Add (x, y)
    | (Frc (a, b), Int c) -> if reducible a y then Frc (add (Int (c*b)) a, b) |> fracSanitize else Add (x, y)
    | (Frc (a, b), Frc (c, d)) -> if reducible a c then Frc (add (intmul d a) (intmul b c) |> addSanitize, b*d) |> fracSanitize else Add (x, y)
    | _ -> Add (x, y) |> addSanitize

and mul (x: num) (y: num) : num =
    match (x, y) with
    | (Zero, _) -> Zero
    | (_, Zero) -> Zero
    | (Int a, Int b) -> Int (a*b)
    | (Int a, Frc (b, c)) -> Frc (intmul a b, c) |> fracSanitize
    | (Frc (a, b), Int c) -> Frc (intmul c a, b) |> fracSanitize
    | (Frc (a, b), Frc (c, d)) -> Frc (mul a c, b*d) |> fracSanitize
    | (Add (a, b), _) -> Add (mul a y, mul b y) |> addSanitize
    | (_, Add (a, b)) -> Add (mul a x, mul b x) |> addSanitize

and isZero (x: num) : bool =
    match x with
    | Zero -> true
    | Int a -> a = 0L
    | Frc (a, _) -> isZero a
    | Add (a, b) -> negate a |> ( *= ) b

and ( *= ) (x: num) (y: num) : bool =
    match (x, y) with
    | (Zero, _) -> isZero y
    | (Int u, Int v) -> u = v
    | (Int _, Frc (_, _)) ->
        let v = fracSanitize y
        match v with
        | Frc (_, _) -> false
        | _ -> x *= v
    | (Int _, Add (_, _)) ->
        let v = addSanitize y
        match v with
        | Frc (_, _) -> false
        | _ -> x *= v
    | (Frc (_, _), Frc (_, _)) ->
        let u, v = fracSanitize x, fracSanitize y
        match (u, v) with
        | (Frc (a, b), Frc (c, d)) -> a = c && b = d
        | (_, Frc (_, _)) | (Frc (_, _), _) -> false
        | (_, _) -> u *= v
    | (Frc (_, _), Add (_, _)) ->
        let u, v = fracSanitize x, addSanitize y
        match (u, v) with
        | (Frc (_, _), Add (_, _)) -> false
        | (_, _) -> u *= v
    | (Add (_, _), Add (_, _)) ->
        let u, v = addSanitize x, addSanitize y
        match (u, v) with
        | (Add (a, b), Add (c, d)) -> (a = c && b = d) || (a = d && b = c)
        | (_, Add (_, _)) | (Add (_, _), _) -> false
        | (_, _) -> u *= v
    | _ -> y *= x // reduced for the sake of size, costs maybe an extra stack?

let rec div (x: num) (y: num) : num =
    match y with
    | Zero -> failwith "#### module Num: Division by Zero attempted. ####"
    | Int 0L -> failwith "#### module Num: Division by Int 0 attempted. ####"
    | Int a -> Frc (x, a) |> fracSanitize
    | Frc (a, b) -> div (intmul b x) a |> fracSanitize
    | Add (a, b) -> div (negate b |> add a |> addSanitize) (mul b b |> negate |> add (mul a a) |> addSanitize) |> fracSanitize |> mul x

let extract (input: string) : num * string =
    let zer = input[0] = '0'
    let neg = input[0] = '-'
    let inp = if neg then input[1..] else input
    let rec loop acc i =
        if i < inp.Length && Char.IsDigit(inp[i]) then
            loop (acc * 10 + int inp[i] - 48) (i + 1)
        else
            let coef =
                if zer then 0 else
                if acc = 0 then 1 else acc
            (if neg then -coef else coef), inp.Substring(i)
    let a, b = loop 0 0
    if a = 0 then (Zero, "") else
    (Int a, b)

let rec parse (l: string list) (right: bool) (a: num) (x: num) (y: num) : num * num * num =
    match l with
    | [] -> (a, x, y)
    | h :: t ->
        if h = "=" then
            parse t true a x y
        else if h = "+" then
            match t with
            | [] -> failwith "..."
            | h' :: t' ->
                let p, q = extract h'
                if right then
                    if q = "x" then parse t' true a (add (negate p) x) y else
                    if q = "y" then parse t' true a x (add (negate p) y)
                    else parse t' true (add (negate p) a) x y
                else
                    if q = "x" then parse t' false a (add p x) y else
                    if q = "y" then parse t' false a x (add p y)
                    else parse t' false (add p a) x y
        else if h = "-" then
            match t with
            | [] -> failwith "..."
            | h' :: t' ->
                let p, q = extract h'
                if right then
                    if q = "x" then parse t' true a (add p x) y else
                    if q = "y" then parse t' true a x (add p y)
                    else parse t' true (add p a) x y
                else
                    if q = "x" then parse t' false a (add (negate p) x) y else
                    if q = "y" then parse t' false a x (add (negate p) y)
                    else parse t' false (add (negate p) a) x y
        else
            let p, q = extract h
            if right then
                if q = "x" then parse t true a (add (negate p) x) y else
                if q = "y" then parse t true a x (add (negate p) y)
                else parse t true (add (negate p) a) x y
            else
                if q = "x" then parse t false a (add p x) y else
                if q = "y" then parse t false a x (add p y)
                else parse t false (add p a) x y

type shape =
| Slope of num * num * num // (a, x, y)
| Verti of num * num       // (a, x, 0)
| Horiz of num    *    num // (a, 0, y)
| Empty // (0, 0, 0)
| Impos // (a, 0, 0) where a <> 0

let conv (a, x, y) =
    match (a, x, y) with
    | (_, Int _, Int _) -> Slope (a, x, y)
    | (_, Int _, Zero) -> Verti (a, x)
    | (_, Zero, Int _) -> Horiz (a, y)
    | (Zero, Zero, Zero) -> Empty
    | (_, Zero, Zero) -> Impos
    | _ -> failwith "..."

type result =
| Good of num
| Bad

let print (r: result) : string =
    match r with
    | Bad -> "don't know"
    | Good Zero -> "0"
    | Good (Int x) -> $"{x}"
    | Good (Frc (Int x, y)) -> $"{x}/{y}"
    | _ -> failwith "..."

let exec () =
    let la = sr.ReadLine().Split() |> Array.toList
    let lb = sr.ReadLine().Split() |> Array.toList
    let ca = parse la false Zero Zero Zero |> conv
    let cb = parse lb false Zero Zero Zero |> conv
    let rx, ry =
        match (ca, cb) with
        | (Impos, _) -> (Bad, Bad)
        | (_, Impos) -> (Bad, Bad)
        | (Empty, Empty) -> (Bad, Bad)
        | (Empty, Verti (a, x)) -> (Good (div a x |> negate), Bad)
        | (Verti (a, x), Empty) -> (Good (div a x |> negate), Bad)
        | (Empty, Horiz (a, y)) -> (Bad, Good (div a y |> negate))
        | (Horiz (a, y), Empty) -> (Bad, Good (div a y |> negate))
        | (Empty, _) -> (Bad, Bad)
        | (_, Empty) -> (Bad, Bad)
        | (Slope (c1, a1, b1), Slope (c2, a2, b2)) ->
            if mul a1 b2 <> mul a2 b1 then
                let xx = div (mul b2 c1 |> negate |> add (mul b1 c2)) (mul b1 a2 |> negate |> add (mul b2 a1))
                let yy = div (mul a2 c1 |> negate |> add (mul a1 c2)) (mul a1 b2 |> negate |> add (mul a2 b1))
                (Good xx, Good yy)
            else (Bad, Bad)
        | (Verti (z, x), Slope (c, a, b)) ->
            let xx = div z x |> negate
            let yy = div (mul a xx |> add c) b |> negate
            (Good xx, Good yy)
        | (Slope (c, a, b), Verti (z, x)) ->
            let xx = div z x |> negate
            let yy = div (mul a xx |> add c) b |> negate
            (Good xx, Good yy)
        | (Horiz (z, y), Slope (c, a, b)) ->
            let yy = div z y |> negate
            let xx = div (mul b yy |> add c) a |> negate
            (Good xx, Good yy)
        | (Slope (c, a, b), Horiz (z, y)) ->
            let yy = div z y |> negate
            let xx = div (mul b yy |> add c) a |> negate
            (Good xx, Good yy)
        | (Verti (z, x), Horiz (w, y)) ->
            let xx = div z x |> negate
            let yy = div w y |> negate
            (Good xx, Good yy)
        | (Horiz (w, y), Verti (z, x)) ->
            let xx = div z x |> negate
            let yy = div w y |> negate
            (Good xx, Good yy)
        | (Verti (z1, x1), Verti (z2, x2)) ->
            let xx1 = div z1 x1 |> negate
            let xx2 = div z2 x2 |> negate
            if xx1 = xx2 then (Good xx1, Bad) else (Bad, Bad)
        | (Horiz (z1, y1), Horiz (z2, y2)) ->
            let yy1 = div z1 y1 |> negate
            let yy2 = div z2 y2 |> negate
            if yy1 = yy2 then (Bad, Good yy1) else (Bad, Bad)
    print rx |> sw.WriteLine
    print ry |> sw.WriteLine
    sr.ReadLine() |> sw.WriteLine

let main () =
    for _ = 1 to sr.ReadLine() |> int do
        exec ()
    done

let () = main ()


sr.Close()
sw.Close()
