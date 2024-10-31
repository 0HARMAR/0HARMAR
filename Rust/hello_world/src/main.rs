use std::fs::{read, File};
use std::io::{self,Read};

fn readfile(filename : &str) -> Result<Vec<u8>,io::Error>{
    let mut file = File::open(filename)?; // open file

    let mut content = Vec::new();

    file.read_to_end(&mut content)?;

    Ok(content)
}


fn main()  {
    match readfile("/mnt/Just-For-Fun/C++/unixexecutable/mini.ue"){
        Ok(bytes) => println!("file content : {}",bytes.len()),
        Err(e) => println!("error message : {}",e)
    }

    println!("main return");
}


fn add(a:i32,b:i32) -> i32{
    a+b
}

