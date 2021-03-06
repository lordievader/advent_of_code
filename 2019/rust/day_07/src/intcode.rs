use std::fmt;

#[derive(Clone)]
pub struct Amp {
    pub state: Vec<i64>,
    pub index: usize,
    pub input_values: Vec<i64>,
    pub output_value: i64,
    pub finished: bool,
    pub relative_base: i64,
}

impl fmt::Display for Amp {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "(index: {index} {relative:?}; output: {output}; state: {state:?}",
         index=self.index, relative=self.input_values,
         output=&self.output_value, state=&self.state[0..20])
    }
}

fn registers(input: &Amp, mode_a: usize, mode_b: usize) -> (i64, i64){ 
    let output = input.state.to_vec();
    let reg_a;
    if mode_a == 1 {
        reg_a = output[input.index + 1];
    }
    else if mode_a == 2 {
        reg_a = output[input.relative_base as usize];
    }
    else {
        reg_a = output[output[input.index + 1] as usize];
    }

    let reg_b;
    if mode_b == 1 {
        reg_b = output[input.index + 2];
    }
    else if mode_b == 2 {
        reg_b = output[input.relative_base as usize];
    }
    else if mode_b == 99 {
        reg_b = 0;
    }
    else {
        reg_b = output[output[input.index + 2] as usize];
    }
    (reg_a, reg_b)
}

fn op_add(input: &Amp, mode_a: usize, mode_b: usize) -> Amp {
    let mut out_amp = input.clone();
    let mut output = input.state.to_vec();
    let (reg_a, reg_b) = registers(input, mode_a, mode_b);
    let outcome = reg_a + reg_b;
    // println!("{} add {} + {} -> {}", input.index, reg_a, reg_b, outcome);
    output[input.state[input.index + 3] as usize] = outcome;
    out_amp.index += 4;
    out_amp.state = output;
    out_amp
}

fn op_mul(input: &Amp, mode_a: usize, mode_b: usize) -> Amp {
    let mut out_amp = input.clone();
    let mut output = input.state.to_vec();
    let (reg_a, reg_b) = registers(input, mode_a, mode_b);
    let outcome = reg_a * reg_b;
    // println!("{} mul {} * {} -> {}", input.index, reg_a, reg_b, outcome);
    output[input.state[input.index + 3] as usize] = outcome;
    out_amp.index += 4;
    out_amp.state = output;
    out_amp
}

fn op_input(input: &Amp, mode_a: usize) -> Amp {
    let mut out_amp = input.clone();
    let mut output = input.state.to_vec();
    let mut input_values = input.input_values.to_vec();
    let input_value = input_values.pop().unwrap();
    let location = input.state[(input.index + 1) as usize] as usize;
    // println!("{} input {} -> {}", input.index, input_value, location);
    output[location] = input_value;
    out_amp.index += 2;
    out_amp.state = output;
    out_amp.input_values = input_values;
    out_amp

}

fn op_output(input: &Amp, mode_a: usize) -> Amp {
    let mut out_amp = input.clone();
    let output = input.state.to_vec();
    let output_value;
    if mode_a == 1 {
        output_value = output[input.index + 1];
    }
    else if mode_a == 2 {
        output_value = output[input.relative_base as usize];
    }
    else {
        output_value = output[output[(input.index + 1) as usize] as usize];
    }
    // println!("{} output {}", input.index, output_value);
    out_amp.output_value = output_value;
    out_amp.index += 2;
    out_amp
}

fn op_jit(input: &Amp, mode_a: usize, mode_b: usize) -> Amp {
    let mut out_amp = input.clone();
    let output = input.state.to_vec();
    let (reg_a, reg_b) = registers(input, mode_a, mode_b);
    if reg_a != 0 {
        out_amp.index = reg_b as usize;
    }
    else {
        out_amp.index += 3;
    }
    out_amp
}

fn op_jif(input: &Amp, mode_a: usize, mode_b: usize) -> Amp {
    let mut out_amp = input.clone();
    let output = input.state.to_vec();
    let (reg_a, reg_b) = registers(input, mode_a, mode_b);
    if reg_a == 0 {
        out_amp.index = reg_b as usize;
    }
    else {
        out_amp.index += 3;
    }
    out_amp
}

fn op_lt(input: &Amp, mode_a: usize, mode_b: usize) -> Amp {
    let mut out_amp = input.clone();
    let mut output = input.state.to_vec();
    let (reg_a, reg_b) = registers(input, mode_a, mode_b);
    if reg_a < reg_b {
        output[input.state[input.index + 3] as usize] = 1;
    }
    else {
        output[input.state[input.index + 3] as usize] = 0;
    }
    out_amp.state = output;
    out_amp.index += 4;
    out_amp
}

fn op_eq(input: &Amp, mode_a: usize, mode_b: usize) -> Amp {
    let mut out_amp = input.clone();
    let mut output = input.state.to_vec();
    let (reg_a, reg_b) = registers(input, mode_a, mode_b);
    if reg_a == reg_b {
        output[input.state[input.index + 3] as usize] = 1;
    }
    else {
        output[input.state[input.index + 3] as usize] = 0;
    }
    out_amp.state = output;
    out_amp.index += 4;
    out_amp
}

fn op_base(input: &Amp, mode_a: usize) -> Amp {
    let mut out_amp = input.clone();
    let (reg_a, _) = registers(input, mode_a, 99);
    out_amp.relative_base += reg_a;
    out_amp.index += 2;
    out_amp
}

pub fn execute(input: &Amp) -> Amp {
    let mut amp = input.clone();
    let length = input.state.len();
    let mem_size = 100000;
    if length < mem_size {
        let mut copy = input.state.to_vec();
        let mut memory = vec![0; mem_size - length];
        copy.append(&mut memory);
        amp.state = copy;
    }

    loop {
        let opcode = amp.state[amp.index];
        // println!("Opcode: {}, state: {}", opcode, amp);
        if opcode == 99 {
            amp.finished = true;
            break;
        }
        amp = match opcode {
            1 =>    op_add(&amp, 0, 0),
            101 =>  op_add(&amp, 1, 0),
            201 =>  op_add(&amp, 2, 0),
            1001 => op_add(&amp, 0, 1),
            2001 => op_add(&amp, 0, 2),
            1101 => op_add(&amp, 1, 1),
            2201 => op_add(&amp, 2, 2),

            2 =>    op_mul(&amp, 0, 0),
            102 =>  op_mul(&amp, 1, 0),
            202 =>  op_mul(&amp, 2, 0),
            1002 => op_mul(&amp, 0, 1),
            2002 => op_mul(&amp, 0, 2),
            1102 => op_mul(&amp, 1, 1),
            2202 => op_mul(&amp, 2, 2),

            3 =>    op_input(&amp, 0),
            103 =>  op_input(&amp, 1),
            203 =>  op_input(&amp, 2),

            4 =>   op_output(&amp, 0),
            104 => op_output(&amp, 1),
            204 => op_output(&amp, 2),

            5 =>    op_jit(&amp, 0, 0),
            105 =>  op_jit(&amp, 1, 0),
            205 =>  op_jit(&amp, 2, 0),
            1005 => op_jit(&amp, 0, 1),
            2005 => op_jit(&amp, 0, 2),
            1105 => op_jit(&amp, 1, 1),
            2205 => op_jit(&amp, 2, 2),

            6 =>    op_jif(&amp, 0, 0),
            106 =>  op_jif(&amp, 1, 0),
            206 =>  op_jif(&amp, 2, 0),
            1006 => op_jif(&amp, 0, 1),
            2006 => op_jif(&amp, 0, 2),
            1106 => op_jif(&amp, 1, 1),
            2206 => op_jif(&amp, 2, 2),

            7 =>    op_lt(&amp, 0, 0),
            107 =>  op_lt(&amp, 1, 0),
            207 =>  op_lt(&amp, 2, 0),
            1007 => op_lt(&amp, 0, 1),
            2007 => op_lt(&amp, 0, 2),
            1107 => op_lt(&amp, 1, 1),
            2207 => op_lt(&amp, 1, 2),


            8 =>    op_eq(&amp, 0, 0),
            108 =>  op_eq(&amp, 1, 0),
            208 =>  op_eq(&amp, 2, 0),
            1008 => op_eq(&amp, 0, 1),
            2008 => op_eq(&amp, 0, 2),
            1108 => op_eq(&amp, 1, 1),
            2208 => op_eq(&amp, 2, 2),

            9 =>    op_base(&amp, 0),
            109 =>  op_base(&amp, 1),
            209 =>  op_base(&amp, 2),

            _ => break,
        };
        if amp.index >= length || vec![4, 104, 204].contains(&opcode) {
            break;
        }
    }
    // println!("");
    amp
}


mod tests{
    use super::*;

    #[test]
    fn test_add(){
        let amp = Amp {
            state: vec![1, 0, 0, 0, 99],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_add(&amp, 0, 0);
        assert_eq!(output.state, vec![2, 0, 0, 0, 99]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);

        let amp = Amp {
            state: vec![1001, 4, 3, 4, 33],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_add(&amp, 0, 1);
        assert_eq!(output.state, vec![1001, 4, 3, 4, 36]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);

        let amp = Amp {
            state: vec![0101, 4, 3, 4, 33],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_add(&amp, 1, 0);
        assert_eq!(output.state, vec![0101, 4, 3, 4, 8]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);

        let amp = Amp {
            state: vec![1101, 4, 3, 4, 33],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_add(&amp, 1, 1);
        assert_eq!(output.state, vec![1101, 4, 3, 4, 7]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);

        let amp = Amp {
            state: vec![201, 4, 3, 4, 33],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_add(&amp, 2, 0);
        assert_eq!(output.state, vec![201, 4, 3, 4, 205]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);

        let amp = Amp {
            state: vec![2001, 4, 3, 4, 33],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_add(&amp, 0, 2);
        assert_eq!(output.state, vec![2001, 4, 3, 4, 2034]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);
    }

    #[test]
    fn test_mul(){
        let amp = Amp {
            state: vec![2, 3, 0, 3, 99],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_mul(&amp, 0, 0);
        assert_eq!(output.state, vec![2, 3, 0, 6, 99]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);

        let amp = Amp {
            state: vec![1002, 4, 3, 4, 33],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_mul(&amp, 0, 1);
        assert_eq!(output.state, vec![1002, 4, 3, 4, 99]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);

        let amp = Amp {
            state: vec![102, 4, 3, 4, 33],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_mul(&amp, 1, 0);
        assert_eq!(output.state, vec![102, 4, 3, 4, 16]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);

        let amp = Amp {
            state: vec![1102, 4, 3, 4, 33],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_mul(&amp, 1, 1);
        assert_eq!(output.state, vec![1102, 4, 3, 4, 12]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);
    }

    #[test]
    fn test_input(){
        let amp = Amp {
            state: vec![3, 3, 0, 3, 99],
            index: 0,
            input_values: vec![5],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_input(&amp, 0);
        assert_eq!(output.state, vec![3, 3, 0, 5, 99]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 2);
    }

    #[test]
    fn test_output(){
        let amp = Amp {
            state: vec![4, 3, 0, 3, 99],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_output(&amp, 0);
        assert_eq!(output.state, vec![4, 3, 0, 3, 99]);
        assert_eq!(output.output_value, 3);
        assert_eq!(output.index, 2);

        let amp = Amp {
            state: vec![4, 3, 0, 3, 99],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_output(&amp, 1);
        assert_eq!(output.state, vec![4, 3, 0, 3, 99]);
        assert_eq!(output.output_value, 3);
        assert_eq!(output.index, 2);
    }

    #[test]
    fn test_jit(){
        let amp = Amp {
            state: vec![5, 0, 0, 3, 99],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_jit(&amp, 0, 0);
        assert_eq!(output.state, vec![5, 0, 0, 3, 99]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 5);

        let amp = Amp {
            state: vec![5, 0, 0, 3, 99],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_jit(&amp, 0, 1);
        assert_eq!(output.state, vec![5, 0, 0, 3, 99]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 0);

        let amp = Amp {
            state: vec![5, 0, 0, 3, 99],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_jit(&amp, 1, 0);
        assert_eq!(output.state, vec![5, 0, 0, 3, 99]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 3);

        let amp = Amp {
            state: vec![5, 0, 0, 3, 99],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_jit(&amp, 1, 1);
        assert_eq!(output.state, vec![5, 0, 0, 3, 99]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 3);
    }

    #[test]
    fn test_jif(){
        let amp = Amp {
            state: vec![6, 0, 0, 3, 99],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_jif(&amp, 0, 0);
        assert_eq!(output.state, vec![6, 0, 0, 3, 99]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 3);
        
        let amp = Amp {
            state: vec![6, 0, 0, 3, 99],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_jif(&amp, 0, 1);
        assert_eq!(output.state, vec![6, 0, 0, 3, 99]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 3);
        
        let amp = Amp {
            state: vec![6, 0, 0, 3, 99],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_jif(&amp, 1, 0);
        assert_eq!(output.state, vec![6, 0, 0, 3, 99]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 6);
        
        let amp = Amp {
            state: vec![6, 0, 0, 3, 99],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_jif(&amp, 1, 1);
        assert_eq!(output.state, vec![6, 0, 0, 3, 99]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 0);
    }

    #[test]
    fn test_lt(){
        let amp = Amp {
            state: vec![7, 3, 4, 0, 1],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_lt(&amp, 0, 0);
        assert_eq!(output.state, vec![1, 3, 4, 0, 1]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);

        let amp = Amp {
            state: vec![7, 0, 1, 3, 1],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_lt(&amp, 1, 1);
        assert_eq!(output.state, vec![7, 0, 1, 1, 1]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);
    }

    #[test]
    fn test_eq(){
        let amp = Amp {
            state: vec![8, 3, 4, 0, 0],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_eq(&amp, 0, 0);
        assert_eq!(output.state, vec![1, 3, 4, 0, 0]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);

        let amp = Amp {
            state: vec![8, 3, 4, 0, 1],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_eq(&amp, 0, 0);
        assert_eq!(output.state, vec![0, 3, 4, 0, 1]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);

        let amp = Amp {
            state: vec![1108, 0, 1, 3, 1],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_eq(&amp, 1, 1);
        assert_eq!(output.state, vec![1108, 0, 1, 0, 1]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);

        let amp = Amp {
            state: vec![1108, 0, 0, 3, 1],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_eq(&amp, 1, 1);
        assert_eq!(output.state, vec![1108, 0, 0, 1, 1]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 4);
    }

    #[test]
    fn test_base(){
        let amp = Amp {
            state: vec![9, 3, 4, 0, 0],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_base(&amp, 0);
        assert_eq!(output.state, vec![9, 3, 4, 0, 0]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 2);
        assert_eq!(output.relative_base, 0);
        
        let amp = Amp {
            state: vec![109, 19, 4, 0, 0],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 2000,
        };
        let output = op_base(&amp, 1);
        assert_eq!(output.state, vec![109, 19, 4, 0, 0]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 2);
        assert_eq!(output.relative_base, 2019);
        
        let amp = Amp {
            state: vec![209, 3, 4, 0, 0],
            index: 0,
            input_values: vec![0],
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let output = op_base(&amp, 2);
        assert_eq!(output.state, vec![209, 3, 4, 0, 0]);
        assert_eq!(output.output_value, 0);
        assert_eq!(output.index, 2);
        assert_eq!(output.relative_base, 209);
    }

    fn run_program(program: Vec<i64>, input: Vec<i64>, finished: Vec<i64>, output: i64, ) {
        let amp = Amp {
            state: program.to_vec(),
            index: 0,
            input_values: input,
            output_value: 0,
            finished: false,
            relative_base: 0,
        };
        let mut state = execute(&amp);
        while state.finished == false {
            state = execute(&state);
        }

        let length = program.len();
        assert_eq!(
            state.state[0..length].to_vec(),
            finished
        );
        assert_eq!(
            state.output_value,
            output
        )
    }

    #[test]
    fn test_execute(){
        run_program(
            vec![1,0,0,0,99],
            vec![0],
            vec![2,0,0,0,99],
            0
        );

        run_program(
            vec![1002, 4, 3, 4, 33],
            vec![0],
            vec![1002,4,3,4,99],
            0
        );

        run_program(
            vec![2, 3, 0, 3, 99],
            vec![0],
            vec![2, 3, 0, 6, 99],
            0
        );

        run_program(
            vec![2, 4, 4, 5, 99, 0],
            vec![0],
            vec![2, 4, 4, 5, 99, 9801],
            0
        );

        run_program(
            vec![1, 1, 1, 4, 99, 5, 6, 0, 99],
            vec![0],
            vec![30,1,1,4,2,5,6,0,99],
            0
        );

        run_program(
            vec![3, 0, 4, 0, 99],
            vec![5],
            vec![5, 0, 4, 0, 99],
            5
        );


        run_program(
            vec![3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],
            vec![5],
            vec![3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, 5, 1, 1, 9],
            1
        );

        run_program(
            vec![3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],
            vec![0],
            vec![3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, 0, 0, 1, 9],
            0
        );

        run_program(
            vec![3,3,1105,-1,9,1101,0,0,12,4,12,99,1],
            vec![5],
            vec![3,3,1105,5,9,1101,0,0,12,4,12,99,1],
            1
        );

        run_program(
            vec![3,3,1105,-1,9,1101,0,0,12,4,12,99,1],
            vec![0],
            vec![3,3,1105,0,9,1101,0,0,12,4,12,99,0],
            0
        );

        run_program(
            vec![109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99],
            vec![0],
            vec![109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99],
            0
        );

        run_program(
            vec![1102,34915192,34915192,7,4,7,99,0],
            vec![0],
            vec![1102,34915192,34915192,7,4,7,99,1219070632396864],
            1219070632396864
        );

        run_program(
            vec![104,1125899906842624,99],
            vec![0],
            vec![104,1125899906842624,99],
            1125899906842624
        );
    }
}