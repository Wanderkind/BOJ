use std::io;

fn main(){
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("");
    let n: i32 = s.trim().parse().unwrap();
    for i in 0..n {
        for _ in 0..=n-i-2 {
            print!(" ");
        }
        for _ in 1..=i+1 {
            print!("*");
        }
        println!();
    }
}