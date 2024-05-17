open System
open System.IO
open System.Text.RegularExpressions

let sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()))
let sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()))


let rec lookup k = function
| [] -> None
| (k', v) :: t -> if k = k' then Some v else lookup k t

type flag =
| Normal
| Abnormal
| Custom of string

type inRange = float -> bool

type reftab = string * (string * (flag * inRange) list)

let l1 = String.replicate 75 "-"
let l2 = String.replicate 80 "="

let parseRange (s: string) : inRange =
    let trimBrackets (s: string) = s.Trim([|'['; ']'; '('; ')'|])
    let removeWhitespace (s: string) = Regex.Replace(s, @"\s+", "")

    let parseBounds (s: string) (leftInclusive: bool) (rightInclusive: bool) =
        let parts = s.Split([|','|], StringSplitOptions.RemoveEmptyEntries)
        if parts.Length = 2 then
            let lower = float parts.[0]
            let upper = float parts.[1]
            fun x -> 
                (if leftInclusive then lower <= x else lower < x) &&
                (if rightInclusive then x <= upper else x < upper)
        else
            failwith "Invalid range format"
    
    match s with
    | _ when s.Contains(" ") && not (Seq.exists (fun c -> s.Contains(c.ToString())) ['('; '['; ')'; ']'; '>'; '<'; '='; '~']) ->
        let parts = s.Split([|' '|], StringSplitOptions.RemoveEmptyEntries)
        if parts.Length = 2 then
            let lower = float parts.[0]
            let upper = float parts.[1]
            fun x -> lower <= x && x <= upper
        else
            let p = parts.[0]
            if p.[1] <> '=' then
                if p.[0] = '<' then
                    fun x -> x < (float p.[1..])
                else
                    fun x -> x > (float p.[1..])
            else
                if p.[0] = '<' then
                    fun x -> x <= (float p.[2..])
                else
                    fun x -> x >= (float p.[2..])
    | _ ->
        let cleaned = removeWhitespace s
        match cleaned with
        | _ when cleaned.Contains("~") ->
            let parts = cleaned.Split([|'~'|], StringSplitOptions.RemoveEmptyEntries)
            if parts.Length = 2 then
                let lower = float parts.[0]
                let upper = float parts.[1]
                fun x -> lower <= x && x <= upper
            else
                failwith "Invalid range format"
        | _ when cleaned.StartsWith("[") && cleaned.EndsWith("]") ->
            parseBounds (trimBrackets cleaned) true true
        | _ when cleaned.StartsWith("[") && cleaned.EndsWith(")") ->
            parseBounds (trimBrackets cleaned) true false
        | _ when cleaned.StartsWith("(") && cleaned.EndsWith("]") ->
            parseBounds (trimBrackets cleaned) false true
        | _ when cleaned.StartsWith("(") && cleaned.EndsWith(")") ->
            parseBounds (trimBrackets cleaned) false false
        | _ when cleaned.StartsWith("<=") ->
            let value = float (cleaned.[2..])
            fun x -> x <= value
        | _ when cleaned.StartsWith("<") ->
            let value = float (cleaned.[1..])
            fun x -> x < value
        | _ when cleaned.StartsWith(">=") ->
            let value = float (cleaned.[2..])
            fun x -> x >= value
        | _ when cleaned.StartsWith(">") ->
            let value = float (cleaned.[1..])
            fun x -> x > value
        | _ -> failwith "Invalid format"
    

let get_reftab () : (reftab * bool) =
    let name = sr.ReadLine()
    let unit = sr.ReadLine()
    let rec get_classif (acc: (flag * inRange) list) (c: bool) : ((flag * inRange) list * bool) =
        let inp = sr.ReadLine()
        if inp = l1 then (acc, true)
        else if inp = l2 then (acc, false)
        else
            let ir : inRange = parseRange inp
            let s = sr.ReadLine()
            if s = l1 then ([(Normal, ir)], true)
            else if s = l2 then ([(Normal, ir)], false)
            else (((if s = "  Normal" then Normal else Custom s.[2..]), ir) :: acc, c) ||> get_classif
    let r, c = get_classif [] true
    ((name, (unit, r)), c)

let rec get_reftabs acc : reftab list =
    let r, c = get_reftab ()
    if c then  r :: acc |> get_reftabs
    else r :: acc

let ext (s : string) : string * string * float =
    let pattern = @"(.*?)(-?\d+(\.\d+)?)$"
    let m = Regex.Match(s, pattern)
    if m.Success then
        let textPart = m.Groups.[1].Value.Trim()
        let valstring = m.Groups.[2].Value
        let numberPart = float valstring
        (textPart, valstring, numberPart)
    else
        failwith "invalid format"


let main () =
    
    let reftabs = get_reftabs []
    let rec report () : unit =
        
        let inp = sr.ReadLine()
        if inp = null then () else
        sw.WriteLine(inp)
        sw.WriteLine(l1)
        sw.WriteLine("Test                      Result  Unit            Flag                     ")
        sw.WriteLine(l1)
        
        let rec loop () =
            let s = sr.ReadLine()
            
            if s = l2 then
                sw.WriteLine(l1)
                sw.WriteLine(l2)
                report ()
            
            else
                let n, sv, v = ext s
                match lookup n reftabs with
                | None -> failwith "..."
                | Some (u, x) ->
                    let rec desig (fir : (flag * inRange) list) =
                        match fir with
                        | [] -> Abnormal
                        | (f, ir) :: t ->
                            if ir v then f
                            else desig t
                    
                    let len1 = n.Length
                    let len2 = sv.Length
                    let len3 = u.Length
                    let f =
                        match desig x with
                        | Normal -> ""
                        | Abnormal -> "Abnormal"
                        | Custom z -> z
                    let len4 = f.Length
                    
                    sw.Write(n)
                    sw.Write(String.replicate (26 - len1) " ")
                    sw.Write(sv)
                    sw.Write(String.replicate (8 - len2) " ")
                    sw.Write(u)
                    sw.Write(String.replicate (16 - len3) " ")
                    sw.Write(f)
                    sw.WriteLine(String.replicate (25 - len4) " ")

                    loop ()
        
        loop ()
    
    report ()


let () = main ()

sr.Close()
sw.Close()
