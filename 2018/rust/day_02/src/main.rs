use std::collections::HashSet;
mod read_input;
mod timing;

fn count(character: char, line: &String) -> i32 {
    line.matches(character).count() as i32
}

fn process_id(id: &String) -> (bool, bool) {
    let mut past = HashSet::new();
    let mut two = false;
    let mut three = false;
    for character in id.chars() {
        if past.contains(&character) {
            continue;
        }
        let number = count(character, id);
        match number {
            2 => two = true,
            3 => three = true,
            _ => (),
        }
        past.insert(character);
    }
    (two, three)
}

fn part_1(input: &Vec<String>) -> i32 {
    let mut count_two = 0;
    let mut count_three = 0;
    for line in input {
        let (two, three) = process_id(&line);
        if two {
            count_two += 1;
        }
        if three {
            count_three += 1;
        }
    }
    count_two * count_three
}

fn char_diff(input: &String, compare: &String) -> i32 {
    let mut count = 0;
    let compare_chars: Vec<char> = compare.chars().collect();
    for (i, c) in input.char_indices() {
        if c != compare_chars[i] {
            count += 1;
        }
    }
    count
}

fn find_ids(input: &Vec<String>) -> (&String, &String) {
    let mut found = false;
    let mut index_i = 0;
    let mut index_j = 0;
    for (i, item_a) in input.iter().enumerate() {
        for (j, item_b) in input[i..].iter().enumerate() {
            let diff_count = char_diff(item_a, item_b);
            if diff_count == 1 {
                index_i = i;
                index_j = i + j;
                found = true;
                break
            }
        }
        if found {
            break
        }
    }
    (&input[index_i], &input[index_j])
}

fn strip_chars(input_a: &String, input_b: &String) -> String {
    let mut output = String::new();
    let compare_chars: Vec<char> = input_b.chars().collect();
    for (i, item_a) in input_a.char_indices() {
        if item_a == compare_chars[i] {
            output.push(item_a);
        }
    }
    output
}

fn part_2(input: &Vec<String>) -> String {
    let (id_a, id_b) = find_ids(&input);
    strip_chars(id_a, id_b)
}

fn main (){
    let input = read_input::read_lines("input.txt").unwrap();
    let start_part_1 = timing::start();
    let part_1_answer = part_1(&input);
    timing::stop(start_part_1);
    println!("Part 1 answer: {}", part_1_answer);

    let start_part_2 = timing::start();
    let part_2_answer = part_2(&input);
    timing::stop(start_part_2);
    println!("Part 2 answer: {}", part_2_answer);
}

mod tests {
    use super::*;

    #[test]
    fn test_count() {
        assert_eq!(count('a', &String::from("hello")), 0);
        assert_eq!(count('a', &String::from("aoc")), 1);
    }

    #[test]
    fn test_process_id() {
        assert_eq!(process_id(&String::from("abcdef")), (false, false));
        assert_eq!(process_id(&String::from("bababc")), (true, true));
        assert_eq!(process_id(&String::from("abbcde")), (true, false));
        assert_eq!(process_id(&String::from("abcccd")), (false, true));
    }

    #[test]
    fn test_part_1(){
        let input = read_input::read_lines("test.txt").unwrap();
        assert_eq!(part_1(&input), 12);
    }

    #[test]
    fn test_char_diff(){
        assert_eq!(char_diff(&String::from("abcde"), &String::from("axcye")), 2);
        assert_eq!(char_diff(&String::from("fghij"), &String::from("fguij")), 1);
    }

    #[test]
    fn test_find_ids(){
        let input = read_input::read_lines("test2.txt").unwrap();
        assert_eq!(find_ids(&input), (&String::from("fghij"), &String::from("fguij")));
    }

    #[test]
    fn test_strip_chars(){
        let input = read_input::read_lines("test2.txt").unwrap();
        let (input_a, input_b) = find_ids(&input);
        assert_eq!(strip_chars(input_a, input_b), String::from("fgij"));
    }

    #[test]
    fn test_part_2(){
        let input = read_input::read_lines("test2.txt").unwrap();
        assert_eq!(part_2(&input), String::from("fgij"));
    }
}