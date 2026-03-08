`timescale 1ps/1ps
`include "mem.v"

`timescale 1ns/1ps

module tb_mem;
    parameter ADDR_WIDTH = 8;
    parameter DATA_WIDTH = 8;
    reg clk;
    reg ce;
    reg we;
    reg oe;
    reg [ADDR_WIDTH-1:0] addr;
    reg [DATA_WIDTH-1:0] din;
    wire [DATA_WIDTH-1:0] dout;
    simple_sram #(
        .ADDR_WIDTH(ADDR_WIDTH),
        .DATA_WIDTH(DATA_WIDTH)
    ) dut (
        .clk(clk),
        .ce(ce),
        .we(we),
        .oe(oe),
        .addr(addr),
        .din(din),
        .dout(dout)
    );

    always #5 clk = ~clk;

    initial begin
        clk  = 0;
        ce   = 0;
        we   = 0;
        oe   = 0;
        addr = 0;
        din  = 0;

        #20;
        $display("Starting WRITE test...");
        ce   = 1;
        we   = 1;
        oe   = 0;

        addr = 8'h05; 
        din  = 8'hAA;
        #10;

        addr = 8'h0A;
        din  = 8'h55;
        #10;

        we = 0; // Stop writing

        // =========================
        // READ TEST
        // =========================
        $display("Starting READ test...");
        oe = 1;

        addr = 8'h05;
        #10;
        $display("Read Addr 0x05 = %h (Expected AA)", dout);

        addr = 8'h0A;
        #10;
        $display("Read Addr 0x0A = %h (Expected 55)", dout);

        // =========================
        // SIMULTANEOUS WRITE + READ TEST
        // =========================
        $display("Testing Write + Read same cycle...");
        we = 1;
        addr = 8'h05;
        din  = 8'hFF;
        #10;

        we = 0;
        #10;
        $display("Read Addr 0x05 = %h (Expected FF)", dout);

        // Finish simulation
        #20;
        $display("Simulation finished.");
        $stop;
    end

endmodule