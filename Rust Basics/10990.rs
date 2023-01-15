use std::io;

fn f(n: i32, i: i32) {
    for _ in 0..n-i-1 {
        print!(" ");
    }
    print!("*");
    for _ in 0..2*i-1 {
        print!(" ");
    }
    print!("*");
    println!();
}

fn main(){
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("");
    let n: i32 = s.trim().parse().unwrap();
    for _ in 0..n-1 {
        print!(" ");
    }
    print!("*\n");
    for i in 1..n {
        f(n, i);
    }
}