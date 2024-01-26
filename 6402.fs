open System
open System.IO

let sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()))
let sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()))

let (|Prefix|_|) (p: string) (s: string) : string option =
    if s.StartsWith(p) then
        Some (s.Substring(p.Length))
    else
        None

type command = Trade | Cheat | Null
type memory = ((command * command) -> command) * ((command * command) * (command * command) -> (command * command))
type statement =
| Command of command
| Ifstat of ifstat
and ifstat = condition * statement * statement
and condition =
| Cond of cond
| Joint of (bool -> bool -> bool) * cond * condition
and cond = memory * (command -> command -> bool) * command
type program = statement


let pairstraight (b: bool) (x, y) = if b then (x, y) else (y, x)

let rec getSubject (info: string) : (((command * command) -> command) * string) =
    match info with
    | Prefix "MY" rest -> (fst, rest)
    | Prefix "YOUR" rest -> (snd, rest)
    | Prefix " " rest -> getSubject rest
    | _ -> failwith "..."

let rec getPairPick (info: string) : (((command * command) * (command * command) -> (command * command)) * string) =
    match info with
    | Prefix "1" rest -> (snd, rest)
    | Prefix "2" rest -> (fst, rest)
    | Prefix "LAST" rest -> getPairPick rest
    | Prefix " " rest -> getPairPick rest
    | _ -> failwith "..."

let getMemory (info: string) : (memory * string) =
    let subj, tail1 = getSubject info
    let n, tail2 = getPairPick tail1
    ((subj, n), tail2)

let rec getEq (info: string) : ((command -> command -> bool) * string) =
    match info with
    | Prefix "=" rest -> (( = ), rest)
    | Prefix "#" rest -> (( <> ), rest)
    | Prefix " " rest -> getEq rest
    | _ -> failwith "..."

let rec getCommand (info: string) : (command * string) =
    match info with
    | Prefix "TRADE" rest -> (Trade, rest)
    | Prefix "CHEAT" rest -> (Cheat, rest)
    | Prefix "NULL" rest -> (Null, rest)
    | Prefix " " rest -> getCommand rest
    | _ -> failwith "..."

let getCond (info: string) : (cond * string) =
    let mem, tail1 = getMemory info
    let eq, tail2 = getEq tail1
    let com, tail3 = getCommand tail2
    ((mem, eq, com), tail3)

let rec getCondition (info: string) : (condition * string) =
    let c, tail = getCond info
    let rec joint = function
    | Prefix " " rest -> joint rest
    | Prefix "AND" rest -> let a, b = getCondition rest in (Joint (( && ), c, a), b)
    | Prefix "OR" rest -> let a, b = getCondition rest in (Joint (( || ), c, a), b)
    | _ -> (Cond c, tail)
    joint tail

let rec getIfstat (info: string) : (ifstat * string) =
    let c, tail1 = getCondition info
    let s1, tail2 = getStatement tail1
    let s2, tail3 = getStatement tail2
    ((c, s1, s2), tail3)

and getStatement (info: string) : (statement * string) =
    match info with
    | Prefix "TRADE" rest -> (Command Trade, rest)
    | Prefix "CHEAT" rest -> (Command Cheat, rest)
    | Prefix "IF" rest -> getStatement rest
    | Prefix "THEN" rest -> getStatement rest
    | Prefix "ELSE" rest -> getStatement rest
    | Prefix " " rest -> getStatement rest
    | _ -> let a, b = getIfstat info in (Ifstat a, b)

let rec getPrograms (acc: program list) (info: string) : program list =
    if info = "" then acc |> List.rev else
    let s, tail = getStatement info
    match tail with
    | Prefix " " rest  -> getPrograms acc rest
    | Prefix "." rest  -> getPrograms (s :: acc) rest
    | _ -> failwith "..."

let rec append (acc: string) : string =
    let line = sr.ReadLine()
    match line with "#" -> acc | _ -> append (acc + line)

let point (pair: command * command) : int * int =
    match pair with
    | (Trade, Trade) -> ( 1,  1)
    | (Trade, Cheat) -> (-2,  2)
    | (Cheat, Trade) -> ( 2, -2)
    | (Cheat, Cheat) -> (-1, -1)
    | _ -> failwith "..."

let encounter_10 (p1: program) (p2: program) : int * int =
    let rec p2f (cpp: (command * command) * (command * command)) x1 x2 cnt : int * int =
        if cnt = 10 then (x1, x2) else
        let rec s2f (isp1: bool) = function
        | Command cmd -> cmd
        | Ifstat (ct, s1, s2) ->
            let rec condition_interpret (c: condition) : bool =
                match c with
                | Cond ((subj, n), eq, cmd) ->
                    cpp |> n |> pairstraight isp1 |> subj |> eq cmd
                | Joint (op, ((subj, n), eq, cmd), cndt) ->
                    let b = cpp |> n |> pairstraight isp1 |> subj |> eq cmd
                    cndt |> condition_interpret |> op b
            if condition_interpret ct then s2f isp1 s1 else s2f isp1 s2
        let cpair = s2f true p1, s2f false p2
        let u, v = point cpair
        p2f (snd cpp, cpair) <||| (x1 + u, x2 + v, cnt + 1)
    p2f ((Null, Null), (Null, Null)) 0 0 0

let simulate (lst: program list) : unit =
    let len = lst.Length
    let rec build (acc: Map<int, int>) ind =
        if ind = len then acc
        else (acc.Add (ind, 0), ind + 1) ||> build
    let rec game (scrs: Map<int, int>) (i: int) : Map<int, int> =
        if i = len - 1 then scrs else
        let pi = lst[i]
        let rec one (s: Map<int, int>) (acc: int) (j: int) : Map<int, int> =
            let change enc = function
            | Some z -> Some (z + enc)
            | None -> None
            if j = len then game <|| (s.Change (i, change acc), i + 1) else
            let u, v = encounter_10 pi lst[j]
            one <||| (s.Change (j, change v), acc + u, j + 1)
        one scrs 0 <| i + 1
    let pairs = game <|| ((Map [], 0) ||> build, 0)
    pairs.Values |> Seq.iter (fun x -> Console.WriteLine("{0,3}", x))

let main _ : unit = append "" |> getPrograms [] |> simulate

main ()

sr.Close()
sw.Close()
