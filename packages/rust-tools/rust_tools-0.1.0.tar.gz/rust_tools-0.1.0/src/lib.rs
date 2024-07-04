use pyo3::PyResult;
use std::collections::HashMap;
use std::fs::File;
use std::io::{self, Write};
use needletail::{parse_fastx_file, FastxReader};
use pyo3::{pymodule, wrap_pyfunction, pyfunction, Python};
use pyo3::types::PyModule;

use std::io::prelude::*;


#[pyfunction]
fn create_labeled_subreads(UMIdict: HashMap<String, (String, u32)>, subread_files: &str, out2: &str) -> PyResult<()> {
    let mut out_sub = File::create(out2).expect("Failed to create output file");
    
    let files: Vec<&str> = subread_files.split(',').collect();
    
    for subread_file in files {
        // Use needletail to parse the FASTX file
        println!("Parsing file start!");
        let mut reader = parse_fastx_file(subread_file).expect("Expecting a valid FASTX file");
        println!("File parsed!");

        while let Some(record) = reader.next() {
            let seq_record = record.expect("Failed to read record");
            let name = std::str::from_utf8(seq_record.id().as_ref()).expect("Failed to convert sequence ID").to_string();
            let seq = std::str::from_utf8(seq_record.seq().as_ref()).expect("Failed to convert sequence").to_string();
            let q = std::str::from_utf8(seq_record.qual().unwrap().as_ref()).expect("Failed to convert quality scores").to_string();
            
            let root = name.split('_').next().unwrap();
            
            if let Some((UMI, number)) = UMIdict.get(root) {
                let line = format!("{}\t{}\t{}\t{}\t{}\n", number, UMI, name, seq, q);
                out_sub.write_all(line.as_bytes()).expect("Failed to write to output file");
            }
        }
    }
    
    out_sub.flush().expect("Failed to flush output file");
    Ok(())
}

#[pymodule]
fn rust_tools(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(create_labeled_subreads, m)?)?;
    Ok(())
}
