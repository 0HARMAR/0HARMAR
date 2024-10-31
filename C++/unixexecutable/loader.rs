use std::fs::{read, File};
use std::io::{self,Read};

fn print_hex_dump(data: &[u8]) {
    for (i, byte) in data.iter().enumerate() {
        print!("{:02x} ", byte);
        if (i + 1) % 16 == 0 {
            println!();
        }
    }
    println!();
}

fn readtext(filename :String,text :&mut Vec<u8>){
    let mut file = File::open(filename)?;
    
    file.seek(SeekF)
}