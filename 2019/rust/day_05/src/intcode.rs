fn registers(input: &Vec<i32>, index: usize, immediate_a: bool, immediate_b: bool) -> (i32, i32){ 
    let output = input.to_vec();
    let reg_a;
    if immediate_a == true {
        reg_a = output[index + 1];
    }
    else {
        reg_a = output[output[index + 1] as usize];
    }

    let reg_b;
    if immediate_b == true {
        reg_b = output[index + 2];
    }
    else {
        reg_b = output[output[index + 2] as usize];
    }
    (reg_a, reg_b)
}

fn op_add(input: &Vec<i32>, index: usize, immediate_a: bool, immediate_b: bool) -> (i32, Vec<i32>, i32) {
    let mut output = input.to_vec();
    let (reg_a, reg_b) = registers(&output, index, immediate_a, immediate_b);
    let outcome = reg_a + reg_b;
    output[input[index + 3] as usize] = outcome;
    (0, output, 4)
}

fn op_mul(input: &Vec<i32>, index: usize, immediate_a: bool, immediate_b: bool) -> (i32, Vec<i32>, i32) {
    let mut output = input.to_vec();
    let (reg_a, reg_b) = registers(&output, index, immediate_a, immediate_b);
    let outcome = reg_a * reg_b;
    output[input[index + 3] as usize] = outcome;
    (0, output, 4)
}

fn op_input(input: &Vec<i32>, index: usize, value: i32) -> (i32, Vec<i32>, i32) {
    let mut output = input.to_vec();
    let outcome_location = input[(index + 3) as usize];
    output[outcome_location as usize] = value;
    (0, output, 2)
}

fn op_output(input: &Vec<i32>, index: usize, immediate_a: bool) -> (i32, Vec<i32>, i32) {
    let output = input.to_vec();
    let output_value;
    if immediate_a == true {
        output_value = output[index + 1];
    }
    else{
        output_value = output[output[(index + 1) as usize] as usize];
    }
    (output_value, output, 2)
}

fn op_jit(input: &Vec<i32>, index: usize, immediate_a: bool, immediate_b: bool) -> (i32, Vec<i32>, i32) {
    let output = input.to_vec();
    let (reg_a, reg_b) = registers(&output, index, immediate_a, immediate_b);
    let mut jump = 3;
    
    if reg_a != 0 {
        jump = reg_b - index as i32;
    }
    (0, output, jump)
}

fn op_jif(input: &Vec<i32>, index: usize, immediate_a: bool, immediate_b: bool) -> (i32, Vec<i32>, i32) {
    let output = input.to_vec();
    let (reg_a, reg_b) = registers(&output, index, immediate_a, immediate_b);
    let mut jump = 3;
    
    if reg_a == 0 {
        jump = reg_b - index as i32;
    }
    (0, output, jump)
}

fn op_lt(input: &Vec<i32>, index: usize, immediate_a: bool, immediate_b: bool) -> (i32, Vec<i32>, i32) {
    let mut output = input.to_vec();
    let (reg_a, reg_b) = registers(&output, index, immediate_a, immediate_b);
    if reg_a < reg_b {
        output[input[index + 3] as usize] = 1;
    }
    else {
        output[input[index + 3] as usize] = 0;
    }
    (0, output, 4)
}

fn op_eq(input: &Vec<i32>, index: usize, immediate_a: bool, immediate_b: bool) -> (i32, Vec<i32>, i32) {
    let mut output = input.to_vec();
    let (reg_a, reg_b) = registers(&output, index, immediate_a, immediate_b);
    if reg_a == reg_b {
        output[input[index + 3] as usize] = 1;
    }
    else {
        output[input[index + 3] as usize] = 0;
    }
    (0, output, 4)
}

pub fn execute(input: &Vec<i32>, input_value: i32) -> (i32, Vec<i32>) {
    let length = input.len();
    let mut output_value = 0;
    let mut output = input.to_vec();
    let mut index = 0;
    loop {
        let opcode = output[index];
        // dbg!(opcode);
        if opcode == 99 {
            break;
        }
        let result = match opcode {
            1 => op_add(&output, index, false, false),
            101 => op_add(&output, index, true, false),
            1001 => op_add(&output, index, false, true),
            1101 => op_add(&output, index, true, true),

            2 => op_mul(&output, index, false, false),
            102 => op_mul(&output, index, true, false),
            1002 => op_mul(&output, index, false, true),
            1102 => op_mul(&output, index, true, true),

            3 => op_input(&output, index, input_value),

            4 => op_output(&output, index, false),
            104 => op_output(&output, index, true),

            5 => op_jit(&output, index, false, false),
            105 => op_jit(&output, index, true, false),
            1005 => op_jit(&output, index, false, true),
            1105 => op_jit(&output, index, true, true),

            6 => op_jif(&output, index, false, false),
            106 => op_jif(&output, index, true, false),
            1006 => op_jif(&output, index, false, true),
            1106 => op_jif(&output, index, true, true),

            7 => op_lt(&output, index, false, false),
            107 => op_lt(&output, index, true, false),
            1007 => op_lt(&output, index, false, true),
            1107 => op_lt(&output, index, true, true),

            8 => op_eq(&output, index, false, false),
            108 => op_eq(&output, index, true, false),
            1008 => op_eq(&output, index, false, true),
            1108 => op_eq(&output, index, true, true),

            _ => break,
        };

        if opcode == 4 {
            output_value = result.0;
        }
        // println!("Ran: {:?}", &output[index..index+result.2 as usize]);
        output = result.1;
        index += result.2 as usize;
        if index >= length {
            break;
        }
    }
    // if index < length {
    //     println!("Stopped at: {}", index);
    // }
    (output_value, output)
}


mod tests{
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(op_add(&vec![1, 0, 0, 0, 99], 0, false, false), (0, vec![2, 0, 0, 0, 99], 4));
        assert_eq!(op_add(&vec![1001, 4, 3, 4, 33], 0, false, true), (0, vec![1001, 4, 3, 4, 36], 4));
        assert_eq!(op_add(&vec![0101, 4, 3, 4, 33], 0, true, false), (0, vec![0101, 4, 3, 4, 8], 4));
        assert_eq!(op_add(&vec![1101, 4, 3, 4, 33], 0, true, true), (0, vec![1101, 4, 3, 4, 7], 4));
    }

    #[test]
    fn test_mul(){
        assert_eq!(op_mul(&vec![2, 3, 0, 3, 99], 0, false, false), (0, vec![2, 3, 0, 6, 99], 4));
        assert_eq!(op_mul(&vec![1002, 4, 3, 4, 33], 0, false, true), (0, vec![1002, 4, 3, 4, 99], 4));
        assert_eq!(op_mul(&vec![0102, 4, 3, 4, 33], 0, true, false), (0, vec![0102, 4, 3, 4, 16], 4));
        assert_eq!(op_mul(&vec![1102, 4, 3, 4, 33], 0, true, true), (0, vec![1102, 4, 3, 4, 12], 4));
    }

    #[test]
    fn test_input(){
        assert_eq!(op_input(&vec![3, 3, 0, 3, 99], 0, 5), (0, vec![3, 3, 0, 5, 99], 2));
    }

    #[test]
    fn test_output(){
        assert_eq!(op_output(&vec![4, 3, 0, 3, 99], 0, false), (3, vec![4, 3, 0, 3, 99], 2));
        assert_eq!(op_output(&vec![4, 3, 0, 3, 99], 0, true), (3, vec![4, 3, 0, 3, 99], 2));
    }

    #[test]
    fn test_jit(){
        assert_eq!(op_jit(&vec![5, 0, 0, 3, 99], 0, false, false), (0, vec![5, 0, 0, 3, 99], 5));
        assert_eq!(op_jit(&vec![5, 0, 0, 3, 99], 0, false, true),  (0, vec![5, 0, 0, 3, 99], 0));
        assert_eq!(op_jit(&vec![5, 0, 0, 3, 99], 0, true, false),  (0, vec![5, 0, 0, 3, 99], 3));
        assert_eq!(op_jit(&vec![5, 0, 0, 3, 99], 0, true, true),   (0, vec![5, 0, 0, 3, 99], 3));
    }

    #[test]
    fn test_jif(){
        assert_eq!(op_jif(&vec![6, 0, 0, 3, 99], 0, false, false), (0, vec![6, 0, 0, 3, 99], 3));
        assert_eq!(op_jif(&vec![6, 0, 0, 3, 99], 0, false, true),  (0, vec![6, 0, 0, 3, 99], 3));
        assert_eq!(op_jif(&vec![6, 0, 0, 3, 99], 0, true, false),  (0, vec![6, 0, 0, 3, 99], 5));
        assert_eq!(op_jif(&vec![6, 0, 0, 3, 99], 0, true, true),   (0, vec![6, 0, 0, 3, 99], 0));
    }

    #[test]
    fn test_lt(){
        assert_eq!(op_lt(&vec![7, 3, 4, 0, 1], 0, false, false), (0, vec![1, 3, 4, 0, 1], 4));
        assert_eq!(op_lt(&vec![7, 0, 1, 3, 1], 0, true, true),   (0, vec![7, 0, 1, 1, 1], 4));
    }

    #[test]
    fn test_eq(){
        assert_eq!(op_eq(&vec![8, 3, 4, 0, 0], 0, false, false), (0, vec![1, 3, 4, 0, 0], 4));
        assert_eq!(op_eq(&vec![8, 3, 4, 0, 1], 0, false, false), (0, vec![0, 3, 4, 0, 1], 4));
        assert_eq!(op_eq(&vec![8, 0, 1, 3, 1], 0, true, true),   (0, vec![8, 0, 1, 0, 1], 4));
        assert_eq!(op_eq(&vec![8, 0, 0, 3, 1], 0, true, true),   (0, vec![8, 0, 0, 1, 1], 4));
    }

    #[test]
    fn test_execute(){
        assert_eq!(execute(&vec![1002, 4, 3, 4, 33], 0), (0, vec![1002, 4, 3, 4, 99]));
        assert_eq!(execute(&vec![1, 0, 0, 0, 99], 5), (0, vec![2, 0, 0, 0, 99]));
        assert_eq!(execute(&vec![2, 3, 0, 3, 99], 5), (0, vec![2, 3, 0, 6, 99]));
        assert_eq!(execute(&vec![2, 4, 4, 5, 99, 0], 5), (0, vec![2, 4, 4, 5, 99, 9801]));
        assert_eq!(execute(&vec![1, 1, 1, 4, 99, 5, 6, 0, 99], 5), (0, vec![30, 1, 1, 4, 2, 5, 6, 0, 99]));
        assert_eq!(execute(&vec![3, 0, 4, 0, 99], 5), (5, vec![5, 0, 4, 0, 99]));

        assert_eq!(
            execute(&vec![3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0),
            (0, vec![3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, 0, 0, 1, 9])
        );
    }
}