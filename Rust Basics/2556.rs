use std::io;

fn f(n: i32) {
    for _ in 0..n {
        print!("*");
    }
    println!();
}

fn main(){
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("");
    let n: i32 = s.trim().parse().unwrap();
    for _ in 0..n {
        f(n);
    }
}