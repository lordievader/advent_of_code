use std::fs::File;
use std::io::{self, prelude::*, BufReader};
use std::time::Instant;
use std::collections::HashSet;

fn read_input(input_filename: &str) -> Result<Vec<i32>, io::Error> {
    let file = File::open(input_filename)?;
    let reader = BufReader::new(file);
    let mut frequencies: Vec<i32> = Vec::new();
    for line in reader.lines() {
        frequencies.push(line.unwrap().parse::<i32>().unwrap());
    }
    Ok(frequencies)
}

fn part_1(frequencies: &Vec<i32>) {
    println!("{}", frequencies.into_iter().sum::<i32>());
}

fn part_2(frequencies: &Vec<i32>) {
    let length: usize = frequencies.len();
    // let mut past: Vec<i32> = Vec::new();
    let mut past = HashSet::new();
    let mut current_frequency:i32 = 0;
    let mut index = 0;
    while !past.contains(&current_frequency) {
        past.insert(current_frequency);
        current_frequency += frequencies[index % length];
        index = (index + 1) % length;
    }
    println!("{:?}", current_frequency);
}

fn main() -> io::Result<()> {
    let start = Instant::now();
    // let input_file = "test.txt";
    let input_file = "input.txt";
    let input = read_input(input_file).unwrap();
    part_1(&input);
    part_2(&input);
    let duration = start.elapsed();
    println!("Time elapsed in expensive_function() is: {:?}", duration);
    Ok(())
}