use std::io;
use std::cmp;


fn main() {
    let mut s = String::new();

    io::stdin().read_line(&mut s).unwrap();
    let values:Vec<i64> = s
        .as_mut_str()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    
    let n = values[0];
    let m = values[1];

    let k = cmp::min(n, m) - 1;
    let x = k/2;
    let y = x + k%2;

    if k%2 == 1 {
        print!("{} {}", x, y);
    }
    else {
        let z = y + cmp::max(n, m) - 1 - k;
        if n < m {
            print!("{} {}", y, z);
        }
        else {
            print!("{} {}", z, y);
        }
    }
}
