use std::io;

fn s(a: &str, k: i32){
    for _ in 0..k {
        print!("{a}");
    }
}

fn f(n: i32, i: i32) {
    s("* ", i);
    s("*", 4*(n-i)-3);
    s(" *", i);
    println!();
}

fn g(n: i32, i: i32) {
    s("* ", i);
    s(" ", 4*(n-i)-3);
    s(" *", i);
    println!();
}

fn main(){
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("");
    let n: i32 = s.trim().parse().unwrap();
    for i in 0..n-1 {
        f(n, i);
        g(n, i+1);
    }
    f(n, n-1);
    for i in (0..n-1).rev() {
        g(n, i+1);
        f(n, i);
    }
}