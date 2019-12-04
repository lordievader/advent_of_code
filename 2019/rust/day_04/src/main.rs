mod read_input;
mod timing;

fn correct(password: i32) -> bool {
    let digits: Vec<_> = password.to_string().chars().map(|d| d.to_digit(10).unwrap()).collect();
    let mut prev_digit = 0;
    let mut decreasing = false;
    let mut adjecent = false;
    for digit in digits.into_iter() {
        if decreasing == false && prev_digit > digit {
            decreasing = true;
        }
        if adjecent == false && prev_digit == digit {
            adjecent = true;
        }
        prev_digit = digit;
    }

    let verdict = !decreasing && adjecent;
    verdict
}

fn correct_v2(password: i32) -> bool {
    let digits: Vec<_> = password.to_string().chars().map(|d| d.to_digit(10).unwrap()).collect();
    let mut prev_digit = 0;
    let mut decreasing = false;
    let mut adjecent = false;
    let mut group_count = 0;
    let mut group_min_count = 0;
    for digit in digits.into_iter() {
        if decreasing == false && prev_digit > digit {
            decreasing = true;
        }
        if adjecent == false && prev_digit == digit {
            adjecent = true;
            group_count = 2;
        }
        else if adjecent == true && prev_digit == digit {
            group_count += 1;
        }
        else if adjecent == true && prev_digit != digit {
            adjecent = false;
            if group_count < group_min_count || group_min_count == 0 {
                group_min_count = group_count;
            }
        }
        prev_digit = digit;
    }
    if group_count < group_min_count || group_min_count == 0 {
        group_min_count = group_count;
    }
    if group_min_count == 2 {
        adjecent = true;
    }
    else {
        adjecent = false;
    }

    let verdict = !decreasing && adjecent;
    verdict
}

fn count_passwords(start: i32, end: i32) -> i32 {
    let mut count = 0;
    for password in start..end {
        if correct(password) {
            count += 1
        }
    }
    count
}

fn count_passwords_v2(start: i32, end: i32) -> i32 {
    let mut count = 0;
    for password in start..end {
        if correct_v2(password) {
            count += 1
        }
    }
    count
}


fn main() {
    // let test_input: Vec<i32> = read_input::read_lines("test.txt").unwrap().iter().map(|x| x.parse().unwrap()).collect();

    let start_part_1 = timing::start();
    let part_1_answer = count_passwords(372037, 905157);
    timing::stop(start_part_1);
    println!("Part 1 answer: {}", part_1_answer);

    let start_part_2 = timing::start();
    let part_2_answer = count_passwords_v2(372037, 905157);
    timing::stop(start_part_1);
    println!("Part 2 answer: {}", part_2_answer);
}

mod tests{
    use super::*;

    #[test]
    fn test_correct() {
        assert_eq!(correct(111111), true);
        assert_eq!(correct(223450), false);
        assert_eq!(correct(123789), false);
    }

    #[test]
    fn test_correct_v2() {
        assert_eq!(correct_v2(112233), true);
        assert_eq!(correct_v2(123444), false);
        assert_eq!(correct_v2(111122), true);
        assert_eq!(correct_v2(112222), true);
    }
}