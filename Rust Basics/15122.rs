use std::io;

fn nozero(n: i32) -> bool {
    if n < 10 {
        true
    }
    else if n%10 == 0 {
        false
    }
    else {
        nozero(n/10)
    }
}

fn f(n: i32) -> i32 {
    if nozero(n) {n} else {f(n+1)}
}

fn main(){
    let mut z = String::new();
    io::stdin().read_line(&mut z).expect("");
    let n: i32 = z.trim().parse().unwrap();
    
    println!("{}", f(n+1));
}