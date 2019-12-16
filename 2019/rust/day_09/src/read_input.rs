use std::fs::File;
use std::io::{self, prelude::*, BufReader};

pub fn read_lines(input_filename: &str) -> Result<Vec<String>, io::Error> {
    let file = File::open(input_filename)?;
    let reader = BufReader::new(file);
    let mut lines: Vec<String> = Vec::new();
    for line in reader.lines() {
        lines.push(line.unwrap());
    }
    Ok(lines)
}