
use cpython::{py_module_initializer, py_fn};

// import all symbols (cant access through namespace in py_module_initializer macro)

py_module_initializer! {
  utility, |py, module| {
    // misc
    module.add(py, "__doc__", "This module is written in Rust")?;

    Ok(())
  }
}
