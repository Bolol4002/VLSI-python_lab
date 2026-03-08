set testbenches {exptestbench01 exptestbench02 exptestbench03 exptestbench04 exptestbench05 exptestbench06 exptestbench07 exptestbench08}

foreach tb $testbenches {
    puts "Running simulation for $tb"
    set_property top $tb [get_filesets sim_1]
    launch_simulation -simset sim_1 -mode behavioral
    run all
    close_sim
}