open System
open System.IO
open System.Text.RegularExpressions

let sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()))
let sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()))


let tl (x: string) = x.ToLower()

let rtna (x: string) : string =
    let rec findEndIndex i =
        if i < 0 || Char.IsLetter(x[i]) then i
        else findEndIndex (i - 1) 
    if String.IsNullOrEmpty(x) then x
    else
        let endIndex = findEndIndex (x.Length - 1)
        x.Substring(0, endIndex + 1)

let rq x = Regex.Replace(x, "qu", "q")

let ry x = Regex.Replace(x, "y(?=[aeiou])", "t")

let isv (c: char) = "aeiou".Contains(c)

let isc (c: char) = not ("aeiou".Contains(c))

let re (x: string) : string =
    let len = x.Length
    if x.EndsWith("es") then
        if len > 3 && isc x[len - 3] && isc x[len - 4] then x
        else x.Substring(0, max 1 <| len - 2)
    else if x.EndsWith("e") then
        if len > 2 && x[len - 2] = 'l' && isc x[len - 3] then x
        else x.Substring(0, max 1 <| len - 1)
    else x

let syl (word: string) : int =
    let w = word |> tl |> rtna |> rq |> ry |> re
    let rec dec (acc: int) (v: bool) (x: string) =
        if x = "" then max 1 acc else
        if isv x[0] && not v then dec (acc + 1) true x[1..]
        else if isc x[0] && v then dec acc false x[1..]
        else dec acc v x[1..]
    dec 0 false w

let haiku (ln: string) : unit =
    let l = ln.Split ' ' |> Array.toList
    let rec fil (lst: string list) (aim: int) (cur: int) = function
    | [] -> (lst, aim, cur, [])
    | h :: t ->
        let s = cur + syl h
        if s >= aim then (lst @ [h], aim, s, t)
        else fil (lst @ [h]) aim s t
    let l1a, l1b, l1c, l1d = fil [] 5 0 l
    if l1b <> l1c then sw.WriteLine(ln) else
    let l2a, l2b, l2c, l2d = fil [] 7 0 l1d
    if l2b <> l2c then sw.WriteLine(ln) else
    let l3a, l3b, l3c, l3d = fil [] 5 0 l2d
    match l3d with
    | [] ->
        if l3b <> l3c then sw.WriteLine(ln)
        else
            String.Join(" ", l1a) |> sw.WriteLine
            String.Join(" ", l2a) |> sw.WriteLine
            String.Join(" ", l3a) |> sw.WriteLine
    | _ -> sw.WriteLine(ln)

let main () =
    let rec exec () =
        let inp = sr.ReadLine()
        if inp = null then
            ()
        else
            haiku inp;
            exec ()
    exec ()

let () = main ()


sr.Close()
sw.Close()
