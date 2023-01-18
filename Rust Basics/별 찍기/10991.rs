use std::io;

fn f(n: i32, i: i32) {
    for _ in 0..n-i {
        print!(" ");
    }
    for _ in 0..i {
        print!("* ");
    }
    println!();
}

fn main(){
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("");
    let n: i32 = s.trim().parse().unwrap();
    for i in 1..n+1 {
        f(n, i);
    }
}