use std::io;
use std::cmp;

fn s(a: &str, k: i32){
    for _ in 0..k {
        print!("{a}");
    }
}

fn d(n: i32, i: i32) {
    s("* ", i);
    s("*", cmp::min(4*(n-i)-1, 4*n-3));
    s(" *", i-1);
    println!();
}

fn e(n: i32, i: i32) {
    if i == 0 {
        print!("*");
    }
    else if i == n-1 {
        s("* ", 2*n-2);
        print!("*");
    }
    else {
        s("* ", i+1);
        s(" ", 4*(n-i)-5);
        s(" *", i);
    }
    println!();
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
    if n == 1 {
        print!("*");
    }
    else {
        for i in 0..n {
            d(n, i);
            e(n, i);
        }
        f(n, n-1);
        for i in (0..n-1).rev() {
            g(n, i+1);
            f(n, i);
        }
    }
    
}