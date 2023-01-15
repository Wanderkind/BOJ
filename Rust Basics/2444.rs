use std::io;

fn f(n: i32, i: i32) {
    for _ in 0..=n-i-2 {
        print!(" ");
    }
    for _ in 0..=i*2 {
        print!("*");
    }
    println!();
}

fn main(){
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("");
    let n: i32 = s.trim().parse().unwrap();
    for i in 0..n {
        f(n, i);
    }
    for i in (0..n-1).rev(){
        f(n, i);
    }
}