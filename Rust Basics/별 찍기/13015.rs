use std::io;

fn s(a: &str, k: i32){
    for _ in 0..k {
        print!("{a}");
    }
}

fn f(n: i32) {
    s("*", n);
    s(" ", 2*n-3);
    s("*", n);
    println!();
}

fn g(n: i32, i: i32) {
    s(" ", i);
    print!("*");
    s(" ", n-2);
    print!("*");
    s(" ", 2*(n-i)-3);
    print!("*");
    s(" ", n-2);
    print!("*");
    println!();
}

fn main(){
    let mut z = String::new();
    io::stdin().read_line(&mut z).expect("");
    let n: i32 = z.trim().parse().unwrap();
    f(n);
    for i in 1..n-1 {
        g(n, i);
    }
    s(" ", n-1);
    print!("*");
    s(" ", n-2);
    print!("*");
    s(" ", n-2);
    print!("*");
    println!();
    for i in (1..n-1).rev() {
        g(n, i);
    }
    f(n);
}