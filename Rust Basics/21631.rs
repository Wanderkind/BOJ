use std::io;

fn main() {
    let mut s = String::new();

    io::stdin().read_line(&mut s).unwrap();
    let values:Vec<i64> = s
        .as_mut_str()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    
    let a = values[0];
    let b = values[1];

    if a >= b-1 {
        print!("{}", b);
    }
    else {
        print!("{}", a+1);
    }
}
